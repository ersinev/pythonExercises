# write your code here
def is_divisible(a, b):
    return max((a%b) < 1,(b%a)<1)