__author__ = 'scottrussell'

import sys


def main():
    file = open(sys.argv[1], 'r')
    for line in file.readlines():
        line = line.strip()
        print 22 % 26

    file.close()


if __name__ == '__main__':
    main()