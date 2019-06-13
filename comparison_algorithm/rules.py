#!/usr/bin/env python3
"""
module contains general matching rules
"""


__author__ = "Florian Rämisch and Peter Mühleder"
__copyright = "Copyright 2017, Universitätsbibliothek Leipzig"
__email__ = "team@diggr.link"


import re
import Levenshtein as lev
from .helpers import std, extract_all_numbers
from .config import *


#REGULAR EXPRESSIONS
NUMBERING_REGEX = r'(\d+.\d+|\d+)'


def numbering_rule(a, b):
    """ 
    Check two stings for number at the end or inbetween followed by a colon.
    If a number is found in both strings and if they do not match, return penalty value.
    """
    
    x, y = "nan", "nan"
    x_str = ""
    y_str = ""
    x_pos = ""
    y_pos = ""

    nums_a = extract_all_numbers(a)
    nums_b = extract_all_numbers(b)
    if nums_a != []:
        x = nums_a[0]["value"]
        x_str =  nums_a[0]["str"]
        x_pos = nums_a[0]["position"][0]
    if nums_b != []:
        y = nums_b[0]["value"]
        y_str = nums_b[0]["str"]
        y_pos = nums_b[0]["position"][0]

    if x_pos == "middle" and y == "nan":          
        check = a.replace(x_str, "")
        if lev.ratio(std(check), std(b)) == 1:
            return 0

    if y_pos == "middle" and x == "nan":
        check = b.replace(y_str, "")
        if lev.ratio(std(check), std(a)) == 1:
            return 0

    if x == y: 
        return 0
    else: 
        return NUMBERING_WEIGHT


def first_letter_rule(a,b):
    """
    checks if first letters of strings :a: and :b: when the strings contain max. 1 word
    """
    if a and b:
        if len(a.split(" ")) == 1 and len(b.split(" ")) == 1:
            if a[0].lower() != b[0].lower():
                return FIRST_LETTER_WEIGHT
    return 0