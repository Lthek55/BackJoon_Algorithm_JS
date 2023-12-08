def solution(box, n):
    x,y,z = box
    x_count = x//n 
    y_count = y//n 
    z_count = z//n 
    return x_count * y_count * z_count
