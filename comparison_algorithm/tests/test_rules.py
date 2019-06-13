import pytest
from diggrtoolbox.linking.rules import *
from diggrtoolbox.linking.config import *

# FIRST LETTER RULE TESTS
@pytest.mark.parametrize(
    "test_a, test_b, output",
    [
        ("", "", 0),
        (None, None, 0),
        (None, "abc", 0),
        ("abc", None, 0),
        ("Abc", "abc", 0),
        ("four word title yes", "yes four world title", 0),
        ("two words", "Two wordtitle", 0),
        ("Two words", "another title", 0),
        ("Title", "Wrongtitle", NUMBERING_WEIGHT)
    ]
)
def test_first_letter_rule(test_a, test_b, output):
    assert first_letter_rule(test_a, test_b) == output


# NUMBERING RULE TESTS
@pytest.mark.parametrize(
    "test_a, test_b, output",
    [
        ("","", 0),
        ("Fifa 2014", "Fifa 2015", NUMBERING_WEIGHT),
        ("FINAL FANTASY X", "Final Fantasy 10", 0),
        ("THE WITCHER III WILD HUNT", "The Witcher 3: Wild Hunt", 0),
        ("The Witcher II", "The Witcher", NUMBERING_WEIGHT),
        ("Final Fantasy Reishiki HD", "Final Fantasy XV", NUMBERING_WEIGHT),
        ("Star Ocean 4: The Last Hope", "Star Ocean IV: The Last Hope", 0),
        ("TWO WORLDS 2", "Two Worlds II", 0),
        ("Ys III Wanderer", "Ys III: Wanderer", 0),
        ("left 4 dead", "Left 4 Dead 2", NUMBERING_WEIGHT),
        ("Yada 2012", "yada 12", 0),
        ("Test 4004", "test 04",NUMBERING_WEIGHT),
        ("Eisenbahn 6.0 exe", "Eisenbahn 6",0)
    ]
)
def test_numbering_rule(test_a, test_b, output):
    assert numbering_rule(test_a,test_b) == output