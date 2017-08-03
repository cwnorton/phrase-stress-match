# Phrase Stress Match

Matches user-input phrase to phrases from an external newline-separated file of phrases, based on stress patterns from nltk.corpus.cmudict.

Very rough-and-ready, designed originally to 'meter-match' people's names to pop songs - but it works slightly better for phrases rather than names.  Slightly.

If external file is tab-delimited, only the first column will be used to match, but all columns will be displayed when there is a match.

    Usage: phrase_stress_match.py [-h] [-l PHRASE_LIST] [phrase]
    
    no arguments: interactive mode
    
    positional arguments:
      phrase                phrase to match to phrase from list, in quotes

    optional arguments:
      -h, --help            show help message and exit
      -l PHRASE_LIST, --phrase-list PHRASE_LIST
                            path to newline-separated list of phrases
