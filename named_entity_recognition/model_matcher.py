import spacy

TEXT = "Developed by From Software, Dark Souls 2 is a sequel to the critically acclaimed Dark Souls, an action RPG with estimated sales of over 1.5 million units. The original game's appeal lay with its renowned difficulty and trial-and-error approach, one that Dark Souls 2 promises to sustain. "

TITLE_MODEL = "model"


class TitleModelMatcher(object):

    nlp = spacy.load(TITLE_MODEL)

    def TitleModelMatcher(self):
        pass

    def __call__(self, text):
        doc = self.nlp(text)
    
        ents = [ (ent.text, ent.start_char, ent.end_char, ent.label_) for ent in doc.ents if ent.label_ not in ["CARDINAL"] ]
        return ents


def test(text=TEXT):
    print(text)
    print("---")
    matcher = TitleModelMatcher()
    titles = matcher(text)
    print(titles)

if __name__ == "__main__":
    test()