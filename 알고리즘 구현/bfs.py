import sys
from collections import deque

FILE_PATH= "./sample_dataset/bfs.txt"

def bfs(v):

    # bfs 의 다른 경우의 수를 저장 큐를 생성
    q = deque([v])

    while q:
        pivot = q.popleft()
        visited[pivot] = 1
        print(pivot, end=" ")

        for next in range(n+1):
            if not visited[next] and graph[pivot][next]:
                q.append(next)
                visited[next] = 1


if __name__ == '__main__':
    sys.stdin = open(FILE_PATH, 'r')

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

    bfs(v)

### 출력 결과 3 1 4 2 5 