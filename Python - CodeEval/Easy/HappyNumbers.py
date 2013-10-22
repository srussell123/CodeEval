import sys


def happyNumber(line):
    numbers = []
    while True:
        currentNum = 0
        for x in line:
            currentNum += sum([int(x) ** 2])
        if currentNum == 1:
            return 1
        elif currentNum in numbers:
            return 0
        else:
            numbers.append(currentNum)
            line = str(currentNum)



def main():
    file = open(sys.argv[1], 'r')
    for line in file.readlines():
        print happyNumber(line.strip())
    file.close()


if __name__ == '__main__':
    main()