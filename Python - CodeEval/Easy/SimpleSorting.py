import sys


def main():
    file = open(sys.argv[1], 'r')
    for line in file.readlines():
        line = line.split()
        line = sorted([float(x) for x in line])
        for x in line:
            print '%.3f' % (x),
        print ''
    file.close()


if __name__ == '__main__':
    main()