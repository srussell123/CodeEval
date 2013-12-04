import sys


def main():
    file = open(sys.argv[1], 'r')
    for line in file.readlines():
        line = line.rsplit()
        for x in range(len(line)):
            if line[x][0].isupper() is False:
                word = line[x][0].upper() + line[x][1:]
                line.insert(x, word)
                line.pop(x+1)
        print ' '.join(line)
    file.close()


if __name__ == '__main__':
    main()

__author__ = 'scottrussell'
