import sys

def mod(n, m):
    quotient = n / m
    print n - m * quotient

def main():
    file = open(sys.argv[1], 'r')
    for line in file.readlines():
        line = line.split(',')
        line[0], line[1] = int(line[0]), int(line[1])
        mod(line[0], line[1])

    file.close()

if __name__ == '__main__':
    main()