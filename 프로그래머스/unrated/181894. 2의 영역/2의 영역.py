def solution(arr):
    left, right = 0, len(arr)-1
    while (2 != arr[left] or 2 != arr[right]) and left < right: 
        if 2 != arr[left]:
            left +=1
        elif 2 != arr[right]:
            right -=1
        # 주어진 arr 에 2가 존재하지 않는 경우 left, right 가 일치하는 케이스 발생
        # 2!= arr[left/right] 를 추가한 이유는  [1,2,1] 와 같이 left, rigth 의 인덱스가 동일한데 2가 존재하는 경우가 존재하기 때문에 예외처리
        
        if left == right and 2 != arr[left] and 2 != arr[right]:
            return [-1]
        
    return arr[left:right+1]
        
    