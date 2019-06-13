#!/usr/bin/env python3
"""
link module for linking datasets
"""

from itertools import product
import random
import Levenshtein as lev
from .rules import *
from .helpers import remove_tm, std, load_series, remove_numbers
from .config import *

__author__ = "Florian Rämisch and Peter Mühleder"
__copyright = "Copyright 2017, Universitätsbibliothek Leipzig"
__email__ = "team@diggr.link"


#MATCHING RULES & FILTERS
ALL_RULES = [first_letter_rule, numbering_rule]

#PREPROCESSING
REMOVE_SERIES = load_series()

def _pre_processing(a):
    """
    inital steps of preparing string :a: for matching
    """
    if a:
        a = remove_tm(a)
        a = a.replace("Ⅱ", "II")
        a = a.split("(")[0]
        a = a.replace("〔", "").replace("〕","")

        for series in REMOVE_SERIES:
            if series in a:
                a = a.replace(series+" Series","")
                break
    return a.strip()

def match_titles(titles_a,titles_b, rules=ALL_RULES):
    """
    Returns match value for two lists of titles.

    :titles_a: List of title strings
    :titles_b: List of title string
    :rules:    List of matching rules
    """
    best_ratio = 0
    for a, b in product(titles_a, titles_b):
        a = _pre_processing(a)
        b = _pre_processing(b)

        if a and b:
            weights = [ rule(a,b) for rule in rules ]

            a_no_numbers = remove_numbers(a)
            b_no_numbers = remove_numbers(b)

            r = lev.ratio(std(a_no_numbers),std(b_no_numbers)) - sum(weights)

            if r > best_ratio: best_ratio = r

    return best_ratio
