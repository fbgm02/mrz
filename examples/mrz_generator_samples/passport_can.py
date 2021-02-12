#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Note for end users: #######################################################################
#
# Adding mrz (local) to PYTHONPATH to execute this example as a script without installing mrz
# (if it was installed using pip or setup.py the two lines below are not necessary)
from os.path import dirname, join, pardir, realpath
import sys
sys.path.append(realpath(join(dirname(__file__), pardir, pardir)))
##############################################################################################


from mrz.generator.td3 import *

td3_generator = TD3CodeGenerator("P",            # Document type   Normally 'P' for passport
                                 "CA",           # Country         3 letters code or country name
                                 "KHANUM",       # Surname(s)      Special characters will be transliterated
                                 "SUMERA",        # Given name(s)   Special characters will be transliterated
                                 "AP2792721",      # Passport number
                                 "CAN",          # Nationality     3 letter code or country name
                                 "750502",       # Birth date      YYMMDD
                                 "F",            # Genre           Male: 'M', Female: 'F' or Undefined 'X'
                                 "260922",       # Expiry date     YYMMDD
                                 "ID88933477")   # Id number       Not mandatory field

print(td3_generator)
print("\n")

td3_generator.country_code = "CAN"
td3_generator.document_number = "AP2792721"
td3_generator.nationality = "CAN"
td3_generator.expiry_date = "260922"
td3_generator.optional_data = ""

print(td3_generator)
