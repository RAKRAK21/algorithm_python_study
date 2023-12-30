from math import sqrt

m, n = map(int, input().split())

prime = [x for x in range(3, n+1, 2)]

for i in range(3, int(sqrt(n))+1, 2) :
    not_prime = [i * k for k in range(3, n//i+1, 2)]
    prime = list(set(prime) - set(not_prime))

prime.append(2)

prime = sorted([x for x in prime if x>=m])

for element in prime :
    print(element)