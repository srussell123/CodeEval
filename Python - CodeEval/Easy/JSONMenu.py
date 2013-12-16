__author__ = 'scottrussell'

import sys
import re


def main():
    file = open(sys.argv[1], 'r')
    for line in file.readlines():
        line = line.strip()
        if line == '':
            pass
        else:
            sum = 0
            label = [m.strip('Label ') for m in list(re.findall('\Label(.*?)\"', line))]
            for x in label:
                sum += int(x)
            print sum
    file.close()


if __name__ == '__main__':
    main()