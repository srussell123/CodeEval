__author__ = 'scottrussell'

import sys


def main():
    file = open(sys.argv[1], 'r')
    for line in file.readlines():
        line = map(int, (line.rsplit()))
        lowest = 10 #9 is the highest possible number
        for x in line:
            if line.count(x) == 1:
                if x < lowest:
                    lowest = x
        if lowest == 10:  #there are no unique numbers
            print 0
        else:
            print 1 + line.index(lowest) #print the location of the unique number (1-based, not 0-based index)
    file.close()


if __name__ == '__main__':
    main()