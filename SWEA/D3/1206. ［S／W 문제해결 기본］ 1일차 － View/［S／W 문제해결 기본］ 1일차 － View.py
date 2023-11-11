for s in range(1, 11):
    # 건물의 갯수를 입력받는다.
    apartment_count = int(input())

    # 건물의 높이를 입력받는다.
    apartment_height = list(map(int, input().split()))

    # 건물의 갯수에 따라서 건물의 높이를 비교한다.
    # !조건1 :비교하는 건물의 수는 현재 건물 위치의 +-2 로 한정한다.
    # !조건2: 건물 높이를 비교하는 시작점은 시작점 +2 부터 종점 -2 까지로 한정한다.

    answer_count = 0

    for i in range(2, apartment_count - 1):
        middle_answer = []
        minimum_diff_height = 0
        for j in range(5):  # 0 ~ 4 가지 순회해야되기 때문에 range(5) 로 설정한다.
            ## ====================================================================================================
            # ? +-2 위치의 건물과 비교하게 되는데 건물[r-1] 과의 높이 차이는 3 건물[r+2] 와의 높이차이는 1인 경우
            # ?/ 해당 좌표 건물의 조망권은 건물[r+2] 와의 높이차이인 1이 된다.
            # ?/ 각각의 건물간의 높이차이가 존재하므로 어떻게 해야하는지 모르겠다는것이 문제였다.
            # answer : 건물[r+-2] 와의 높이 차이를 구한다음에 최소치를 정답으로 설정하며, 사전 조건으로 건물[r+-2] 중에서 현재 건물보다 높이가 큰 경우만 계산하는 로직을 추가한다.
            ## ====================================================================================================

            # print('I',i)
            # print('J', j)
            comparison_point = -2 + j
            # print(f"comparison_point{comparison_point}")
            if comparison_point == 0: continue  # 현재 건물의 좌표에 도달한 케이스를 제외한다.

            diff_height = apartment_height[i] - apartment_height[
                i + comparison_point]  # 현재 건물을 기준으로 +-2 위치의 건물과 높이 차이를 구한다.
            if diff_height < 0: break  # 건물간 높이 차이값이 마이너스값인 경우 해당 건물을 조망권을 확보 할 수 없으므로 +1 좌표의 건물의 조망권을 구하기 위해 순회를 종료한다.
            middle_answer.append(diff_height)
            # print(f"diff_height {diff_height}")
            # print(f"middle_answer {middle_answer}")
            minimum_diff_height = min(middle_answer)
            # print(f"minimum_diff_height {minimum_diff_height}")
            if j == 4: answer_count += minimum_diff_height
                
    print(f"#{s} {answer_count}")








