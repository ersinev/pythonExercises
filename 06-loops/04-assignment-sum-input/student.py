# write your code here
def sum_input():
    total = 0
    number = int(input(f"Enter integer: "))
   
    while number != 0:
        if total > 0:
            number = int(input(f"Enter integer: "))
            

        total = total + number

    print(f"The sum equals {total}.")       




