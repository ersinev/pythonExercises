# def gcd(a, b):
#     if a<0:
#         a= -a
#     if b<0:
#         b= -b    

#     top = min(a,b)   
#     list_of_numbers = []
#     if top <0:
#         top = -top
#     for i in range(1,top+1):
#         if a%i ==0 and b%i ==0:
#             list_of_numbers.append(i)

#     print(list_of_numbers)
#     return max(list_of_numbers)          


# print(gcd(10,-150))


def gcd(a, b):
    
    if a < 0:
        a = -a
    if b < 0:
        b = -b

    top = min(a,b)

    for i in range(top,0,-1):
        if a%i == 0 and b%i == 0:
            return i


print(gcd(100,150))