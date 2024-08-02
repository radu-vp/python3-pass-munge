"""Mostly leet helper functions and variables.

This file contains some helper functions used to simplify the logic of the script.
"""

import itertools
import random


digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = [" ", "`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")",
           "-", "_", "=", "+", ",", "<", ".", ">", "/", "?", ";", ":", "'",
           "\"", "[", "{", "]", "}"]
characters = digits + symbols
leet_dict = {"a": ["a", "4", "@",  "^", "λ", "∂", "Д"],
            "b": ["b", "8", "ß", "18"],
            "c": ["c", "(", "<", "[", "{", "k", "©", "¢", "€"],
            "d": ["d", "0", "Ð", "∂", "ð"],
            "e": ["e", "3", "&", "€", "ə", "£"],
            "f": ["f", "ph", "ʃ", "ph"],
            "g": ["g", "6", "9", "&", "[", "-"],
            "h": ["h", "#",  "╫"],
            "i": ["i", "!", "1", "|", "l"],
            "j": ["j", "_|", "¿", "ʝ"],
            "k": ["k", "x", "ɮ"],
            "l": ["l", "1", "7", "£", "¬"],
            "m": ["m", "/\/\\", "|\\/|", "em", "|v|", "[v]"],
            "n": ["n", "|\\|", "/\\/",  "~", "₪", "/|/"],
            "o": ["o", "0", "()", "oh", "[]", "{}", "¤", "Ω", "ω", "*",],
            "p": ["p", "?", "9", "q", "℗", "þ", "¶"],
            "q": ["q",  "0,", "o,", "9", "¶"],
            "r": ["r", "2", "®", "Я", "ʁ"],
            "s": ["s", "5", "$", "z", "2", "§", "š"],
            "t": ["t", "7", "+", "1", "†"],
            "u": ["u", "m", "µ"],
            "v": ["v", "\\/", "√"],
            "w": ["w", "\\/\\/", "vv", "uu", "Ш", "ɰ"],
            "x": ["x", "%", "x", "*","Ж", "×"],
            "y": ["y", "j", "Ψ", "φ", "λ", "Ч", "¥"],
            "z": ["z", "2", "~/_", "%", "7_", "ʒ", "≥", "`/_"]}


def sublists(lst: list) -> list:
    """Function that returns all the sublists from a given list."""

    return [lst[i:j] for i in range(len(lst)) for j in range(i + 1, len(lst) + 1)]


def gen_rand_dict(input_dict: dict) -> dict:
    """Function that returns a randomised dictionary from an input dictionary.

    Given an input dictionary where each key has multiple values, generate
    and return a dictionary that has one random value per key chosen from the
    original dictionary.

    Ex.:
    Input: {k0: [v0, v1], k1: [v0, v1], k2: [v0, v1, v2]}
    Output: {k0: v1, k1: v0, k2: v2}
    """

    dict_random = {}
    for key in input_dict:
        val = random.choice(list(input_dict[key]))
        dict_random.update({key: val})

    return dict_random


def leet_replace_random(word: str, dictionary: dict) -> str:
    """Replace random characters with leet

    Intended to be used with dictionary with multiple values per key, will extract a random value per key.
    """

    word_leet = ""
    for char in word:
        # 70% chance that each character will be translated
        if char.lower() in dictionary and random.random() <= 0.70:
            possible_replacements = dictionary[char.lower()]
            leet_substitute = random.choice(possible_replacements)
            word_leet = word_leet + leet_substitute
        # Use original character
        else:
            word_leet = word_leet + char
    return word_leet


def leet_replace_random_vowels(word: str, dictionary: dict) -> str:

    word_leet = ""
    vowels = "aeiou"

    for char in word:
        # 70% chance for each vowel to be leetified
        if any(vowel == char.lower() for vowel in vowels) and char in dictionary and random.random() <= 0.70:
            possible_replacements = dictionary[char.lower()]
            leet_substitute = random.choice(possible_replacements)
            word_leet = word_leet + leet_substitute
        # Use original vowel
        else:
            word_leet = word_leet + char

    return word_leet


def leet_replace_random_consonants(word: str, dictionary: dict) -> str:

    word_leet = ""
    consonants = "bcdfghjklmnpqrstvwxyz"

    for char in word:
      # 70% chance for a consonant to be leetified
        if any(cons == char.lower() for cons in consonants) and char in dictionary and random.random() <= 0.70:
            possible_replacements = dictionary[char.lower()]
            leet_substitute = random.choice(possible_replacements)
            word_leet = word_leet + leet_substitute
        # Use original consonant
        else:
            word_leet = word_leet + char
    return word_leet


def leet_replace_all_vowels(word: str, dictionary: dict) -> str:
    word_leet = word
    vowels = "aeiou"
    for char in word:
        for vowel in vowels:
            if char.lower() == vowel:
                word_leet = word_leet.replace(char, dictionary[vowel])
    return word_leet


def leet_replace_all_consonants(word: str, dictionary: dict) -> str:
    word_leet = word
    consonants = "bcdfghjklmnpqrstvwxyz"
    for char in word:
        for cons in consonants:
            if char.lower() == cons:
                word_leet = word_leet.replace(char, dictionary[cons])
    return word_leet


def leet_replace_all(word: str, dictionary: dict) -> str:
    """Replace all chars from a word if char in dict and has value.

    Given a dictionary, replace all occurances of the dictionary keys in a
    word with the values of said keys.

    Example usage with generated random dict
    """

    word_leet = word
    for i, j in dictionary.items():
        word_leet = word.replace(i, j)
    return word_leet
