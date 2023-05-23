def solution(array):
    # 배열내 중복값 제거
    pre_array = list(set(array))
    
    # list 를 dict 로 전환. 초기값 0 셋팅
    pre_dict = dict.fromkeys(pre_array, 0)
    
    # 각 요소별 등장 횟수 적립
    for i in array:
        pre_dict[i] += 1
    
    # 등장횟수
    cumulative_count_arr = list(pre_dict.values())
    
    # 등장횟수 중 최대값
    max_value_count = max(cumulative_count_arr)
    
    # 등장 횟수가 중복인 경우 예외처리
    if cumulative_count_arr.count(max_value_count) != 1:
        return -1
    
    
    # pre_dict : 각 요소 ( key ) 별 등장횟수 ( value ) 를 dict 형태 저장
    # max_value_count : 요소의 등장횟수 중 최대값
    # dict 형태의 데이터에서 value 를 기반으로 key 를 뽑아내는 패턴 코드
    return dict((v,k) for k,v in pre_dict.items()).get(max_value_count)
    
    


