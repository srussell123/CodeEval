__author__ = 'scottrussell'

import sys

def testRepetition(place, line):
    period = len(line) / place
    if (line[0: place] * period) == line:
        print place
        return True

def main():
    file = open(sys.argv[1], 'r')
    for line in file.readlines():
        line = line.strip()
        place = 1
        finished = False
        length = len(line)
        while finished is not True:
            if len(line) % place == 0:
                finished = testRepetition(place, line)
            place += 1
    file.close()


if __name__ == '__main__':
    main()