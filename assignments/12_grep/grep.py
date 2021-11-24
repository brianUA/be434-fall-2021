#!/usr/bin/env python3
"""
Author : root <brianscott@email.arizona.edu>
Date   : 2021-11-22
Purpose: Search for files
"""

import argparse
import sys
import os
import re

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

   

    parser.add_argument('-i',
                        '--insensitive',
                        help='Case-insensivitive search (default: false)',
                        action='store_false')

    parser.add_argument('-o',
                        '--outfile',
                        help='specificy output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    parser.add_argument('pattern',
                        metavar='str',
                        help='Search pattern')

    parser.add_argument('files',
                        help='Input file(s)',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('rt'))



    return parser.parse_args()


# --------------------------------------------------
def main():
    args = get_args()
    search(args.pattern, args.files, args.insensitive, args.outfile)

def search(pattern, files, sensitive, outfile):

    for fh in files:
        if len(files) > 1:
            print(os.path.basename(fh.name), file=outfile)
        for line in fh:
            if sensitive:
                if re.search(pattern, line):
                    print(line.strip(), file=outfile)
            else:
                if re.search(pattern, line, re.I):
                    print(line.strip(), file=outfile)

# --------------------------------------------------
if __name__ == '__main__':
    main()
