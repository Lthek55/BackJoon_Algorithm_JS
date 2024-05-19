# dfs 풀이(미사용)
# input = ["aya", "yee", "u", "maa", "wyeoo"]
# compare_word = ["aya", "ye", "woo", "ma"]

# input 배열의 길이만큼 배열을 돈다.
# 각 순회마다 dfs 를 실행하며 compare_word 에 담긴 단어가 포함되어 있는지 확인한다.
# false: input 배열의 다음 단어로 넘어간다.
# true: input 단어에서 매칭된 compare_word 단어를 제거하고, 남은 단어를 기반으로 dfs 를 다시 실행한다. 이때, compare_word 의 단어들은 1번만 사용될 수 있음으로 이를 기억할 수 있는 object 를 만들어 기록한다.
# 남은 단어도 compare_word 의 단어를 한번씩만 사용하는 조건을 만족하면 true 를 반환한다. 
# 이때 n 번의 dfs 를 모두 만족하는 경우만 answer++ 한다. 


def solution(babbling):
    compare_word = ["aya", "ye", "woo", "ma"]
    answer = 0
    
    for i in babbling: 
        word = ""
        cnt = 0
        for j in i: 
            word += j
            if word in compare_word:
                word = ""
                cnt += 1
                
                
        if len(word) == 0 and cnt > 0:  # 조건에 부합하지 않아 남은 word 가 있는 경우 answer 를 증가 시키지 않음.
            answer += 1
            
    return answer