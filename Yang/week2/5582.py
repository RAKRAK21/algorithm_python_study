# 5582. 공통 부분 문자열

a = input()
b = input()

if len(set(a) & set(b)) == 0 :
    print(0)

