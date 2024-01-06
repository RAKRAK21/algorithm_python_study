n = int(input())

def fibo(n):
    first = 0
    second = 1

    if n == 1:
        return 1

    for i in range(1, n+1):
        current = first + second
        first = second
        second = current

    return current


print(fibo(n) % 1000000)