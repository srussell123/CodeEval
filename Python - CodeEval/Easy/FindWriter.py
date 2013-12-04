import sys


def main():
    file = open(sys.argv[1], 'r')
    for line in file:
        author = ''
        line = line.rstrip()
        if len(line) is not 0:
            word = line[0:line.index('|') + 1]
            nums = map(int, (line[line.index('|') + 2:].split()))
            for x in nums:
                author += word[x-1]
            print author

    file.close()


if __name__ == '__main__':
    main()

__author__ = 'scottrussell'
