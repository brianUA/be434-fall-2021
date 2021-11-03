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

    parser.add_argument('file',
                        help='Input file(s)',
                        metavar='FILE',
                        nargs='+',
                        type=argparse.FileType('rt'))

    parser.add_argument('-o',
                        '--outdir',
                        help='specificy output directory',
                        metavar='str',
                        default="split")

    return parser.parse_args()


# --------------------------------------------------
def main():
    args = get_args()
    makedir(args)

    outfiles = args.file
    for files in outfiles:
        file = files.name
        basename = os.path.basename(file)
        root, ext = os.path.splitext(basename)
        outname1 = os.path.join(args.outdir, root + '_1' + ext)
        outname2 = os.path.join(args.outdir, root + '_2' + ext)


        reader = SeqIO.parse(files, 'fasta')


        with open(outname1, 'w') as f:
            sys.stdout = f
            for rec in reader:
                line =+ 1
                if (line % 2) != 0:
                    print(rec.description)
                    print(rec.seq)


        with open(outname2, 'w') as f:
            sys.stdout = f
            for rec in reader:
                line =+ 1
                if (line % 2) == 0:
                    print(rec.description)
                    print(rec.seq)

    



def makedir(args):
    directory = args.outdir
    if not os.path.exists(directory):
        os.makedirs(directory)
    print(f"Done, see output in \"{directory}\"")

def split(args):
    print()

    
def out(args):
    #outfiles = args.file
    #outnames = []
    #for files in outfiles:
    #    counter = 1
    #    namelist = []
    #    for char in files.name:
    #        namelist.append(char)
    #    del namelist[0:namelist.index("/")+1]
    #    namelist2 = []
    #    for entry in namelist:
    #        namelist2.append(entry)
    #    namelist.insert(namelist.index("."), "_" + str(counter))
    #    outnames.append("".join(namelist))
    #    counter += 1
    #    namelist2.insert(namelist2.index("."), "_" + str(counter))
    #    outnames.append("".join(namelist2))
    #print(outnames)
    teststr = "This is a test"



# --------------------------------------------------
if __name__ == '__main__':
    main()
