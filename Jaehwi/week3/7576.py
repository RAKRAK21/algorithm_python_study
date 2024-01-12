from collections import deque

M, N = map(int, input().split())

riped_idx = []
zero_count = 0
tomato = []


# Up Down Left Right
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x,y):
    visited = [[False]*M for _ in range(N)]
    
    queue = deque([(x,y)])
    
    visited[x][y] = True
    
    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            
            if new_x < 0 or new_x >= N or new_y < 0 or new_y >= M:
                continue
            if visited[new_x][new_y]:
                continue
            if tomato[new_x][new_y] == -1:
                continue
            if tomato[new_x][new_y] == 1:
                continue
            if tomato[new_x][new_y] == 0:
                tomato[new_x][new_y] = tomato[x][y] + 1
                visited[new_x][new_y] = True
                queue.append((new_x, new_y))
            else:
                if tomato[new_x][new_y] > tomato[x][y] + 1:
                    tomato[new_x][new_y] = tomato[x][y] + 1
                    visited[new_x][new_y] = True
                    queue.append((new_x, new_y))
    

for x in range(N):
    tomato_row = list(map(int, input().split()))
    for y, value in enumerate(tomato_row):
        if value == 1:
            riped_idx.append((x, y))
        elif zero_count == 0 and value == 0:
            zero_count += 1
    tomato.append(tomato_row)
            
if zero_count == 0:
    print("0")

else:    
    for x,y in riped_idx:
        BFS(x,y)

    maximum = 0
    zero_count = 0
    for row in tomato:
        for item in row:
            if item == 0:
                zero_count += 1
            elif item > maximum:
                maximum = item
    
    if zero_count > 0:
        print(-1)
    else:            
        print(maximum -1)