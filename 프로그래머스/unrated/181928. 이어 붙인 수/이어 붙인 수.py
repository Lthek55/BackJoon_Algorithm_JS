def solution(num_list):
    answer = 0
    even_value =''
    odd_value = ''
        
    for i in num_list:
        if i % 2 ==0 :
            even_value += str(i) 
        else:
            odd_value += str(i) 
    
    
    return int(even_value) + int(odd_value) 