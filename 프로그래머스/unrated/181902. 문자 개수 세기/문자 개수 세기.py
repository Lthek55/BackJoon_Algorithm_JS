def solution(my_string):
    answer = [0] * 52
    
    for i in my_string:
        if ord(i) <= 90 :
            # ASCII 에서 A 는 65 부터 시작하지만, 이 문제에서는 0 부터 시작하기에 -65 를 해줘야한다.
            answer[ord(i) - 65] += 1    
        else:
            # ASCII 에서 a 는 97 부터 시작하기에 -97 을 하고, A-Z 가 0 ~ 25 까지의 배열을 차지하고 있기에 a-z 는 26번째 인덱스부터 입력되어야한다.
            answer[ord(i) - 97 + 26] += 1
        
    return answer
