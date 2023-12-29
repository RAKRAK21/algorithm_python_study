from collections import deque

n, k = map(int, input().split())

circle = deque([x for x in range(1, n+1)])
order = []

while len(circle) > 1 :
    circle.rotate(1-k)
    order.append(circle.popleft())

order.append(circle[0])

print("<", end="")
print(*order, sep=', ', end="")
print(">")