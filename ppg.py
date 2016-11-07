#!/usr/bin/python

import sys
import os
import getopt
import string
import itertools

# global variables
inputName = "intput.lst"
outputName = "output.lst"
maxSize = -1
permutations = []


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
    
def main():
    global inputName
    global outputName
    global maxSize
    global permutations
    
    if not len(sys.argv[1:]):
        usage()
        
    # read the command line options
    try:
        opts, args = getopt.getopt(sys.argv[1:],"h:i:o:b",
                                   ["help","input-name", "output-name", "max-size"])
    except getopt.GetoptError as err:
        print(str(err))
        usage()
        
    for o,a in opts:
        print(a)
        if o in ("-h", "--help"):
            usage()
        elif o in ("-i", "--input-name"):
            inputName = a
        elif o in ("-o", "--output-name"):
            outputName = a
        elif o in ("-b", "--max-size"):
            maxSize = a
        else:
            print("assert false")
            assert False,"Unhandled Option"
        
    
    # Read contents of input file into a list
    with open(inputName) as f:
        lines = [line.rstrip('\n') for line in open(inputName)]
        
    generate(lines)
    
        
def generate(lines):
    global inputName
    global outputName
    global maxSize
    global permutations
    
    if maxSize > 0:
        # work in progress
        print(list(itertools.permutations(lines, maxSize)))
    else:
        permutations = list(itertools.permutations(lines))
        print(permutations)
    
    
    
        
main()