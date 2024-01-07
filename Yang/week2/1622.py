# 1622. 공통 순열

a = input()
b = input()

answer = ''
    
for element in sorted(list(set(a) & set(b))) :
    answer += element

print(answer)