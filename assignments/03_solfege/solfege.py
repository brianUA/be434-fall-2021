#!/usr/bin/env python3
"""
Author : root <root@localhost>
Date   : 2021-09-22
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='A Program to return lines from Do Re Me from the first syllables',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('syllable',
                        metavar='str',
                        nargs='+',
                        type=str,
                        help='Syllables from Do Re Me')
    return parser.parse_args()


# --------------------------------------------------
def main():
    """The main script to print the proper lines"""
    args = get_args()
    #list of syllables and lines
    syls = ['Do', 'Re', 'Mi', 'Fa', 'Sol', 'La', 'Ti']
    lines = ["Do, A deer, a female deer", "Re, A drop of golden sun", "Mi, A name I call myself", "Fa, A long long way to run", "Sol, A needle pulling thread", "La, A note to follow sol", "Ti, A drink with jam and bread"]

    for i in range(0, len(args.syllable)):
        if args.syllable[i] in syls:
            for x in range(0, len(syls)):
                if syls[x] == args.syllable[i]:
                    print(lines[x])
        else:
            print('I don\'t know ' + "\"" + args.syllable[i] + "\"")
            



# --------------------------------------------------
if __name__ == '__main__':
    main()
