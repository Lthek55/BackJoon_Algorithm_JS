# 출력 값의 형태는 `#1 {result}` 와 같은 형태가 되어야 한다.
# 조건 1 : 판위의 룩은 모두 8개가 존재해야한다.
# 조건 2 : 판위의 룩은 서로 다른 룩들을 죽일 수 없는 위치에 존재해야한다. 즉 해당 룩의 행과 열에 다른 룩이 존재해서는 안된다.
# 조건 3 : 제일 처음 입력되는 값은 이와 같은 판별법을 몇번 실행할것인지를 의미한다.

T = int(input())

for input_count in range(1, T+1):
  graph = []
  for input_value in range(8):  # 값 입력
    graph.append(list(input()))

  # ! 행렬을 순회하며 'O' 인것 경우 판별법을 시작한다.
  # ! ( 기각 ) raw 의 경우 해당 좌표까지 도달하기까지 순회하는 과정에서 'O' 이 존재하는 경우 raw_pivot_count 를 누적하여 판별한다. / start ~ v 까지는 판별이 가능할지라도 v ~ end 까지는 판별이 불가능하다.

  pivot_position = []

  for raw in range(8): # graph 순회
    # ! 순회를 하는 과정에서 graph 를 직접사용한 순회는 index 를 구할 수 없으므로, 해당 좌표를 이용한 판별법을 이후에 사용할 수 없게 되므로 range() 를 사용하는 방식으로 변경해야한다.
    for col in range(8): 
      if 'O' == graph[raw][col] :
        pivot_position.append([raw,col])
      # print(f"raw: {raw}, col: {col}")
      # print(graph[raw][col])
  
  
  # ! pivot_position 좌표를 기준으로 하여 [raw, 0 ~ 7], [0 ~ 7, col] 좌표를 순회하며 룩의 갯수를 카운트 한다. or [raw, col] 의 좌표를 생략하고 룩이 존재하는지 순회한다.
    look_count = 0    
  for look_raw_position, look_col_position in pivot_position: # [raw, col] 룩이 존재하는 좌표 기준 행렬 순회

    # [raw, 0 ~ 8]
    for a in range(8):
      if a == look_col_position: 
        continue

      if 'O' == graph[look_raw_position][a]:
        look_count+=1


    # [0 ~ 8, col]
    for b in range(8):
      if b == look_raw_position: 
        continue

      if 'O' == graph[b][look_col_position]:
        look_count+=1

  answer = 'yes' if look_count == 0 else 'no'
  
  if len(pivot_position) != 8: 
    print(f"#{input_count} no")
    continue
  
  print(f"#{input_count} {answer}")





  