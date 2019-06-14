# Game Title Feature Statistics

Generate statistics of common video game title features in a list of game titles.

## Usage

Provide a list of game titles (a list of strings) in Json format as an argument.

```zsh
$ python tcs.py ../dataset/game_titles.json 
```

### Parameters

| Parameter | Description | Default |
| --- | --- |--- |
| `--show_features/--no-show_features` | display all implemented featuers at the beginning. | `--show_feature` |
| `--save/--no-save` | save a list of matched title for each feature | `--no-save` |
| `--outpath` `-o` | define the output path for the `save` parameter | `saved_matches` |

## Implemented features

* Contains one number
* Contains two numbers
* Starts with a number
* Contains 'versus' / 'vs'
* Contains 'and'
* Contains 'The'
* Contains colon or minus
* Contains 'Directors Cut'
* Contains 'HD remastered'
* Contains 'Edition'
* Contains apostrophes
* Contains famous name or trademark (e.g. "Disney's ...")
* Contains year
* Contains words with digits (e.g. "V8", "3D")

The regular expressions for these features can be found in `title_feature_matchers.py`