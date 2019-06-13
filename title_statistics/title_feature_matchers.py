#!/usr/bin/env python3
"""
This file contains the matchers.
"""

import re

NUMBER = r'\d+' # includes floating point numbers
FLOAT = r'\d+(\.\d+)'
ANY_NUMBER = '({0}|{1})'.format(NUMBER, FLOAT)
ROMAN_NUMERAL = r'\b(?=[MDCLXVI]+\b)M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})\b'
ANY_NUMERAL = '({0}|{1})'.format(ANY_NUMBER, ROMAN_NUMERAL)

PATTERNS = {
    'contains_one_number':  { 'pattern' : '^\D*{0}\D*$'.format(ANY_NUMBER),
                              'method'  : re.match },
    'contains_two_numbers': { 'pattern' : '^\D*{0}\D+{0}\D*$'.format(ANY_NUMBER),
                              'method'  : re.match },
    'starts_with_number':   { 'pattern' : '^{0}\D+'.format(NUMBER),
                              'method'  : re.match },
    'versus_vs':           { 'pattern' : r'(\b(vs|VS|versus|VERSUS|Versus)\b)',
                              'method'  : re.search },
    'and_And_AND':        { 'pattern' : r'&| [aA]nd | AND ',
                              'method'  : re.search },
    'the_The_THE':          { 'pattern' : r'\b([tT]he|THE)\b',
                              'method'  : re.search },
    'colon_or_minus':       { 'pattern' : r'(\:|-)',
                              'method'  : re.search },
    'directors_cut':        { 'pattern' : r"([dD]irector|DIRECTOR)'?(s|S) *([cC]ut|CUT)",
                              'method'  : re.search },
    'HD_remastered':        { 'pattern' : r'\b(HD|[rR]emastered|REMASTERED)\b',
                              'method'  : re.search },
    'editions':             { 'pattern' : r'\b([eE]dition|EDITION|[Tt]rilogy|TRILOGY|[cC]ollection|COLLECTION|[aA]nthology|ANTHOLOGY)\b',
                              'method'  : re.search },
    'apostrophes':          { 'pattern' : r"'",
                              'method'  : re.search },
    'famous_patron':        { 'pattern' : r'([tT]ony Hawk|[tT]om [cC]lancy|[pP]ixar|[dD]isney|[sS]id [mM]eier)',
                              'method'  : re.search },
    'contains_a_year':      { 'pattern' : r'\b([12](\d|k|K))?[0189]\d\b',
                              'method'  : re.search },
    'number_letter':        { 'pattern' : r'([a-zA-Z]+\d+|\d+[a-zA-Z])',
                              'method'  : re.search },
}

def match_feature(name, title, patterns=PATTERNS):
    """
    Applies a pattern from the pattern matchers to a string
    and returns True/False if matched or not.
    """
    if type(title) is not str:
        return False
    try:
        pattern = patterns[name]['pattern']
        method = patterns[name]['method']
    except KeyError:
        raise KeyError("No Pattern with name {0} found.".format(name))
    if method(pattern, title) is not None:
        return True
    else:
        return False
