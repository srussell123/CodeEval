__author__ = 'scottrussell'

import sys


def main():
    file = open(sys.argv[1], 'r')
    for line in file.readlines():
        line = line.split()
        listOne = []
        listTwo = []
        for x in line[0:line.index('|')]:
            listOne.append(int(x))
        for x in line[line.index('|')+1:]:
            listTwo.append(int(x))
        line = [x*y for x,y in zip(listOne, listTwo)]
        for x in line:
            print x,
        print
    file.close()


if __name__ == '__main__':
    main()