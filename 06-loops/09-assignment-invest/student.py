def invest(amount, rate, goal):
    if goal/amount <=1:
        return 0
    number_of_years = 0
    
    while goal/amount >1:
        number_of_years +=1
        amount = amount + amount*rate/100    
       
       
    return number_of_years
       
