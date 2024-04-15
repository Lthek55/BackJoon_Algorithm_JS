from collections import Counter

def solution(a, b, c, d):
    # 각 주사위의 숫자를 세어줍니다.
    counts = Counter([a, b, c, d])

    # 네 주사위의 숫자가 모두 같은 경우
    if len(counts) == 1:
        return a * 1111

    # 세개의 주사위의 숫자가 같은 경우 또는 두개씩 주사위가 같은 경우 
    elif len(counts) == 2:
        # value 값 기준 가장 큰/작은 값
        mp = max(counts, key=counts.get)
        mq = min(counts, key=counts.get)
        
        # key 값 기준 가장 큰/작은 값
        p = max(counts.keys())
        q = min(counts.keys())
        
        # 두개씩 주사위가 같은 경우
        if mp == mq:
            return (p + q) * abs(p - q)
        
        # 세개의 주사위가 같은 경우
        return (10 * mp + mq) ** 2

    # 두개의 주사위의 숫자가 같은 경우
    elif len(counts) == 3:
        pivot = [key for key, value in counts.items() if value == 1]
        print(pivot)
        return pivot[0] * pivot[1]

    # 네 주사위의 숫자가 모두 다른 경우
    else:
        return min(a, b, c, d)
