def is_prime(n):
    total = 0
    for i in range(1,n+1):
        if n%i == 0:
            total = total + 1

    if total>2 or total == 1:
        return False
    else:
        return True        