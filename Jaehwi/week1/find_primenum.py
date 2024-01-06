M, N = map(int, input().split())

prime_num = []

for i in range(2, N+1):
    flag = True
    if i == 2 and M<=2:
        print(2)
        prime_num.append(2)
        continue
    for j in prime_num:
        if i % j == 0:
            flag=False
            break
    if flag == True:
        prime_num.append(i)
        print(i)


