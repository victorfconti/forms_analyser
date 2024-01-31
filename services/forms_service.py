from typing import List, Tuple

from pandas import DataFrame

from client.gform_client import get_book_form, get_book_form_answer


class FormsService:

    def __init__(self):
        self.form = get_book_form()
        self.answers = FormsService.__transform_data(get_book_form_answer())
        self.questions_id_name = FormsService.__create_form_name_to_id(self.form)

    @staticmethod
    def __create_form_name_to_id(form_data: dict[str, any]) -> dict[str, str]:
        name_to_id: dict[str, str] = {}
        for item in form_data['items']:
            name_to_id[item['itemId']] = item['title']

        return name_to_id

    @staticmethod
    def __transform_data(responses: dict[str, any]) -> DataFrame:
        person_data: List[Tuple] = []

        for response in responses['responses']:
            print(response)

            city: str = FormsService.__extract_single_answer(response, '12822e20')

            age: int = FormsService.__extract_single_answer_int(response, '13e6871d')
            gender: str = FormsService.__extract_single_answer(response, '48e971ef')
            fav_gen: str = FormsService.__extract_single_answer(response, '7aaaed46')
            scholarship: str = FormsService.__extract_single_answer(response, '1a68573f')
            book_form: str = FormsService.__extract_single_answer(response, '3bca0437')

            person_data.append((age, gender, fav_gen, book_form, scholarship, city))

        columns: List[str] = ['age', 'gender', 'fav_gen', 'book_form', 'scholarship', 'city']
        person_data_df: DataFrame = DataFrame(person_data, columns=columns)
        print(person_data_df)
        return person_data_df

    @staticmethod
    def __extract_single_answer_int(response: dict[str, any], response_id: str) -> int:
        answer: str = FormsService.__extract_single_answer(response, response_id)
        if answer == "":
            return 0
        else:
            return int(answer)

    @staticmethod
    def __extract_single_answer(response: dict[str, any], response_id: str) -> str:
        if response_id in response['answers']:
            return response['answers'][response_id]['textAnswers']['answers'][0]['value']
        else:
            return ""
