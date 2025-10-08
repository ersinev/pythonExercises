def factorial(n):
    total = 1
    if n>1:
        for i in range(1,n+1):
            total = i* total

    return total    