def solution(my_string, queries):
    
    
    for query in queries:
        query_start_position = query[0]
        query_end_position = query[1] + 1
        
        first_word=my_string[0:query_start_position]
        second_word="".join(list(reversed(my_string[query_start_position:query_end_position])))
        third_word=my_string[query_end_position:]
        
        my_string = first_word+second_word+third_word
        
    return my_string
