def solution():
    cook_start_time_hour, cook_start_time_minute, cook_start_time_second = map(int, input().split())
    cook_time = int(input())

    # 초 계산식
    step1_calc_second_result = (cook_start_time_second + cook_time) % 60  # 분 계산식 -> 잔여 초 산출
    step1_calc_minute = (cook_start_time_second + cook_time) // 60 # 분 계산식 -> 분 산출


    # 분 계산식
    step2_calc_minute_result = (cook_start_time_minute + step1_calc_minute) % 60 # 분 계산식 -> 잔여 분 산출
    step2_calc_hour = (cook_start_time_minute + step1_calc_minute) // 60 # 분 계산식 -> 시간 산출

    # 시간 계산식
    step3_calc_hour_result = (cook_start_time_hour + step2_calc_hour) % 24 # 시간 계산식


    print(f"{step3_calc_hour_result} {step2_calc_minute_result} {step1_calc_second_result}")

if __name__ == '__main__':
    solution()
