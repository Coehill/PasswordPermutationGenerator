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
minl = -1
maxl = -1


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
    global minl
    global maxl
    
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
            inputName = a
        elif o in ("-o", "--output-name"):
            outputName = a
        elif o in ("-b", "--max-size"):
            maxSize = a
        elif o in ("-m", "--min"):
            minl = int(a)
        elif o in ("-x", "--max"):
            maxl = int(a)
        else:
            print("assert false")
            assert False,"Unhandled Option"
        
    
    # Read contents of input file into a list
    with open(inputName) as f:
        lines = [line.rstrip('\n') for line in open(inputName)]
        
    generate(lines)
    
    formatSize()
    
    print(permutations)
    
        
'''
Given a list of strings, generate permutations of those strings and store
in the global list Permutations.  This method has the permutations residing
in memory, so the size of the wordlist will depend on your hardware.  In
the future, this should be optimized to write directly to an external file
to remove the dependance on physical memory.
'''
def generate(lines):
    global inputName
    global outputName
    global maxSize
    global permutations
    
    if maxSize > 0:
        # work in progress
        print(list(itertools.permutations(lines, maxSize)))
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
def formatSize():
    global permutations
    global minl
    global maxl
    
    tempList = []
    if minl > 0:
        for item in permutations:
            if len(item) >= minl:
                tempList.append(item)
    permutations = tempList
    tempList = []
    if maxl > 0:
        for item in permutations:
            if len(item) <= maxl:
                tempList.append(item)
    permutations = tempList
    
    
        
main()