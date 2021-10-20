#!/usr/bin/env python3
"""
Author : Brian Scott <brianscott@email.arizona.edu>
Date   : 2021-10-18
Purpose: Translates IUPAC codes
"""

import argparse
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('SEQ',
                        metavar='str',
                        help='Sequences to translate',
                        nargs='+',
                        type=str)

    parser.add_argument('-o',
                        '--outfile',
                        help='specificy output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    codes = {
            "R": "AG",
            "Y": "CT",
            "S": "GC",
            "W": "AT",
            "K": "GT",
            "M": "AC",
            "B": "CGT",
            "D": "AGT",
            "H": "ACT",
            "V": "ACG",
            "N": "ACGT"
            }

    for sequences in args.SEQ:
        edited = ""
        for letter in sequences:
            if letter in codes:
                edited = edited + "[" + codes.get(letter) + "]"
            else:
                edited = edited + letter


        print(sequences, edited, file=args.outfile)

    if args.outfile is not sys.stdout:
        print("Done, see output in \"" + str(args.outfile.name) + "\"")

# --------------------------------------------------
if __name__ == '__main__':
    main()
