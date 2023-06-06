'''
This provide the necessary credentials and set up the enviroment
'''
import json
import os
from deep_translator import MyMemoryTranslator

#Translation from english to french
def english_to_french(english_text):
    """Function that translate english to french"""
    french_text= MyMemoryTranslator(source='english', target='french').translate(english_text)
    return french_text

#Translation from french to english
def french_to_english(french_text):
    """Function that translate french to english"""
    english_text= MyMemoryTranslator(source='french', target='english').translate(french_text)
    return english_text
