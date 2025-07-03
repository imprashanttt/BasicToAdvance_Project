def fibo(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

# Print Fibonacci from position 1 to 10
for i in range(1, 11):
    print(fibo(i))
