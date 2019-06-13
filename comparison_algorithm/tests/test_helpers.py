import pytest
from diggrtoolbox.linking.helpers import *


#remove_tm tests
@pytest.mark.parametrize(
    "test_input, expected_output",
    [
        ("", ""),
        ("Title(TM)", "Title"),
        ("(R)", "")
    ]
    )
def test_remove_tm(test_input, expected_output):
    assert remove_tm(test_input) == expected_output


#word_before_after tests
@pytest.mark.parametrize(
    "test_string, test_sep, output",
    [
        ("Final Fantasy Adventure", "Fantasy", ("Final", "Adventure")),
        ("Final Fantasy Adventure", "Final", ("", "Fantasy")),
        ("Final Fantasy Adventure", "Adventure", ("Fantasy", "")),
        ("Final Fantasy Adventure", "X", ("","")),
        ("Final Fantasy 5: The Finalising", "5", ("Fantasy", ":"))
    ]
)
def test_word_before_after(test_string, test_sep, output):
    assert word_before_after(test_string, test_sep) == output

#load series test
def test_load_series():
    series = load_series()
    assert isinstance(series, list)
    assert "SIMPLE" in series

# test removing numbers from string
@pytest.mark.parametrize(
    "test_input, expected_output",
    [
        ("Mario Party 2", "Mario Party"),
        ("Call of Duty IV: Whatever", "Call of Duty: Whatever"),
        ("Final Fantasy X/X-2", "Final Fantasy /-")
    ]
    )
def test_remove_numbers(test_input, expected_output):
    assert remove_numbers(test_input) == expected_output