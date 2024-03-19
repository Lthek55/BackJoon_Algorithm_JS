from collections import deque

def bfs(start,end):
  q = deque([(start, 0)])
  visited = set([start])

  while q:
     position, time = q.popleft()

     if position == end:
        return time
     
     for next in [position-1, position+1,position*2]:
        if 0<= next <= 100000 and next not in visited:
           q.append((next,time+1))
           visited.add(next)


if __name__ == '__main__':
    start,end = map(int,input().split())

    print(bfs(start, end))