import sys


def distance(line):
    xrange = (line[0] - line[2]) ** 2
    yrange = (line[1] - line[3]) ** 2
    return (xrange + yrange) ** (1.0/2)

def main():
    file = open(sys.argv[1], 'r')
    for line in file.readlines():
        line = map(int, line.translate(None, '(),').split())
        print int(distance(line))
    file.close()


if __name__ == '__main__':
    main()


__author__ = 'scottrussell'

