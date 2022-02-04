'''
    Code to Translate text usin WATSON API
'''
import os
from ibm_watson import LanguageTranslatorV3, ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

def translate(text, model):
    '''
        Watson API call
    '''
    transtext = ''
    try:
        load_dotenv()
        apikey = os.environ['apikey']
        url = os.environ['url']

        authenticator = IAMAuthenticator(apikey)
        language_translator = LanguageTranslatorV3(version='2018-05-01',authenticator=authenticator)
        language_translator.set_service_url(url)

        transresponse = language_translator.translate(text=text, model_id=model)
        transjson=transresponse.get_result()
        transtext =transjson['translations'][0]['translation']

    except ApiException as err:
        print(err)
    except Exception as err:
        print(err)

    return transtext


def englishToFrench(englishText):
    '''
        Converts English text to French
    '''
    frenchText = translate(englishText, 'en-fr')
    return frenchText


def frenchToEnglish(frenchText):
    '''
        Converts French text to English
    '''
    englishText = translate(frenchText, 'fr-en')
    return englishText
