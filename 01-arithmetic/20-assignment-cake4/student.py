# write your code here
def cake4(eggs, flour, butter, sugar, eggs_per_cake, flour_per_cake, butter_per_cake, sugar_per_cake):
    cakes_by_egg = eggs//eggs_per_cake
    cakes_by_flour = flour//flour_per_cake
    cakes_by_butter = butter//butter_per_cake
    cakes_by_sugar = sugar//sugar_per_cake

    return min(cakes_by_egg,cakes_by_flour, cakes_by_butter, cakes_by_sugar )