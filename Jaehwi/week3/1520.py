import sys
sys.setrecursionlimit=(10**6)

input = sys.stdin.readline

M, N = map(int, input().rstrip().split())
visited = [[False]*N for _ in range(M)]

table = []
for _ in range(M):
    table.append(list(map(int, input().rstrip().split())))

# Up, Down, Left, Right
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

stack = [(0,0,0,0)]
route = 0

def manage_visited():
    if len(stack) == 1:
        return
    if (stack[-1][0], stack[-1][1]) == (stack[-2][2], stack[-2][3]):
        return
    else:
        save_state = stack.pop()
        while (stack[-1][2], stack[-1][3]) != (save_state[0], save_state[1]):
            _, _, x, y = stack.pop()
            visited[x][y] = False
            
        stack.append(save_state)
            
            
    
def DFS(x, y):
    visited[x][y] = True
    if (x,y) == (M-1,N-1):
        global route
        route += 1
        manage_visited()
        return
    
    manage_visited()
            
    for i in range(4):
        new_x = x + dx[i]
        new_y = y + dy[i]
        
        if new_x < 0 or new_x >= M or new_y < 0 or new_y >= N:
            continue
        if visited[new_x][new_y]:
            continue
        if table[new_x][new_y] >= table[x][y]:
            continue
        stack.append((x,y,new_x,new_y))
        DFS(new_x, new_y)
        
    
    
DFS(0,0)
print(route)