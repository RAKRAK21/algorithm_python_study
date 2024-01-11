from collections import deque

N, M = map(int, input().split())

maze = []
visited = [[False]*(M) for _ in range(N)]

# up, down, left, right
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x, y):
    queue = deque([(x,y)])
    
    visited[x][y] = True
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if new_x <= -1 or new_x >= N or new_y <= -1 or new_y >= M :
                continue
            if visited[new_x][new_y]:
                continue
            if maze[new_x][new_y] == '1':
                maze[new_x][new_y] = int(maze[x][y]) + 1
                visited[new_x][new_y] = True
                queue.append((new_x,new_y))
            
        
for _ in range(N):
    maze.append(list(input()))
    
    
for x in range(N):
    for y in range(M):
        if not visited[x][y]:
            BFS(x, y)

print(maze[N-1][M-1])