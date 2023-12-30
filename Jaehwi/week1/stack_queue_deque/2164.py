import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())


cards = deque([i+1 for i in range(N)])

turn = True
while len(cards) != 1:
    if turn:
        cards.popleft()
        turn = False
    else:
        cards.rotate(-1)
        turn = True

print(cards[0])