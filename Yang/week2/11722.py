# 11722. 가장 긴 부분 감소하는 수열

n = int(input())

numbers = [int(x) for x in input().split()]
answer = [1 for _ in range(len(numbers))]
numbers.reverse()

for i in range(n) :
    for j in range(i) :
        if numbers[i] > numbers[j] :
            answer[i] = max(answer[i], answer[j]+1)

print(max(answer))