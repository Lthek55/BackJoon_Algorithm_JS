from functools import reduce
import sys

FILE_PATH= "./sample_dataset/5355.txt"


def is_numeric_string(value):
    if value.isdigit():
        return True

    if value.count('.') == 1:
        parts = value.split('.')
        if all(part.isdigit() for part in parts):
            return True

    return False

def convert_operator(acc, list_item_value):
    if list_item_value == "@":
        return acc * 3
    elif list_item_value == "%":
        return acc + 5
    elif list_item_value == "#":
        return acc - 7
    else:
        return acc + list_item_value


def solution():
    # 테스트 데이터 입력
    # sys.stdin = open(FILE_PATH, 'r')

    T = int(input())

    for i in range(T):
        # input 데이터 전처리
        preprocesssed_input_data = [
            float(input_arr_value)
                if is_numeric_string(input_arr_value)
                else input_arr_value
            for input_arr_value in input().split()
        ]

        # print("preprocesssed_input_data",preprocesssed_input_data)
        result = reduce(convert_operator, preprocesssed_input_data, 0)
        print(f"{result:.2f}")

if __name__ == '__main__':
    solution()
