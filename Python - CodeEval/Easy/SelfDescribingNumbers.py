import sys

def selfDescribing(line):
    for x in range(len(line)):
        if not int(line[x]) == line.count(str(x)):
            return False
    return True


def main():
    file = open(sys.argv[1], 'r')
    for line in file.readlines():
        line = line.strip('\n')
        if selfDescribing(line):
            print 1
        else:
            print 0
    file.close()

if __name__ == '__main__':
    main()