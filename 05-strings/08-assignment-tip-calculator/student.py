# write your code here
def tip_calculator():
    price = int(input("Enter total pirice:"))
    tip_percentage = input("Enter tip percentage (default=20):")
   

    if tip_percentage == "":
        tip_percentage =20
    else:
        tip_percentage = int(tip_percentage)     

    final_pay = price + price * tip_percentage/100
    
    print(f"You have to pay {round(final_pay)}")