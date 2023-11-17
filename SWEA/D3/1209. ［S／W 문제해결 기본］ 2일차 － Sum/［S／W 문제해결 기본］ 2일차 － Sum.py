def solution():
  
  T = int(input())
  # 입력 받은 숫자로 배열을 초기화한다.

  arr = [list(map(int, input().split())) for _ in range(100)]

  answer = []
  right_cross = 0
  left_cross = 0

  for i in range(100):  # 행
    raw = 0
    col = 0
    for j in range(100):  # 열 
      raw += arr[i][j]
      col += arr[j][i]
      # print(f"raw {raw} | col {col}")
      if i == j: 
        right_cross += arr[i][j]
      if 99 == i+j:
        left_cross += arr[i][j]

    # print(f"행 {i}, 열 {j} | 결과 raw : {raw}, col :  {col}")

    answer.append(raw)
    answer.append(col)
  

  
  print(f"#{T} {max(list(set(answer)))}")

def main():
  for _ in range(10):
    solution()

main()

