import sys

def pangrams(line):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in line:
        if char in alphabet:
           alphabet = alphabet.replace(char, '')
    return alphabet


def main():
    file = open(sys.argv[1], "r")
    lines = file.readlines()
    for line in lines:
        line = line.lower()
        line = line.replace(" ", '')
        missingLetters = pangrams(line)
        if not missingLetters:
            print 'NULL'
        else:
            print missingLetters
    file.close()

if __name__ == '__main__':
    main()