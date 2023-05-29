from itertools import product 

# permutations :순열, 인자로 주어진 값을 '한번만' 사용하여 순열을 생성한다.
# product : 중복순열, 인자로 주어진 값을 '중복' 사용하여 순열을 생성한다.
    # product 사용시 일반적인 permutations 사용법과는 다르게 2번째 인자에 repeat 값을 넣어줘야한다.

def solution(l, r):
    # 1) 방법 1 : 순회
    # 2) 방법 2 : 조합 - 필터링
    
    
    # print(list(product([0,5], repeat=3)))
    
    answer = [int("".join(a)) for a in list(product(['0','5'], repeat=len(str(r))))]
    answer = list(filter(lambda x: x >=l , answer))
    answer = list(filter(lambda x: x <=r , answer))
    
    
    return [-1] if not answer else list(sorted(answer))