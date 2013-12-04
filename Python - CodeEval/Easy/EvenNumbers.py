__author__ = 'scottrussell'

import sys

def main():
    file = open(sys.argv[1], 'r')
    for line in file.readlines():
        line = int(line)
        if line % 2 == 0:
            print 1
        else:
            print 0
    file.close()


if __name__ == '__main__':
    main()