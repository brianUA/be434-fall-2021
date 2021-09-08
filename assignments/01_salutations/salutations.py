#!/usr/bin/env python3
"""
Author : Brian Scott <brianscott@email.arizona.edu>
Date   : 2021-09-08
Purpose: Print a Friendly Greeting
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-g',
                        '--greeting',
                        help='A greeting, defaults to "Howdy"',
                        metavar='str',
                        type=str,
                        default='Howdy')

    parser.add_argument('-n',
                        '--name',
                        help='A name to greet, defaults to "Stranger"',
                        metavar='str',
                        type=str,
                        default='Stranger')
    

    parser.add_argument('-e',
                        '--excited',
                        help='A flag to terminate the greeting with an exclamation point',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    if args.excited == True:
        excited = '!'
    else:
        excited = '.'

    print(args.greeting + ', ' + args.name + excited)



# --------------------------------------------------
if __name__ == '__main__':
    main()
