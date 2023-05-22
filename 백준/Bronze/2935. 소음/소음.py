from functools import reduce
import sys

FILE_PATH= "./sample_dataset/2935.txt"

def solution():
    # 테스트 데이터 입력
    # sys.stdin = open(FILE_PATH, 'r')

    n = int(input())
    op= input()
    m = int(input())

    if op == '+':
        print(n+m)
    if op == '*':
        print(n*m)


if __name__ == '__main__':
    solution()
