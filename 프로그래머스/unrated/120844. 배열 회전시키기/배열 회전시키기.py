# 시작 9:43
def solution(numbers, direction):
    return [*numbers[1:],numbers[0]] if "left" == direction else [numbers[-1],*numbers[:len(numbers)-1]]