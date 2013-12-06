__author__ = 'scottrussell'

import sys


def main():
    file = open(sys.argv[1], 'r')
    for line in file.readlines():
        line = line.split()
        longest = line[0]
        for word in line:
            if len(longest) < len(word):
                longest = word
        print longest
    file.close()


if __name__ == '__main__':
    main()