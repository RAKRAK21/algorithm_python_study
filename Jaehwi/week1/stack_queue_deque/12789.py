import sys

N = int(sys.stdin.readline().rstrip())
seq = list(map(int, sys.stdin.readline().rstrip().split()))
members = seq[:]

stack = []
flag = False

for i in range(N):
    if members[i] == min(seq):
        seq.pop(seq.index(min(seq)))
        continue
        
    while stack:
        if len(stack) != 0 and stack[-1] == min(seq):
            seq.pop(seq.index(stack.pop()))
        else:
            break            

    if len(stack) != 0 and stack[-1] < members[i]:
        flag = True
        break
    else:
        stack.append(members[i])

while stack:
        if len(stack) != 0 and stack[-1] == min(seq):
            seq.pop(seq.index(stack.pop()))
        else:
            break

if stack or flag or seq:
    print("Sad")
else:
    print("Nice")