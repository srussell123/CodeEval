__author__ = 'scottrussell'

import sys


def main():

    numbers = { 'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
                'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

    file = open(sys.argv[1], 'r')
    for line in file.readlines():
        line = line.strip().split(';')
        translation = []
        for x in line:
            translation.append(numbers[x])
        print "".join(translation)

    file.close()


if __name__ == '__main__':
    main()