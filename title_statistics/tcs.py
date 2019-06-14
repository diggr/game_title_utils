#!/usr/bin/env python3
"""
This file calculates various feature statistics for a list of game
titles. From the results it can be decided, which features in the titles
are should be considered in a linking process and which are corner cases 
not to be considered.
"""

import json
import click
from re import escape
from os import mkdir
from os.path import isdir, join
from tqdm import tqdm
from title_feature_matchers import PATTERNS, match_feature


OUTPATH = "saved_matches"
OUTEXT = ".json"


TITLE_LIST = "../named_entity_recognition/dict/game_titles.json"


def load_title_list(filepath):
    """
    Loads a list of game titles from a json file
    """
    with open(filepath) as f:
        all_titles = json.load(f)
    return all_titles


def show_feature_matchers(patterns=PATTERNS):
    print("Found Feature Matchers:")
    for pattern in patterns.keys():
        print("\t{0}".format(pattern))


def print_stats(pattern_name, count, n_titles):
    percent = 100*(count/n_titles)
    print("{0}:\t {1}/{2} ({3:.2f}%)".format(pattern_name, count, n_titles, percent))

@click.command()
@click.argument("title_list")
@click.option("--save/--no-save", default=False)
@click.option("--show_features/--no-show_features", default=True)
@click.option("--outpath", "-o", default=OUTPATH)
def generate_stats(title_list,
                show_features,
                save,
                outpath,
                patterns=PATTERNS,                
                outext=OUTEXT):
    if show_features:
        show_feature_matchers()
    all_titles = load_title_list(title_list)
    n_titles = len(all_titles)
    for pattern_name in patterns:
        if save:
            matched_titles = []
        current_count = 0
        for title in tqdm(all_titles):
            if match_feature(pattern_name, title):
                current_count+=1
                if save:
                    matched_titles.append(title)
        print_stats(pattern_name, current_count, n_titles)
        if save:
            if not isdir(outpath):
                mkdir(outpath)
            outfilename = join(outpath, pattern_name+outext)
            with open(outfilename, 'w') as outfile:
                json.dump(matched_titles, outfile, indent=4)


if __name__ == "__main__":
    generate_stats()
