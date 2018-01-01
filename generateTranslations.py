from deeplTranslator.deeplTranslator import DeeplTranslator
import logging


"""
The purpose of this main file is to show how to use DeeplTranslator class
"""
if __name__ == '__main__':

    # Logging stuff
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler()
    handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter("%(asctime)s %(threadName)s %(levelname)s %(filename)s %(funcName)s: %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    dt = DeeplTranslator()

    dt.connect()

    sentence = "Lilou is beautifull."

    result = dt.translate(sentence, "EN", "FR")

    sentence = "J'aime bien le chocolat."

    result = dt.translate(sentence, "FR", "ES")
