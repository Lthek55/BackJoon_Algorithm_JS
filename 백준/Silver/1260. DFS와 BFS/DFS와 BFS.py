def bfs():
    q = [v]

    while q:
        pivot = q.pop(0)
        # 시작하는 pivot 의 방문 정보 기록
        visited[pivot] = 1

        print(pivot, end = " ")

        # 모든 행을 순회한다.
        for next in range(1, n+1):
            # 조건 : 방문기록이 없고 graph 좌표상 값이 1인 경우
            if not visited[next] and graph[pivot][next]:
                # 방문기록을 추가한다.
                visited[next] = 1
                # 기준이 되었던 idx 값을 큐에 저장한다.
                # 이 값은 BFS 에서 다음 노드의 시작 기준이 된다.
                q.append(next)

                #print(next,"추가됨")
        #print(pivot, visited)


def dfs(pivot):
    print(pivot, end=" ")
    visited[pivot] = 1

    for next in range(1, n+1):
        if not visited[next] and graph[pivot][next]:
            dfs(next)




if __name__ == '__main__':

    # n = 정점의 갯수
    # m = 간선의 갯수
    # v = 시작점
    n, m, v = map(int, input().split())

    # graph 생성
    graph = [[0] * (n+1) for _ in range(n+1)] # 간선 번호가 arr index 를 감안하고 작성되지 않았기 때문에 간선의 값을 체크 할 수 있도록 n+1 을 한다.

    # 1) 간선값 입력 받기
    # 2) 각 간선값을 graph 에 입력
    for _ in range(m):
        x,y = map(int, input().split())
        graph[x][y] = 1
        graph[y][x] = 1

    # visited
    visited = [0] * (n+1)

    dfs(v)

    print()
    visited = [0] * (n + 1)
    bfs()