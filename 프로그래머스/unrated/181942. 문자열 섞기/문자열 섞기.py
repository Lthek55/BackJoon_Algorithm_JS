def solution(str1, str2):
    # 길이가 같은 문자열 2개가 input 으로 주어진다.
    # str1, str2 가 동일한 문자로 구성된다고 확신할 수 있는 전제는 존재하지 않는다. 
    string1 = list(str1)
    string2 = list(str2)
    answer = ''
    
    for i in range(len(string1)):
        answer += string1[i] + string2[i]
    
    return answer