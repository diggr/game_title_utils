#!/usr/bin/env python3
"""
diggrlink helpers module contains helper functions used for dataset linking
"""


import roman
import re
import string
import os

__author__ = "Florian Rämisch and Peter Mühleder"
__copyright = "Copyright 2017, Universitätsbibliothek Leipzig"
__email__ = "team@diggr.link"


#CONSTANTS
PUNCT_TRANSTABLE = str.maketrans("","",".,:-〔〕'’*/!&?+ ")
REMOVE_TM = ["™","®","(TM)", "(R)"]


#REGULAR EXPRESSIONS
ROMAN_NUMERAL_REGEX = r'\b(M{1,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})|M{0,4}(CM|C?D|D?C{1,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})|M{0,4}(CM|CD|D?C{0,3})(XC|X?L|L?X{1,3})(IX|IV|V?I{0,3})|M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|I?V|V?I{1,3}))\b'
NUMBERING_REGEX = r'(\d+\.\d+|\d+)'

NUMBERING_RE = re.compile(NUMBERING_REGEX)
ROMAN_NUMERAL_RE = re.compile(ROMAN_NUMERAL_REGEX)


def load_excluded_titles():
    """
    Load list of excudled titles from resource file
    """
    file_name = os.path.join(os.path.dirname(__file__), "resources/exclude.txt")
    with open(file_name) as f:
        excluded_titles = f.readlines()
    return [ x.strip() for x in excluded_titles ]


def load_series():
    """
    Load list of series to remove from title
    """
    file_name = os.path.join(os.path.dirname(__file__), "resources/series.txt")
    with open(file_name) as f:
        series = f.readlines()
    return [ x.strip() for x in series ]


def remove_tm(a):
    """
    Removes trademark symbols from string :a:
    """
    for t in REMOVE_TM:
        a = a.replace(t, "")
    return a.strip()


def word_before_after(a, sep):
    """
    returns word before and after :sep: in string :a:
    """
    word_before, word_after = "", ""
    if sep in a:
        word_before = a.split(str(sep))[0].strip().split(" ")[-1]
        word_after = a.split(str(sep))[1].strip().split(" ")[0]
    return word_before, word_after


def std(a):
    """
    standardizes string :a: (removes punctuation, blanks, macrons; sets string to lower case)
    """
    if a:
        a = a.replace("The"," "). replace("・", " ").replace("THE", " ").replace("the", " ")
        #remove punctuations
        a = a.translate(PUNCT_TRANSTABLE)
        #remove macrons
        a = a.replace("ō", "o").replace("Ō", "O").replace("ū", "u").replace("Ū", "U")
        a = a.replace("ou", "o").replace("Ou", "O").replace("uu", "u").replace("Uu", "U").replace("nb", "mb")
        #remove blanks, lower case, strip string
        a = a.lower()
        return a
    else:
        return ""

def _get_position(a, n):
    """ returns position of substring :n: as "start", "end" or "middle" """
    position = a.index(n)
    if position == 0:
        return ("start", position)
    elif position+len(n) == len(a):
        return ("end", position)
    else:
        return ("middle", position)


def _extract_roman_numerals(a):
    """ extracts all roman numerals in string :a:, including their position and numerical value """
    rv = ROMAN_NUMERAL_RE.findall(a)
    rv = [no[0] for no in rv ]

    numbers = []

    for n in rv:
        position = _get_position(a, n)

        numbers.append({
            "type": "roman",
            "value": float(roman.fromRoman(n)),
            "position": position,
            "str": n
        })
    return numbers

def _extract_numbers(a):
    """
    returns all numbers in string :a:, their position and value als float.
    if number is identified as year, only the last two digits get set as value
    """

    rv = NUMBERING_RE.findall(a)

    numbers = []

    for n in rv:

        position = _get_position(a, n)

        #check if year
        if len(n) == 4 and n[0] in "12" and "." not in n:
            ntype = "year"
            value = int(n[2:])
        elif len(n) == 2 and n[0] in "890" and "." not in n:
            ntype = "year"
            value = int(n)
        #elso convert value to float
        else:
            ntype = "number"
            value = float(n)

        numbers.append({
            "type": ntype,
            "value": value,
            "position": position,
            "str": n
        })

    return numbers

def extract_all_numbers(a):
    """ returns all numbers (roman and arabic) in string :a: """

    numbers = _extract_numbers(a) + _extract_roman_numerals(a)
    sorted_numbers = sorted(numbers, key=lambda x: -x["position"][1])

    return sorted_numbers


def remove_numbers(a):
    """ removes all numbers (arabic and roman) from string a """
    a = NUMBERING_RE.sub("", a)
    a = ROMAN_NUMERAL_RE.sub("",a)
    a = re.sub(" +", " ", a)
    return a.replace(" :", ":").strip()