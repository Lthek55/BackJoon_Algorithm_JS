from functools import reduce
import sys

FILE_PATH= "./sample_dataset/10817.txt"

def solution():
    # 테스트 데이터 입력
    # sys.stdin = open(FILE_PATH, 'r')

    input_arr = [int(num) for num in input().split()]
    input_arr.sort()
    print(input_arr[1])

if __name__ == '__main__':
    solution()
0