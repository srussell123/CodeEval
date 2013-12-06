__author__ = 'scottrussell'

import sys


def main():

    tenStep = ['I', 'X', 'C', 'M'] #1, 10, 100, 1000
    fiveStep = ['V', 'L', 'D']     #5, 50, 500


    file = open(sys.argv[1], 'r')
    for line in file.readlines():
        line = line.rstrip()
        place = len(line) - 1
        roman = []
        for digit in line:
            if digit == '4':
                roman.extend(tenStep[place] + fiveStep[place])
            elif digit == '9':
                roman.extend(tenStep[place] + tenStep[place + 1])
            elif '4' > digit > '0':
                roman.extend(tenStep[place] * int(digit))
            elif '9' > digit > '5':
                roman.extend(fiveStep[place] + (tenStep[place] * (int(digit)-5)))
            elif digit == '5':
                roman.extend(fiveStep[place])
            else:
                pass
            place -=1
        print ''.join(roman)
    file.close()


if __name__ == '__main__':
    main()