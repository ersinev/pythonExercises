# write your code here
# def coins(amount): #13
#     mod5 = amount//5 #2
#     rest2= amount- mod5*5 #3
#     mod2 = rest2//2 #1
#     rest1 = rest2- mod2*2
#     mod1= rest1//1
#     return(mod5+mod2+mod1)


def coins(amount):  
    coins_5 = amount//5 
    amount= amount%5 
    coins_2 = amount//2 
    amount= amount%2
    coins_1 = amount
    return(coins_5 + coins_2 + coins_1) 




    




