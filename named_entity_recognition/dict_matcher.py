import json
import string
import re

TITLE_DICT = "dict/game_titles.json"

TEXT = """
Spyro: year of the dragon Spyro Reignited Trilogy is coming to PlayStation 4 
and Xbox One on Sept. 21, Activision announced today. The collection will include 
the first three games in the series (Spyro the Dragon, Spyro 2: Ripto’s Rage, Spyro: Year of the Dragon) 
in remastered form. Those three games were original developed by Insomniac Games, which has since moved on to 
Ratchet and Clank and is developing this year’s Spider-Man for PS4."""


class TitleDictMatcher(object):

    def __init__(self):
        self.found_titles = []
        with open(TITLE_DICT) as f:
            self.game_titles = json.load(f)

    def _contains(self, title):
        for found_title in self.found_titles:
            if title in found_title and title != found_title:
                return True
        return False

    def __call__(self, text):
        self.found_titles = []
        for title in sorted(self.game_titles, key=lambda x: -len(x)):

            l_text = text.lower()
            l_title = title.lower()

            start_index = l_text.find(l_title)
            while start_index >= 0:

                if start_index == 0:
                    prior_char = " "
                else:
                    prior_char = l_text[start_index-1]

                end_index = start_index+len(l_title)-1
                if end_index == len(l_text)-1:
                    after_char = " "
                else:
                    after_char = l_text[end_index+1]

                if prior_char in string.punctuation+" " and after_char in string.punctuation+" ":

                    if not self._contains(title):
                        yield(title, start_index, end_index)
                        self.found_titles.append(title)

                start_index = l_text.find(l_title, end_index+1)        


def test(text=TEXT):
    matcher = TitleDictMatcher()

    for game, start, end in matcher(text):
        print(game, start, end)

    

if __name__ == "__main__":
    test()