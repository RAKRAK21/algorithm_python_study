
# t = int(input())
# for _ in range(t):
#     bracket = input()
#     vps = []
#     for i in bracket:
#         vps.append(i)
#         if i == '(':
#             continue
#         elif i == ')':
#             if len(vps) <= 1:
#                 print('NO')
#                 break
#             if vps[-2] == '(':
#                 vps.pop()
#                 vps.pop()
#             elif vps[-2] == ')':
#                 print('NO')
#                 break
        
#     if vps:
#         print('NO')
#     else:
#         print('YES')



t = int(input())

for i in range(t):
    vps = []
    bracket = input()
    tmp = 0
    for i in bracket:
        vps.append(i)
    
    for i in vps:
        if i == '(':
            tmp += 1
        elif i == ')':
            tmp -= 1
        if tmp < 0:
            print('NO')
            break
    
    if tmp > 0:
        print('NO')
    elif tmp == 0:
        print('YES')

