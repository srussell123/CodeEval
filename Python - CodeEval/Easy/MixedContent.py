__author__ = 'scottrussell'

import sys


def main():
    file = open(sys.argv[1], 'r')
    for line in file.readlines():
        beginList = []
        endList = []
        line = line.rstrip().split(',')
        for place in line:
            if place[0] >= 'a' and place[0] <= 'z':
                beginList.append(place)
            else:
                endList.append(place)
        if len(beginList) > 0:
            if len(endList) > 0:
                print ",".join(beginList) + '|' + ",".join(endList)
            else:
                print ",".join(beginList)
        else:
            print ",".join(endList)
    file.close()


if __name__ == '__main__':
    main()