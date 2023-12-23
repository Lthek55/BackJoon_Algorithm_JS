def solution(num, k):
    pivot = str(num)
    token = str(k)
    ans = pivot.find(token)
    return ans +1 if ans >= 0 else -1
