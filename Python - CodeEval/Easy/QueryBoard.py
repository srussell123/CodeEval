__author__ = 'scottrussell'

import sys


def SetRow(board, row, val):
    for x in range(256):
        board[row][x] = val
    return board


def SetCol(board, col, val):
    for x in range(256):
        board[x][col] = val
    return board


def QueryRow(board, row):
    sum = 0
    for x in range(256):
        sum = sum + board[row][x]
    print int(sum)


def QueryCol(board, col):
    sum = 0
    for x in range(256):
        sum = sum + board[x][col]
    print int(sum)


def main():
    board = [[0 for x in range(256)] for y in range(256)]

    file = open(sys.argv[1], 'r')
    for line in file.readlines():
        line = line.rstrip().split(' ')
        if line[0] == "SetRow":
            board = SetRow(board, int(line[1]), int(line[2]))
        elif line[0] == "SetCol":
            board = SetCol(board, int(line[1]), int(line[2]))
        elif line[0] == "QueryRow":
            QueryRow(board, int(line[1]))
        elif line[0] == "QueryCol":
            QueryCol(board, int(line[1]))
    file.close()


if __name__ == '__main__':
    main()