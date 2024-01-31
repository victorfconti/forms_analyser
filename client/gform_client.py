import json
from os import environ
from base64 import b64decode

from google.oauth2 import service_account
from apiclient import discovery


DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"
FORM_ID = '1Pa3oBEmPcb9wVQscwlBaxwNycVu6I4oTl4n-7i511iw'
raw_credentials = json.loads(b64decode(environ['CRED']))
credentials = service_account.Credentials.from_service_account_info(raw_credentials)


def get_book_form_answer():
    form_service = discovery.build('forms', 'v1', credentials=credentials)
    return form_service.forms().responses().list(formId=FORM_ID).execute()  # pylint: disable=maybe-no-member


def get_book_form():
    form_service = discovery.build('forms', 'v1', credentials=credentials)
    return form_service.forms().get(formId=FORM_ID).execute()  # pylint: disable=maybe-no-member
