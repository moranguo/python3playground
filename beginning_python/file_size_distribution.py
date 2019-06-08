#! /usr/bin/python

import os, sys
from stat import *

size_distribution = {
    '0-1K': 0,
    '1K-10K': 0,
    '10K-100K': 0,
    '100K-300K': 0,
    '300K-500K': 0,
    '500K-1M': 0,
    '1M-4M': 0,
    '4M-100M': 0
}

def walktree(top, callback):
    '''recursively descend the directory tree rooted at top,
       calling the callback function for each regular file'''

    for f in os.listdir(top):
        pathname = os.path.join(top, f)
        mode = os.stat(pathname).st_mode
        if S_ISDIR(mode):
            # It's a directory, recurse into it
            walktree(pathname, callback)
        elif S_ISREG(mode):
            # It's a file, call the callback function
            callback(pathname)
        else:
            # Unknown file type, print a message
            print('Skipping %s' % pathname)

def visitfile(file):
    file_size = os.stat(file).st_size
    if(file_size < 1000):
        size_distribution['0-1K'] += 1
    elif(file_size < 10000):
        size_distribution['1K-10K'] += 1
    elif(file_size < 100000):
        size_distribution['10K-100K'] += 1
    elif (file_size < 300000):
        size_distribution['100K-300K'] += 1
    elif (file_size < 500000):
        size_distribution['300K-500K'] += 1
    elif (file_size < 1000000):
        size_distribution['500K-1M'] += 1
    elif (file_size < 4000000):
        size_distribution['1M-4M'] += 1
    elif (file_size < 100000000):
        size_distribution['4M-100M'] += 1
    else:
        print(file, 'exceed max size!')


    #print('visiting', file)

if __name__ == '__main__':
    walktree(sys.argv[1], visitfile)
    print(size_distribution)