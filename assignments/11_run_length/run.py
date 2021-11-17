#!/usr/bin/env python3
"""
Author : Brian Scott <brianscott@email.arizona.edu>
Date   : 2021-11-15
Purpose: Create the 
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('seq',
                        metavar='str',
                        help='A positional argument')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    tempseq = "x"
    newseq = ""
    outseq = ""
    

    for line in args.seq:
        for value, base in enumerate(line):
            if base == tempseq[0]:
                tempseq = tempseq + base
            elif base != tempseq[0] or (base == tempseq[0] and value == len(line)):
                count = len(tempseq)
                tempseq = base
                if count > 1:
                    newseq = newseq + str(count) + tempseq[0] 
                elif base == line[len(line)-1]:
                    print("base:", base, "line", line)
                    newseq = newseq + base + str(count)
                else:
                    newseq = newseq + base
        print(newseq)

            




# --------------------------------------------------
if __name__ == '__main__':
    main()
