# 출력 값의 형태는 `#1 {result}` 와 같은 형태가 되어야 한다.
# 조건 1 : 평탄화 작업을 통해 양옆의 덤프간 높이차가 1로 만들고자 한다.
# 조건 2 : 평탄화 작업에는 횟수 제한이 존재한다.
# 조건 3 : 평탄화 작업 이후에는 max height 와 min height 차이값을 구한다.

def solution(answer_count):
  # 덤프의 높이 값을 입력 받아 배열에 초기화 한다.
  T = int(input())


  dump_arr = list(map(int,input().split()))

  # 배열에 담긴 덤프값을 내림차순으로 정렬한다
  dump_arr.sort(reverse=True)


  # 덤프값을 순회하며 배열의 가장 왼쪽 ( 제일 큰값 ) 과 가장 오른쪽 ( 제일 낮은값 ) 값을 평탄화 한다.
  # 매 순회마다 기준이 되는 가장 높은 값의 덤프는 평탄화 작업을 수행하기전 오른쪽의 덤프와의 값을 비교하여 높이차가 1인 경우 해당 덤프는 생략하고 다음 덤프부터 다시 평탄화 작업을 진행한다.


  dump_len = len(dump_arr)
  for _ in range(T):
    # 기준이 되는 덤프와 해당 덤프에서 +1 한 위치에 존재하는 덤프의 차이값을 구한다. 해당 값이 1인 경우 해당 덤프는 평탄화 작업을 생략하고 다음 덤프로 진행한다.

    # !) 평탄화 작업의 목적은 덤프간의 높이차를 줄이기 위함인데, 지금 고민하고 있는 부분은 가장 높은 값의 덤프를 가장 낮은 값의 덤프에 더한다고 하더라도 다음단계를 어떻게 판단하고 넘어갈지에 대한 부분이다.

    # answer > 가장 높은값의 덤프에서 -- 를 하고 가장 낮은 값의 덤프에 ++ 을 한다음에 다시 정렬을 진행한다면 각각의 덤프를 조건에 맞게 판별하고 평탄화하는 작업을 생략해도된다.
    dump_arr[0]-=1
    dump_arr[dump_len-1]+=1
    dump_arr.sort(reverse=True)
    
  answer = max(dump_arr) - min(dump_arr)
  print(f"#{answer_count} {answer}")
    # print(f"현재 진행중인 덤프횟수 {i}")
    # print(dump_arr)
    # print(f"가장 높은 덤프값 {max(dump_arr)}")
    # print(f"가장 낮은 덤프값 {min(dump_arr)}")

def main():
  for i in range(1,11):
    solution(i)

main()