from functools import reduce
import sys

FILE_PATH= "./sample_dataset/11653.txt"

def solution():
    # 테스트 데이터 입력
    # sys.stdin = open(FILE_PATH, 'r')

    input_value = int(input())

    quotient = input_value
    min_division_value = 2

    while quotient != 1:
        # 나눈 나머지 값이 0 인 경우
        # 해당 값으로 소인수 분해가 가능하다. -> 출력

        if quotient % min_division_value == 0 :
            # print("quotient",quotient)
            print(min_division_value)
            # 나누셈 몫값 재설정
            quotient = quotient // min_division_value

            # 최소 소인수 분해값 재설정
            min_division_value = 2
            continue

        min_division_value+=1

if __name__ == '__main__':
    solution()
