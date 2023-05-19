def solution():
    cook_start_time_hour, cook_start_time_minute = map(int, input().split())
    cook_time = int(input())


    calc_hour = (cook_start_time_minute + cook_time) // 60  # 분 계산식 -> 시간 산출
    calc_minute = (cook_start_time_minute + cook_time) % 60  # 분 계산식 -> 잔여 분 산출


    calc_result_hour = (cook_start_time_hour + calc_hour) % 24 # 시간 계산식

    print(f"{calc_result_hour} {calc_minute}")

if __name__ == '__main__':
    solution()
