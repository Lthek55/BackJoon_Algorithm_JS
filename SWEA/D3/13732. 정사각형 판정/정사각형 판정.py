def solution():
  N = int(input())
  input_map = [list(input()) for _ in range(N)]
  
  pivot_position = []

  for i in range(N):
    for j in range(N):
      if input_map[i][j] == '#':  
        pivot_position.append((i,j))


  start_x, start_y = pivot_position[0]
  end_x, end_y = pivot_position[-1]

  # 좌표 판정 결과 정사각형이 아닌것
  if end_x - start_x != end_y - start_y:
    return False

  # 좌표 판정 결과 1차로 정사각형이라고 판정
  if end_x - start_x == end_y - start_y:
    # 좌표 시작점부터 끝점까지 순회하며 '#' 가 존재하는지 확인
    for i in range(start_x, end_x+1):
      for j in range(start_y, end_y+1):
        if '#' != input_map[i][j]:
          return False
  
  return True



def main():
  T = int(input())
  for idx in range(1,T+1):
    res = solution()
    print(f"#{idx} {'yes' if res == True else 'no'}")

main()

