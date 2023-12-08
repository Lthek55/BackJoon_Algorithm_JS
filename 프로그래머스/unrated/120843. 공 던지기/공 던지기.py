def solution(numbers, k):
    answer = numbers*k
    return answer[::2][k-1]