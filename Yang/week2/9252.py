# 9252. LCS 2
a = input()
b = input()

if len(a) < len(b) :
    short = a
    long = b

else :
    short = b
    long = a

# answer_a = [0 for _ in range(len(short) + 1)]
answer_a = 0
            
for i in range(len(short)):
    for j in range(i, len(long)):
        # print(short[i], long[j])
        if short[i] == long[j] :
            # answer_a[i+1] = answer_a[i]+1
            answer_a += 1
            # print(answer_a)
            break

# print(max(answer_a))

# print('-------------')

answer_b = 0

for i in range(len(long)):
    for j in range(i, len(short)):
        print(long[i], short[j])
        if long[i] == short[j] :
            answer_b += 1
            break
        
# print(answer_b)

print(max(answer_a, answer_b))