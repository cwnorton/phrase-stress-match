# Phrase Stress Match

Matches a user-input English phrase with phrases from an external list, based on stress patterns.  Stress is taken from the cmudict corpus in nltk (http://www.nltk.org/_modules/nltk/corpus/reader/cmudict.html).

A silly thing put together in procrastination time.  Originally designed to match people’s names with pop songs, but it works a little better with phrases.

`Usage: phrase_stress_match.py [-h] [-l PHRASE_LIST] [phrase]

no arguments: interactive mode

positional arguments:
  phrase                phrase to match to phrase from list, in quotes

optional arguments:
  -h, --help            show help message and exit
  -l PHRASE_LIST, --phrase-list PHRASE_LIST
                        path to newline-separated list of phrases`
