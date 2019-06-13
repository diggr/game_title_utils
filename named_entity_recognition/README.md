#Video Game Title Named Entity Recognition


## Dictionary

`dict/game_titles.json`

The dictionary contains a list of ~260.000 unique game titles from Mobygames, MediaArt DB and GameFAQs.
Game titles which are single generic English terms (e.g. "Inside", "Kingdom") were filtered out.


## Trained Model

`model`

A video game title named entity recognition model trained on game related Wikipedia articles using spacy.


### Process


## Game title matcher

Helper classes for applying dictionary or model based video game title NER.

### Usage