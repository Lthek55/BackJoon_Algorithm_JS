
from collections import deque

def solution():
  
  T = int(input())
  # 입력 받은 숫자로 배열을 초기화한다.
  # 사다리 왼쪽/오른쪽으로 이동하는 경우 arr[fixed][moved] 로 좌표를 변경하여 해당 좌표를 기반으로 다시 이동한다.
  arr = [list(map(int, input().split())) for _ in range(100)]

  dx = [0,0,1]
  dy = [1,-1,0]

  for i in range(100):
    if arr[0][i] == 0 : 
      continue

    queue = deque()
    queue.append((0,i))

    visited = [[-1] * 100 for _ in range(100)]
    visited[0][i] = 1

    while queue:
      x,y = queue.popleft()


      for j in range(3):
        move_x_position = x + dx[j]
        move_y_position = y + dy[j]
        

        if 0 <= move_x_position <100 and 0<= move_y_position <100 and visited[move_x_position][move_y_position] == -1:
          if 1 == arr[move_x_position][move_y_position]: 
            # if i == 96:
            #   print(f"현재 좌표 : x {x} y {y}")
            #   print(f"dx {dx[j]} dy {dy[j]} 로 이동")
            #   print(f"이동할 좌표 : x {move_x_position} y {move_y_position}")
            #   print(f"visited[move_x_position][move_y_position] {visited[move_x_position][move_y_position]}" )
            #   print(f"arr[move_x_position][move_y_position] {arr[move_x_position][move_y_position]}")
            queue.append((move_x_position,move_y_position))
            # print(queue)
            visited[move_x_position][move_y_position] = visited[x][y] + 1
            break
          if 2 == arr[move_x_position][move_y_position]:
            # print(f"현재 좌표 : x {x} y {y}")
            # print(f"dx {dx[j]} dy {dy[j]} 로 이동")
            # print(f"이동할 좌표 : x {move_x_position} y {move_y_position}")
            # print(f"visited[move_x_position][move_y_position] {visited[move_x_position][move_y_position]}" )
            # print(f"arr[move_x_position][move_y_position] {arr[move_x_position][move_y_position]}")
            print(f"#{T} {i}")  
            #  print("통과")
  
          
        #   print(f"move_x_position {move_x_position}")
        #   print(f"move_y_position {move_y_position}")
        

def main():
    for _ in range(10):
      solution()

main()

