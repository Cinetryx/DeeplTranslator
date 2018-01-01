import requests
import logging
from bs4 import BeautifulSoup
import json


class DeeplTranslator(object):

    urlDeepl = 'https://www.deepl.com/'
    urlDeeplMainPage = urlDeepl + 'translator'
    urlDeeplJsonrpc = urlDeepl + 'jsonrpc'
    retRequest = None

    def __init__(self):
        self.session = requests.Session()
        self.logger = logging.getLogger()

    def connect(self):

        self.logger.info("Connect attempt...")

        self.retRequest = self.session.get(self.urlDeeplMainPage)

        soup = BeautifulSoup(self.retRequest.content, 'html.parser')
        self.logger.debug(soup.prettify())

    def translate(self, text, langSource, langTarget):

        self.logger.info("Translate attempt...")

        data = '{"jsonrpc":"2.0","method":"LMT_handle_jobs","params":{"jobs":[{"kind":"default","raw_en_sentence":"' + text + '"}],"lang":{"user_preferred_langs":["EN"],"source_lang_user_selected":"' + langSource + '","target_lang":"' + langTarget + '"},"priority":-1},"id":11}'

        self.retRequest = self.session.post(self.urlDeeplJsonrpc, data=data)

        returnedData = json.loads(self.retRequest.content.decode("utf-8"))

        result = returnedData['result']['translations'][0]['beams'][0]['postprocessed_sentence']

        self.logger.info(text + " ==> " + result)

        return result
