#!/usr/bin/env python3
"""Hello World Multi Lang

Displays the message "Hello World" based on environment lang.

Usage:

Set the variable LANG e.g.,

    export LANG=pt_BR

Execute:

    ./hello.py
"""
__version__ = "0.0.1"
__author__  = "claromes"
__license__ = "Unlicense"

import os

curr_lang = os.getenv("LANG", "en_US")[:5]

msg = "Hello World!"

if curr_lang == "pt_BR":
    msg = "Olá, Mundo!"
elif curr_lang == "it_IT":
    msg = "Ciao, Mondo!"
elif curr_lang == "es_SP":
    msg = "Hole, Mundo!"
elif curr_lang == "fr_FR":
    msg = "Bonjour Monde!"
    
print(msg)