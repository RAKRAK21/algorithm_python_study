# import sys
# from collections import deque
# input = sys.stdin.readline

# N = int(input())

# stairs = []

# for i in range(N):
#     stairs.append(int(input()))

# routes = deque([[[1]], [[1, 2]], [[1, 3]]])
# points = deque([[stairs[0]], [stairs[0]+stairs[1]], [stairs[0]+stairs[2]]])


# def maximum_point(N):
#     if N == 1:
#         print(points[0])
#     elif N == 2:
#         print(points[1])
#     elif N == 3:
#         print(points[2])

#     for i in range(3, N):
#         routes.rotate(-1)
#         points.rotate(-1)

#         for idx, value in enumerate(routes[1]):
#             # 연속된 세 개의 계단을 건너는 경우
#             if (i-1) in value:
#                 continue
#             else:
#                 if len(routes[2]) == 0 or (i+1) not in routes[2][0]:
#                     routes[2] = []
#                     points[2] = []
#                 routes[2].append(routes[1][idx] + [i+1])
#                 points[2].append(points[1][idx] + stairs[i])

#         for idx, value in enumerate(routes[0]):
#             if len(routes[2]) == 0 or (i+1) not in routes[2][0]:
#                 routes[2] = []
#                 points[2] = []
#             routes[2].append(routes[0][idx] + [i+1])
#             points[2].append(points[0][idx] + stairs[i])

#         while len(routes[2]) > 10:
#             min_point = min(points[2])
#             idx = points[2].index(min_point)
#             points[2].pop(idx)
#             routes[2].pop(idx)

# maximum_point(N)

# print(max(points[2]))
# 실패한 코드

import sys
input = sys.stdin.readline

N = int(input())

stairs = []

for i in range(N):
    stairs.append(int(input()))

points = [0] * N


def maximum_point(N):
    if len(stairs) <= 2:
        print(sum(stairs))

    points[0] = stairs[0]
    points[1] = stairs[0] + stairs[1]

    for i in range(2, N):
        points[i] = max(points[i-3] + stairs[i-1] + stairs[i], points[i-2] + stairs[i])
        
    print(points[N-1])

maximum_point(N)