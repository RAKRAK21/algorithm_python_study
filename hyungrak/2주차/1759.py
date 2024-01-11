from itertools import combinations


l, c = map(int, input().split())

c_list = list(input().split())
c_list.sort()
vowel = ['a', 'e', 'i', 'o', 'u']

combi_list = list(map(''.join, combinations(c_list, l)))

for c in combi_list:
    cnt_v = 0
    cnt_c = 0
    for char in c:
        if char in vowel:
            cnt_v += 1
        else:
            cnt_c +=1
    if cnt_v > 0 and cnt_c > 1:
        print(c)
        
'''처음에 모음이 최소 1개 이상 포함되어 있는 것만 출력했는데 계속 틀렸었다. 그래서 자음이 최소 2개 이상 포함되어 있는 것도 체크해서 출력했더니 통과됨.
l이 3 이상인 것이 조건이라 모음 조건만 확인해주면 될 줄 알았음. 반례가 무엇인지는 찾아보아야겠음.'''