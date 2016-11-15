#!/usr/bin/python

import sys
import os
import getopt
import string
import itertools
import argparse

__version__ = '0.0.1'

# global variables
permutations = []
CONST_MAX = 99999999999999


def usage():
    print("Password Permutation Generator\n")
    print("Usage: ppg.py <min-len> <max-len> [FILE]\n")
    print("-i --input-name wordlist.txt\n     Specifies the file to read the input from, eg: wordlist.txt\n")
    print("-o --output-name wordlist.txt\n     Specifies the file to write the output to, eg: wordlist.txt\n")
    print("-b number[type]\n     Specifies  the  size  of  the  output file, only works if -o START is used, i.e.: 60MB  The " + 
          "output files will be in the format of starting letter-ending letter or example: ./crunch 4 5 -b 20mib -o START " +
          "will generate 4 files: aaaa-gvfed.txt, gvfee-ombqy.txt, ombqz-wcydt.txt, wcydu-zzzzz.txt valid values for type " +
          "are kb, mb, gb, kib, mib, and gib.  The first three types are based on 1000 while the last three types are " +
          "based  on  1024.  NOTE There is no space between the number and type.  For example 500mb is correct 500 mb " +
          "is NOT correct.\n")
    sys.exit(0)
    
    
def run(input_file, output_file, max_length, min_length, max_filesize):
    global permutations
    global CONST_MAX
    
    max_length = max_length
    min_length = min_length
    max_filesize = max_filesize
    
    # Read contents of input file into a list
    with open(input_file) as f:
        lines = [line.rstrip('\n') for line in open(input_file)]
        
    generate(lines, max_filesize)
    
    formatSize(min_length, max_length)
    
    print(permutations)
    
    sys.exit(0)
    
    
def commandline():
    global CONST_MAX

    parser = argparse.ArgumentParser(
            description='Python script that generates possible password permutations\n'\
                    'from a given list of words.',
            epilog="""    Example:
    markdown-toclify.py ~/Desktop/input.md -o ~/Desktop/output.md
    Updates for this script will be available at
    https://github.com/DistantParadox/PasswordPermutationGenerator
    """,
            formatter_class=argparse.RawTextHelpFormatter
    )

    parser.add_argument('InputFile',
                        metavar='input.lst',
                        help='path to the input file')
    parser.add_argument('-o', '--output',
                        metavar='output.lst',
                        default='output.lst',
                        nargs=1,
                        type=str,
                        help='path to the output file')
    parser.add_argument('-n', '--min',
                        default=0,
                        type=int,
                        metavar='min', choices=range(0,CONST_MAX),
                        help='specify a minimum password length.')
    parser.add_argument('-m', '--max',
                        default=CONST_MAX,
                        type=int,
                        metavar='max', choices=range(0,CONST_MAX),
                        help='specify a maximum password length.')
    parser.add_argument('-b', '--max_size',
                        metavar='max_size', type=float, nargs=1,
                        default = -1,
                        help='specify a maximum output filesize.')
    parser.add_argument('-v', '--version',
                        action='version',
                        version='%s' % __version__)

    args = parser.parse_args()

    '''if args.exclude_h:
        exclude_h = [int(i) for i in args.exclude_h.split(',')]
    else:
        exclude_h = None'''

    cont = run(input_file=args.InputFile,
                            output_file=args.output,
                            max_length=args.max,
                            min_length=args.min,
                            max_filesize=args.max_size)

    if not args.output:
        print(cont)
    
    
    
    #-----------------------------------------
    '''
    if not len(sys.argv[1:]):
        usage()
        
    # read the command line options
    try:
        # if one of the options requires an arg, then it's followed by a colon
        opts, args = getopt.getopt(sys.argv[1:],"hi:o:b:m:x:",
                                   ["help","input-name=", "output-name=", "max-size=", "min=", "max="])
    except getopt.GetoptError as err:
        print(str(err))
        usage()
        
    for o,a in opts:
        if o in ("-h", "--help"):
            usage()
        elif o in ("-i", "--input-name"):
            input_file = a
        elif o in ("-o", "--output-name"):
            output_file = a
        elif o in ("-b", "--max-size"):
            max_filesize = a
        elif o in ("-m", "--min"):
            min_length = int(a)
        elif o in ("-x", "--max"):
            max_length = int(a)
        else:
            print("assert false")
            assert False,"Unhandled Option"
        
    
    # Read contents of input file into a list
    with open(input_file) as f:
        lines = [line.rstrip('\n') for line in open(input_file)]
        
    generate(lines)
    
    formatSize()
    
    print(permutations)'''
    
        
'''
Given a list of strings, generate permutations of those strings and store
in the global list Permutations.  This method has the permutations residing
in memory, so the size of the wordlist will depend on your hardware.  In
the future, this should be optimized to write directly to an external file
to remove the dependance on physical memory.
'''
def generate(lines, max_filesize):
    global permutations
    global CONST_MAX
    
    if max_filesize != -1:
        # work in progress
        print(list(itertools.permutations(lines, max_filesize)))
    else:
        # create permutations
        tempList = list(itertools.permutations(lines))
        
        # convert permutation tuples into strings
        for tuple in tempList:
            a = ""
            for tupleItem in tuple:
                a = a + tupleItem
            permutations.append(a)
            
        # print(permutations)
        

'''
Using the global permutations list, remove necessary items to conform to the
size restrictions in min and max
'''
def formatSize(min_length, max_length):
    global permutations
    
    tempList = []
    if min_length > 0:
        for item in permutations:
            if len(item) >= min_length:
                tempList.append(item)
        permutations = tempList
        tempList = []
            
    if max_length > 0:
        for item in permutations:
            if len(item) <= max_length:
                tempList.append(item)
        permutations = tempList
    
    
if __name__ == '__main__':
    commandline()