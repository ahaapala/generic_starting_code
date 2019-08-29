#! /usr/bin/env python

import sys
import traceback
import argparse

def parse_args():

    parser = argparse.ArgumentParser(description='Console App 0.0.1')

    misc = parser.add_argument_group('Misc','Miscellaneous')

    misc.add_argument('-t', '--test', dest='test', action='store_true', help='Run the test block')

    """
    usage examples

    exclusive = parser.add_mutually_exclusive_group()
    exclusive.add_argument('-d', '--dice-pool', dest='d_note', action='store', help='Roll some dice, e.g. 3d12')
    exclusive.add_argument('-s', '--system', dest='system', action='store', help='Specify what ttrpg system to use')
    misc.add_argument('-v', '--verbose', dest='verbose', action='store_true', help='Print debugging information')
    parser.add_argument('--name', default='', dest='name', action='store', help='Name used as an id in various parts of the code')
    parser.add_argument('--notes', default='', dest='notes', action='store', help='Misc notes about what you are trying to do')
    """

    args = parser.parse_args()

    return args

def main(args):

    if args.test:
        results = "Hello, World!"        
    else:
        results = "Not a recognized option or argument"

    print(results)

    return 0

if __name__ == "__main__":
    try:
        args = parse_args()
        main(args)
    except Exception as e:
        print('Script Error:'+str(e))
        traceback.print_exc()
