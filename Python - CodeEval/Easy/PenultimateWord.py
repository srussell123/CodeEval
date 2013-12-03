import sys


def main():
    file = open(sys.argv[1], 'r')
    for line in file.readlines():
        line = line.rstrip().split()
        print line[-2]
    file.close()


if __name__ == '__main__':
    main()

__author__ = 'scottrussell'
