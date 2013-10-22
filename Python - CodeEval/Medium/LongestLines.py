import sys

def main():
    lines = []
    file = open(sys.argv[1], "r")
    #get the number of lines to print
    num = int(file.readline())

    #read each line into list (lines), ignore whitespace lines
    for line in file.readlines()[1:]:
        line = line.strip()
        if line:
            lines.append(line)

    #sort by length of string (descending)
    lines.sort(key=len, reverse = True)
    #print lines as defined by value stored in num
    for index in range(0, num):
        print lines[index]

    file.close()

if __name__ == '__main__':
    main()
