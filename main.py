#!/usr/bin/env python3

import argparse
import textwrap
import os
import sys

sys.path.insert(0, os.path.abspath("lib"))
from dicts import digits, symbols, characters, leet_dict
from dicts import gen_rand_dict, sublists
from dicts import leet_replace_random
from dicts import leet_replace_random_consonants, leet_replace_random_vowels
from dicts import leet_replace_all
from dicts import leet_replace_all_vowels, leet_replace_all_consonants


def munge_word(word: str, level: int) -> list:
    """Function that takes a word and a level and munges it.

    Different munging levels based on input.

    The original word to be munged will also be found in the output file.
    """

    # Wordlist with case combination & leet speek, that will be app and prep to
    wordlist_process = []
    # Munged wordlist that will be returned by the function
    wordlist_munged = []

    wordlist_case = [word, word.capitalize(), word.casefold(), word.upper(),
                    word.lower(), word.swapcase()]

    wordlist_process.extend(wordlist_case)
    wordlist_munged.extend(wordlist_case)

    for word in wordlist_case:
        i = 0
        while i <= level:
            i += 1
            temp_word = word
            rand_dict = gen_rand_dict(leet_dict)

            leet_repl_all = leet_replace_all(temp_word, rand_dict)
            leet_rand = leet_replace_random(temp_word, leet_dict)
            leet_rand_vow = leet_replace_random_vowels(temp_word, leet_dict)
            leet_rand_cons = leet_replace_random_consonants(temp_word, leet_dict)
            leet_rand_vows_all = leet_replace_all_vowels(temp_word, rand_dict)
            leet_rand_cons_all = leet_replace_all_consonants(temp_word, rand_dict)
            wordlist_process.extend([leet_repl_all,
                                     leet_rand,
                                     leet_rand_vow,
                                     leet_rand_cons,
                                     leet_rand_vows_all,
                                     leet_rand_cons_all])

    wordlist_process = list(set(wordlist_process))
    wordlist_munged.extend(wordlist_process)
    wordlist_munged = list(set(wordlist_munged))

    digits_sublists = sublists(digits)
    symbols_sublists = sublists(symbols)
    character_sublists = sublists(characters)

    # Append and prepend each word in the "wordlist_process"
    for word_app in wordlist_process:
        for sublist in digits_sublists:
            if len(sublist) <= level and level != 9:
                rand_string = "".join(str(elem) for elem in sublist)
                word_temp_prep = rand_string + word_app
                word_temp_app = word_app + rand_string
                wordlist_munged.append(word_temp_prep)
                wordlist_munged.append(word_temp_app)
            if level == 9:
                rand_string = "".join(str(elem) for elem in sublist)
                word_temp_prep = rand_string + word_app
                word_temp_app = word_app + rand_string
                wordlist_munged.append(word_temp_prep)
                wordlist_munged.append(word_temp_app)

        for sublist in symbols_sublists:
            if len(sublist) <= level and level != 9:
                rand_string = "".join(str(elem) for elem in sublist)
                word_temp_prep = rand_string + word_app
                word_temp_app = word_app + rand_string
                wordlist_munged.append(word_temp_prep)
                wordlist_munged.append(word_temp_app)
            if level == 9:
                rand_string = "".join(str(elem) for elem in sublist)
                word_temp_prep = rand_string + word_app
                word_temp_app = word_app + rand_string
                wordlist_munged.append(word_temp_prep)
                wordlist_munged.append(word_temp_app)

        for sublist in character_sublists:
            if len(sublist) <= level and level != 9:
                rand_string = "".join(str(elem) for elem in sublist)
                word_temp_prep = rand_string + word_app
                word_temp_app = word_app + rand_string
                wordlist_munged.append(word_temp_prep)
                wordlist_munged.append(word_temp_app)
            if level == 9:
                rand_string = "".join(str(elem) for elem in sublist)
                word_temp_prep = rand_string + word_app
                word_temp_app = word_app + rand_string
                wordlist_munged.append(word_temp_prep)
                wordlist_munged.append(word_temp_app)

    wordlist_munged = list(set(wordlist_munged))
    return wordlist_munged


def parse_arguments():

    description = ("Script intended to be used in conjunction with other "
                   "password cracking tools\n\n"
                   "NOTE: Resulting wordlists will be very large.")

    parser = argparse.ArgumentParser(prog = "Python3 wordlist munging tool",
                                     formatter_class = argparse.RawDescriptionHelpFormatter,
                                     description = description,
                                     epilog = "L33t_pyth0n")

    parser.add_argument("word",
                        metavar = "word",
                        nargs = "?",
                        help = "Single word to be munged.")
    parser.add_argument("-l", "--level",
                        type = int,
                        default = 5,
                        choices = range(0, 10),
                        help = "Specify level of munge depth (default 5).")
    parser.add_argument("-i", "--input",
                        dest = "input",
                        help = "Input file containing the initial wordlist to be munged.")
    parser.add_argument("-o", "--output",
                        dest = "output",
                        help = "Output file with the final munged wordlist.",
                        required = True)

    args = parser.parse_args()

    return args


def main():

    args = parse_arguments()
    level = args.level

    with open(args.output, "w+") as f_output:
        if args.word:
            word = str(args.word).lower()
            wordlist_munged = munge_word(word, level)
            for i, word in enumerate(wordlist_munged):
                f_output.write(word + "\n")
            print(f"[#] Generated {(len(wordlist_munged))} words.")

        if args.input:
            chunk = 100
            print(f"[#] Opening file: \"{args.input}\" - updates every {chunk} words processed")
            print(f"[#] Press CTRL+C to interrupt at anytime, while retaining partially munged wordlist.")

            with open(args.input, "r") as f_input:
                for i, word in enumerate(f_input):
                    if i % chunk == 0:
                        print(f"[#] Processing word #{i+1}")
                    wordlist_munged = munge_word(word, level)
                    for word_munged in wordlist_munged:
                        f_output.write(word_munged + "\n")
                f_input.close()

        f_output.close()

    print(f"[!] Done. Munged wordlist written to: \"{args.output}\"")


if __name__ == "__main__":
    # Catch CTR+C and exit without error message.
    try:
        main()
    except KeyboardInterrupt:
        print()
        sys.exit(1)
