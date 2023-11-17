from collections import deque

def solution():

  T = int(input())
  queue = deque()

  input_map = [list(map(int, input().split())) for _ in range(100)]
  

  dx = [0,0,1]
  dy = [-1,1,0]


  start_position = -1
  res_count = 999999999
  pivot_move_count = 0 

  for i in range(100):
    if input_map[0][i] == 1:
      queue.append((0,i))
      checked_map = [[-1]* 100 for _ in range(100)] # 지나온 경로를 표시하는 지도 생성
      checked_map[0][i] = 1 # 지나온 경로를 체크하는 지도에서 시작 좌표의 값을 1로 설정

      # last_visited_position = deque() # 마지막 방문 위치를 저장하여 이동 횟수를 구한다.

      while queue:
        x, y = queue.popleft()
        for j in range(3):
          move_x = x + dx[j]
          move_y = y + dy[j]
          if 0<= move_x< 100 and 0<= move_y< 100 and checked_map[move_x][move_y] == -1:
            if 1== input_map[move_x][move_y]:
              queue.append((move_x, move_y))
              checked_map[move_x][move_y] = checked_map[x][y] + 1 
              # print(f"해당 좌표로 이동합니다 x {move_x} y {move_y}")
              pivot_move_count = checked_map[move_x][move_y]
              break # 하나의 방향이 정해졌다면 queue 에 다른 방향이 입력되지 않게 break 를 걸어줘야한다.

      if res_count >= pivot_move_count: # 각 사다리의 이동 횟수 비교 및 값 갱신 ( 최소값 )
        start_position = i
        res_count = pivot_move_count        


  print(f"#{T} {start_position}") # 


def main():
    for _ in range(10):
      solution()

main()

