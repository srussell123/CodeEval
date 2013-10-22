import sys

def main():
    file = open(sys.argv[1], 'r')
    for line in file.readlines():
        line = int(line, 16)
        print line

    file.close()

if __name__ == '__main__':
    main()