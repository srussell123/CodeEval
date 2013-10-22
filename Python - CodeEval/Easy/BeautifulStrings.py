import sys
import collections
import string


def main():
    file = open(sys.argv[1], 'r')
    for line in file.readlines():
        line = line.lower()
        letters = collections.Counter(line)
        beauty = 0
        weight = 26
        for key, value in letters.most_common():
            if key in string.ascii_lowercase[:26]:
                beauty += weight * value
                weight -= 1
        print beauty

    file.close()


if __name__ == '__main__':
    main()