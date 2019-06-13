#!/usr/bin/env python3
"""
Test Cases for the Title Feature Matchers.
"""


import pytest
from title_feature_matchers import PATTERNS, match_feature


@pytest.mark.parametrize("contains_one_number_in, contains_one_number_out", [
    ("Theatre of War 2: Africa 1943", False),
    ("High School Musical 3: Senior Year Dance", True),
    #("Battlefield 1942™ World War II Anthology", False),
    ("Eisenbahn.exe 6.0 Gold Edition", True),
    ("Superstars V8 Next Challenge", True),
    ("Moto GP2", True),
    ("MOTORM4X: Offroad Extreme", True),
    ("Left 4 Dead 2", False),
    ("688i - Hunter Killer", True),
    ("Elite Forces Unit 77", True),
    ("Euro Fishing", False)
])
def test_contains_one_number(contains_one_number_in, contains_one_number_out):
    assert match_feature('contains_one_number', contains_one_number_in) == contains_one_number_out


@pytest.mark.parametrize("contains_two_numbers_in, contains_two_numbers_out", [
    ("Theatre of War 2: Africa 1943", True),
    ("Left 4 Dead 2", True),
    ("Eisenbahn.exe 6.0 Gold Edition", True),
    ("688i - Hunter Killer", False),
    ("Euro Fishing", False),
    ("Final Fantasy X/X-2", False)
])
def test_two_numbers(contains_two_numbers_in, contains_two_numbers_out):
    assert match_feature('contains_two_numbers', contains_two_numbers_in) == contains_two_numbers_out


@pytest.mark.parametrize("starts_with_number_in, starts_with_number_out", [
    ("Theatre of War 2: Africa 1943", False),
    ("Left 4 Dead", False),
    ("Eisenbahn.exe 6.0 Gold Edition", False),
    ("688i - Hunter Killer", True),
    ("Euro Fishing", False),
])
def test_starts_with_number(starts_with_number_in, starts_with_number_out):
    assert match_feature('starts_with_number', starts_with_number_in) == starts_with_number_out


@pytest.mark.parametrize("contains_vs_in, contains_vs_out", [
    ("Marvel vs Capcom", True),
    ("Marvel versus Capcom", True),
    ("Marvel vs. Capcom", True),
    ("Marvel v Capcom", False),
    ("Marvel Versus Capcom", True),
    ("MARVEL VERSUS CAPCOM", True)
])
def test_contain_versus_vs(contains_vs_in, contains_vs_out):
    assert match_feature('versus_vs', contains_vs_in) == contains_vs_out


@pytest.mark.parametrize("contains_and_in, contains_and_out", [
    ("Black and White", True),
    ("Blackand White", False),
    ("Black AndWhite", False),
    ("Black & White", True),
    ("BLACK AND WHITE", True),
    ("Euro Fishing", False),
])
def test_contain_and(contains_and_in, contains_and_out):
    assert match_feature('and_And_AND', contains_and_in) == contains_and_out


@pytest.mark.parametrize("contains_the_in, contains_the_out", [
    ("SpongeBob SquarePants: Creature from the Krusty Krab", True),
    ("Pitfall: The Lost Expedition", True),
    ("WOLFENSTEIN: THE NEW ORDER", True),
    ("The Last Tinker: City of Colors", True),
    ("Lathe Safety Simulator", False),
    ("Theatre of War 2: Africa 1943", False),

])
def test_contain_the(contains_the_in, contains_the_out):
    assert match_feature('the_The_THE', contains_the_in) == contains_the_out


@pytest.mark.parametrize("colon_or_minus_in, colon_or_minus_out", [
    ("688i - Hunter Killer", True),
    ("Theatre of War 2: Africa 1943", True),
    ("WipeOut 2", False)
])
def test_contain_colon(colon_or_minus_in, colon_or_minus_out):
    assert match_feature('colon_or_minus', colon_or_minus_in) ==  colon_or_minus_out


@pytest.mark.parametrize("directors_cut_in, directors_cut_out", [
    ("WipeOut Director's Cut", True),
    ("WipeOut directorscut", True),
    ("WipeOut Directors cut", True),
    ("WipeOut DIRECTORS CUT", True),
    ("WipeOut Directors Cut", True),
    ("WipeOut Directors CUT", True),
    ("WipeOut 2", False)
])
def test_contain_directorscut(directors_cut_in, directors_cut_out):
    assert match_feature('directors_cut', directors_cut_in) ==  directors_cut_out


@pytest.mark.parametrize("HD_remastered_in, HD_remastered_out", [
    ("LocoRoco: Remastered", True),
    ("FULL THROTTLE: REMASTERED", True),
    ("Rez HD", True),
    ("Superstars V8 Next Challenge", False),
])
def test_contain_remastered(HD_remastered_in, HD_remastered_out):
    assert match_feature('HD_remastered', HD_remastered_in) ==  HD_remastered_out


@pytest.mark.parametrize("editions_in, editions_out", [
    ("Darkspore (Limited Edition)", True),
    ("The Silent Hill Collection", True),
    ("Viva Piñata (Special Edition)", True),
    ("Half-Life: Game of the Year Edition", True),
    ("Battlefield 1942™ World War II Anthology", True),
    ("Elite Forces Unit 77", False),
])
def test_editions(editions_in, editions_out):
    assert match_feature('editions', editions_in) ==  editions_out


@pytest.mark.parametrize("apostrophes_in, apostrophes_out", [
    ("WipeOut Director's Cut", True),
    ("Disney Pixar's Cars", True),
    ("Tom Clancy's Rainbow Six", True),
    ("Let's Create: Pottery", True),
    ("Tony Hawk's Pro Skater 3", True),
    ("Elite Forces Unit 77", False),
])
def test_contain_apostrophes(apostrophes_in, apostrophes_out):
    assert match_feature('apostrophes', apostrophes_in) == apostrophes_out


@pytest.mark.parametrize("famous_patron_in, famous_patron_out", [
    ("WipeOut Director's Cut", False),
    ("Disney Pixar's Cars", True),
    ("Tom Clancy's Rainbow Six", True),
    ("Let's Create: Pottery", False),
    ("Tony Hawk's Pro Skater 3", True),
    ("Sid Meier's: Pirates", True),
    ("Elite Forces Unit 77", False),
])
def test_contain_famous_patron(famous_patron_in, famous_patron_out):
    assert match_feature('famous_patron', famous_patron_in) == famous_patron_out


@pytest.mark.parametrize("contains_a_year_in, contains_a_year_out", [
    ("Theatre of War 2: Africa 1943", False),
    ("Battlefield 1942™ World War II Anthology", False),
    ("Madden NFL 06", True),
    ("WWE 2K16", True),
    ("Elite Forces Unit 77", False),
    ("Valet Parking 1989", True)
])
def test_contain_a_year(contains_a_year_in, contains_a_year_out):
    assert match_feature('contains_a_year', contains_a_year_in) == contains_a_year_out


@pytest.mark.parametrize("number_letter_in, number_letter_out", [
    ("Theatre of War 2: Africa 1943", False),
    ("Superstars V8 Next Challenge", True),
    ("Moto GP2", True),
    ("Elite Forces Unit 77", False),
    ("688i - Hunter Killer", True),
])
def test_contains_number_letter(number_letter_in, number_letter_out):
    assert match_feature('number_letter', number_letter_in) == number_letter_out
