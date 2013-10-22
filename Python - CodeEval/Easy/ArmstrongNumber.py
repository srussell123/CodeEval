import sys


def armstrong(line):
    sum = 0
    for x in range(len(line)):
        sum += (int(line[x]) ** len(line))
    if str(sum) == line:
        print True
    else:
        print False


def main():
    file = open(sys.argv[1], 'r')
    for line in file.readlines():
        line = line.strip('\n')
        armstrong(line)
    file.close()


if __name__ == '__main__':
    main()