import sys

input = sys.stdin.readline

M, N = map(int, input().rstrip().split())

heights = [list(map(int, input().rstrip().split())) for i in range(M)]

