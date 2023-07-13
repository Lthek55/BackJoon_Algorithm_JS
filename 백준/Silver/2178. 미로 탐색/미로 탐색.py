import sys
from collections import deque

def bfs(x,y):
    q = deque([(x,y)])

    while q:
        x1, y1 = q.popleft()

        for i in range(4):
            position_x = x1 + dx[i]
            position_y = y1 + dy[i]
            # print(graph)
            # print("x", position_x)
            # print("y", position_y)

            if n <= position_x or position_x < 0 or m <= position_y or position_y < 0:
                # print("pass 됨")
                continue

            if graph[position_x][position_y] == 0:
                continue

            if graph[position_x][position_y] == 1:
                graph[position_x][position_y] = graph[x1][y1] + 1
                # print("# 새로운 좌표 ========================================= # ")
                q.append((position_x, position_y))

    return graph[n-1][m-1]


if __name__ == '__main__':
    n, m = map(int, input().split())

    dx = [-1, 1, 0, 0]
    dy = [0, 0, 1, -1]

    graph = []

    for line in range(n):
        graph.append(list(map(int, input())))

    print(bfs(0, 0))
