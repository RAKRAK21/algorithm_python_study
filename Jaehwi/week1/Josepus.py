N, K = map(int, input().split())

circular_list = [i for i in range(1, N+1)]

print("<", end="")
idx = -1
while len(circular_list) != 0:
    if len(circular_list) == 1:
        print(circular_list.pop(0), end="")
        break

    idx += K
    if idx >= len(circular_list):
        time = idx // len(circular_list)
        idx -= time * len(circular_list)
    
    print(circular_list.pop(idx), end=", ")
    idx -= 1

print(">")