# P@ssw0rd_mvng3_T001

## Description

Given either a word as an argument or a wordlist in the form of a `.txt` file,
where each word is present on a new line, generate a munged password list.

This is intended to supplement (not replace) existing rule-based password
cracking tools or wordlist generation tools, by significantly expanding
wordlists. Alternatively, it can generate huge wordlists given a few partial
or complete passwords that may have been re-used with some small changes.

**WARNING: Resulting wordlists will be very large.**

## Requirements

* Python 3.11 or above

## Usage

Munge a single word into a wordlist.

```bash
$ python main.py [WORD] -l [LEVEL_INT] -o [OUTPUT_FILE.TXT]
$ python main.py hacker -l 9 -o mangled.txt
```

Munge a wordlist into a bigger wordlist.

```bash
$ python main.py -i [INPUT_FILE.TXT] -l [LEVEL_INT] -o [OUTPUT_FILE.TXT]
$ python main.py -i mywords.txt -l 9 -o mangled.txt
```

## Help

```bash
$ python main.py --help
usage: Python3 wordlist munging tool [-h] [-l {0,1,2,3,4,5,6,7,8,9}] [-i INPUT] -o OUTPUT [word]

Script intended to be used in conjunction with other password cracking tools

NOTE: Resulting wordlists will be very large.

positional arguments:
  word                  Single word to be munged.

options:
  -h, --help            show this help message and exit
  -l {0,1,2,3,4,5,6,7,8,9}, --level {0,1,2,3,4,5,6,7,8,9}
                        Specify level of munge depth (default 5).
  -i INPUT, --input INPUT
                        Input file containing the initial wordlist to be munged.
  -o OUTPUT, --output OUTPUT
                        Output file with the final munged wordlist.

L33t_pyth0n
```
