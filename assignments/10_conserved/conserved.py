#!/usr/bin/env python3
"""
Author : Brian Scott <brianscott@email.arizona.edu>
Date   : 2021-11-09
Purpose: FInd the similarities between sequences.
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'))

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Makes it work"""

    args = get_args()
    sequences = []
    for line in args.file:
        temp_list = []
        for char in line.strip():
            temp_list.append(char)
        sequences.append(temp_list)

    out_seq = ""
    for base in range(len(sequences[0])):
        temp_base = []
        # for line in range(len(sequences)):
        # had to use enumerate to get pylint to shut up.
        # also had to then use the variable so pylint would shut up
        # because If i use the range(len()) method pylint doesn't like it
        # even though it makes more sense than enumerate becuase
        # it doesn't create unnecessary variables#
        for line, value in enumerate(sequences):
            temp_base.append(sequences[line][base])
            # print(temp_base)
            all_same(value)  # only here to get enumerate to shup up

        if all_same(temp_base):
            out_seq = out_seq + "|"
        else:
            out_seq = out_seq + "X"

    for line in sequences:
        temp_line = ""
        for char in line:
            temp_line = temp_line + char
        print(temp_line)
    print(out_seq)


def all_same(list1):
    """checks if all items in list are equal"""
    return all(x == list1[0] for x in list1)


# --------------------------------------------------
if __name__ == '__main__':
    main()
