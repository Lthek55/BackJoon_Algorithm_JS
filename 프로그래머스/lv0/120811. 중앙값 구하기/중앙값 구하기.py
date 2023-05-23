def solution(array):
    # input array 의 길이는 홀수임이 명시되어 있다.
    pick_position = len(array) // 2
    return sorted(array)[pick_position]