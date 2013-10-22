import sys

def FizzBuzz(directions):
    for x in range(1, directions[2] + 1):
        if x % directions[0] == 0 and x % directions[1] == 0:
            print 'FB',
        elif x % directions[0] == 0:
            print 'F',
        elif x % directions[1] == 0:
            print 'B',
        else:
            print x,
    return

def main():
    file = open(sys.argv[1], "r")
    while 1:
        lines = file.readlines(100000)
        if not lines:
            break
        for line in lines:
            directions = [int(x) for x in line.split()]
            FizzBuzz(directions)
            print '\n', #newline between iterations
    file.close()
    return

if __name__ == '__main__':
    main()