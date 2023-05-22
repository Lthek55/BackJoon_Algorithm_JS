from functools import reduce
import sys

FILE_PATH= "./sample_dataset/2675.txt"

def solution():
    # 테스트 데이터 입력
    # sys.stdin = open(FILE_PATH, 'r')

    T = int(input())

    for i in range(T):
        # input 데이터 전처리
        loop_count, s = input().split()

        result = reduce(lambda acc, item: acc + item * int(loop_count), list(s),'')

        print(result)

if __name__ == '__main__':
    solution()
