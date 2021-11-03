#!/usr/bin/env python3
"""
Author : brian scott <brianscott@email.arizona.edu>
Date   : 2021-11-01
Purpose: Rock the Casbah
"""

import argparse
from Bio import SeqIO
import os
import sys
# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='SPlit interleaved/paired reads',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('files',
                        help='Input file(s)',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('rt'))

    parser.add_argument('-o',
                        '--outdir',
                        help='specificy output directory',
                        metavar=str,
                        default="split")

    return parser.parse_args()


# --------------------------------------------------
def main():
    args = get_args()

    out_dir = args.outdir
    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)
    

    for fh in args.files:
        basename = os.path.basename(fh.name)
        root, ext = os.path.splitext(basename)
        forward = open(os.path.join(out_dir, root + '_1' + ext), 'wt')
        reverse = open(os.path.join(out_dir, root + '_2' + ext), 'wt')
        parser = SeqIO.parse(fh, 'fasta')

        for i, rec in enumerate(parser):
            SeqUI.write(rec, forward if i % 2 == 0 else reverse, 'fasta')

    print(f'Done, see output in "{out_dir}"')
# --------------------------------------------------
if __name__ == '__main__':
    main()
