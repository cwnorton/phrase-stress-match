#!/usr/bin/env python3

"""
phrase_stress_match.py
By Chris Norton, 2017

Matches user-input phrase to phrases from an external newline-separated file of
phrases, based on stress patterns from nltk.corpus.cmudict.

Very rough-and-ready, designed originally to 'meter-match' people's names to pop
songs - but it works slightly better for phrases rather than names.  Slightly.

If external file is tab-delimited, only the first column will be used to match,
but all columns will be displayed when there is a match.

Usage: phrase_stress_match.py [-h] [-l PHRASE_LIST] [phrase]

no arguments: interactive mode

positional arguments:
  phrase                phrase to match to phrase from list, in quotes

optional arguments:
  -h, --help            show help message and exit
  -l PHRASE_LIST, --phrase-list PHRASE_LIST
                        path to newline-separated list of phrases

"""

import argparse
import pathlib
import re
from nltk.corpus import cmudict

DEFAULT_INPUT_PATH = 'uk_number_ones.txt'
STRESS_DICT = cmudict.dict()

def handle_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('phrase', nargs = '?',
            help = 'phrase to match to phrase from list, in quotes')
    parser.add_argument("-l", "--phrase-list", type = str,
            help = 'path to newline-separated list of phrases',
            default = DEFAULT_INPUT_PATH)
    parsed_args = parser.parse_args()
    return parsed_args

def clean_string(string):
    # Return `string` lowercased & with non-alphanumeric characters removed.

    string = re.sub(r'[^\w .]', '', string.lower())
    return string

def get_stress_pattern(word):
    # Return a string representing the stress pattern of `word`.

    try:
        stress_pattern = [list(y[2] for y in word if y[-1].isdigit())
                for word in STRESS_DICT[word.lower()]]
    except:
        return None
    else:
        return str(('').join(stress_pattern[0]))

def get_phrase_stress_pattern(phrase):
    # Return a space-separated string for the stress patterns of each word in
    # `phrase`.

    phrase = clean_string(phrase)
    phrase_stress_pattern = []
    for word in phrase.split(' '):
        word_stress_pattern = get_stress_pattern(word)
        if word_stress_pattern is not None:
            phrase_stress_pattern.append(word_stress_pattern)
        else:
            return None

    return str(''.join(phrase_stress_pattern))

def tag_list(input_list):
    # Return a dictionary of stress patterns, with each stress pattern
    # containing a list of phrases that have that pattern.

    tagged_list = {}
    for phrase in input_list:
        original_phrase = phrase
        # If this a tabbed file, only take phrase from first column.
        if phrase.find('\t') > -1:
            phrase = phrase[0:phrase.find('\t')]
        stress_pattern = get_phrase_stress_pattern(phrase)
        if stress_pattern is not None :
            if stress_pattern in tagged_list.keys():
                tagged_list[stress_pattern].append(original_phrase)
            else:
                tagged_list[stress_pattern] = [original_phrase]

    return tagged_list

def get_matches(input_phrase, phrases):
    # Display list of phrases that match the input.

    stress = get_phrase_stress_pattern(input_phrase)
    if stress in phrases.keys():
        return('\n'.join(phrases[stress]))
    else:
        return('No matches found :(')

def main():

    args = handle_arguments()
    if args.phrase is None:
        interactive_mode = True
    else:
        interactive_mode = False

    if args.phrase_list != DEFAULT_INPUT_PATH:
        path = pathlib.Path(args.phrase_list)
        if not path.exists():
            print('Error: Phrase list file {0} not found.'.format(
                args.phrase_list))
            return

    # Read in external list of phrases and create a stress pattern dictionary
    # from them.
    phrases = [phrase.strip() for phrase
            in open(args.phrase_list, 'r').readlines()]
    phrases = tag_list(phrases)

    if interactive_mode:

        while True:

            # Get user input.
            try:
                input_phrase = input('\nEnter a phrase (x to exit): ')
            except KeyboardInterrupt:
                return
            if input_phrase == 'x': return

            # If user input phrase has same stress pattern as anything in the
            # external list of phrases, display all matches.
            print(get_matches(input_phrase, phrases))
    else:
        print(get_matches(args.phrase, phrases))

if __name__ == '__main__':
    main()
