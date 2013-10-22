import sys

def main():
    file = open(sys.argv[1], "r")
    lines = file.readlines()
    for line in lines:
        list = line.split()
        index = int(list[-1]) + 1
        if index <= len(list):
            print list[0 - (index)]
    file.close()
    return

if __name__ == '__main__':
    main()

#original stuff in MthCheck
'''
    if index > len(list):
        raise ValueError() #error condition
    '''
#original stuff in main
'''    try:
            num = MthCheck(list)
            print list[0 - num]
        except ValueError:
            pass
    '''