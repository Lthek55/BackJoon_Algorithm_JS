from itertools import chain

def solution(arr, intervals):
    answer = []
    for idx, (i,j) in enumerate(intervals):
        answer.append(arr[i:j+1])
    return list(chain.from_iterable(answer))