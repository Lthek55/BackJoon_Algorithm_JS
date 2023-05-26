def solution(num_list):
    answer = []
    even_count = 0 # 짝
    odd_count = 0 # 홀
    
    for i in num_list:
        if i % 2 == 0:
            even_count = even_count + 1
        else:
            odd_count = odd_count + 1
        
    return [even_count, odd_count]