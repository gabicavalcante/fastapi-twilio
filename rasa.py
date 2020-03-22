from rasa_nlu.model import Interpreter

import os

rasa_model_path = os.path.abspath("rasa/models/20200321-174355.tar.gz")
print(rasa_model_path)

interpreter = Interpreter.load(rasa_model_path)


def rasa_output(text):
    message = str(text).strip()
    result = interpreter.parse(message)
    return result


rasa_output("hello")
