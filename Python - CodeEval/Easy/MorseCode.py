__author__ = 'scottrussell'

import sys


morseDict = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
    '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
    '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P',
    '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T', '..-': 'U', '...-': 'V',
    '.--': 'W', '-..-': 'X', '-.--': 'Y', '--..': 'Z',
    '.----': '1', '..---': '2', '...--': '3', '....-': '4', '.....': '5',
    '-....': '6', '--...': '7', '---..': '8', '----.': '9', '-----': '0'
    }

def main():
    file = open(sys.argv[1], 'r')

    for line in file.readlines():
        word = []
        line = line.strip().split(' ')
        for beep in line:
            if beep is not '':
                word.append(morseDict[beep])
            else:
                word.append(' ')
        print "".join(word)

    file.close()


if __name__ == '__main__':
    main()