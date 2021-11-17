#!/usr/bin/env python3
"""
Author : Brian Scott <brianscott@email.arizona.edu>
Date   : 2021-11-15
Purpose: Create the 
"""

import argparse
import os

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='text', help='Input text or file')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    tempseq = "x"    
    newseq = ""
    line = args.text
    for value, base in enumerate(line):
        if value == len(line) -1 and base == line[len(line)-1]:
            if base == tempseq[0]:
                newseq = newseq +str(len(tempseq)+1)
        if base == tempseq[0]:
            tempseq = tempseq + base
        else:
            count = len(tempseq)
            tempseq = base
            if count > 1:
                newseq = newseq + str(count) + tempseq[0] 
            elif base == line[len(line)-1] and count > 1:
                    newseq = newseq + base + str(count)
            else:
                newseq = newseq + base
    print(newseq)

            




# --------------------------------------------------
if __name__ == '__main__':
    main()