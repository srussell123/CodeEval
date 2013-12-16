__author__ = 'scottrussell'

import sys

digits = {'a': '0', 'b': '1', 'c': '2', 'd': '3', 'e': '4', 'f': '5',
          'g': '6', 'h': '7', 'i': '8', 'j': '9'}

def main():
    file = open(sys.argv[1], 'r')
    for line in file.readlines():
        line = line.strip()
        hidden = []
        for x in line:
            if x.isdigit():
                hidden.append(x)
            elif x in digits:
                hidden.append(digits[x])
        if len(hidden) > 0:
            print ''.join(hidden)
        else:
            print 'NONE'
    file.close()


if __name__ == '__main__':
    main()