# Game Title Comparison Algorithm


## Usage

The comparison function takes two sets of game titles. A set can contain titles for a game (translations, alternative spellings, etc.).

Every entry in a set is compared to each entry in the other set. The best 
result (a value between 0.0 and 1.0) will be returned.

E.g. 
```python

from comparison_algorithm import cmp_titles

cmp_titles(
    ["Final Fantasy VII"],
    ["FF 7", "Final Fantasy 7"]
)
```
returns 1.0

## Preprocessing

* Remove trademark symbols
* Replace Ⅱ symbol with correct roman numeral II
* Remove brackets (with content)
* Remove〔〕brackets
* Remove common (Japanese) game series names from titles (e.g. "SIMPLE 1500")

## Standardization

Before comparison the title strings will be standardized:
* Remove articles ("The", ...)
* Remove punctuation
* Standardize Japanese macron and vowel transcription
* Set to lower case

## Rules

The comparision is based on Levenshtein distance between the two strings.
Additionaly, some rules were implemented to take specific features of game titles into account.

### Numbering

Using Levensthein distance, a differnt number in games title can still result in a high similarity score in the case of longer titles. This rule therefore adds a penalty weight if the numbers in the titles mismatch.
Additionally, this rule considers:
* roman and arabic numerals are treated as the same value
* position of the number in the title  

### First letter

This rule adds a penalty weight if the first letter of the strings mismatch. (Only applied in case of short titles).