n = int(input())

towers = [int(x) for x in input().split()]
towers.reverse()

res = []
temp = []
missed = []
maximum = 0

for i in range(0, n-1) :
    temp.append(towers[i] - towers[i+1])
    
print(towers)
print(temp)

for k in range(0, n-1) :
    print(k)
    if temp[k] > 0 :
        print(f'max : {maximum}, tower : {towers[k]}')
        if maximum < towers[k] :
            maximum = towers[k]
        res.append(-1)
        missed.append(k)
        print(missed)
    else :
        # maximum = max(maximum, towers[k])
        res.append(n-k-1)
        if maximum < towers[k] :
            print(f'max : {maximum}, tower : {towers[k]}')
            # maximum = towers[k]
            # print(f'max : {maximum}, tower : {towers[k]}')
            # print(f'missed : {missed}')
            # print(f'res before : {res}')
            for element in missed:
                res[element] = n-k-1
            missed = []
            # print(f'res after : {res}')
        # res.append(k+1)
        # print(f'res : {res}')

res.append(0)

for element in missed:
    res[element] = 0

# for k in range(-1, -n, -1) :
#     if temp[k] < 0 :
#         res.append(-1)
#         missed.append(towers[k])
#     else :
#         res.append(n+k)

# print(missed)

# count = 1   

# for k in range(-1, -n, -1) :
#     if temp[k] < 0 :
#         count += 1
#         missed.append(towers[k])
#     else :
#         for _ in range(count):
#             res.append(n+k)
#         count = 1

# for _ in range(count):
#     res.append(0)

res.reverse()

print(*res)