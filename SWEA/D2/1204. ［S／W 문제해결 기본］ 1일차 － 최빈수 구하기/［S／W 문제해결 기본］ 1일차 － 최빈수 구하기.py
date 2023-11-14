
def solution():
  
  T = int(input())
  # 입력 받은 숫자로 배열을 초기화한다.
  arr = list(map(int, input().split()))

  # 해당 배열을 내림차순으로 정렬한다.
  arr.sort(reverse=True)

  # 배열의 마지막 인덱스부터 0 번째 인덱스까지 순회하면서 해당 인덱스에 입력된 값을 기준으로 count 한다.

  arr_len = len(arr)
  pivot_num = -1
  pivot_num_count = -1
  answer = 0

  for i in range(arr_len-1, 0, -1): # 배열 역순 순회
    # index 가 변경될때마다 최빈수를 카운트하고 최빈수가 변경되는 경우 answer 값을 변경한다.
    if -1 == pivot_num: 
      pivot_num = arr[i]
      pivot_num_count = arr.count(arr[i])
      continue

    # 현재 인덱스에 위치한 값의 총 갯수를 구한다.
    num_count = arr.count(arr[i])

    # 해당 값의 갯수를 pivot 과 비교하여 더많거나 같은 경우 값을 갱신한다.
    if num_count >= pivot_num_count:
      pivot_num = arr[i]
      pivot_num_count = arr.count(arr[i])

  answer = pivot_num
  print(f"#{T} {answer}")

def main():
  loop_count = int(input())

  for _ in range(loop_count):
    solution()

main()

