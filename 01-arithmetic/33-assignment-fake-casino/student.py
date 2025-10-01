# write your code here
import random

def roll_dice(n):
    dice_number = random.randint(1,n)
    return dice_number



def fake_casino(n):
    random.seed(42)
    print(random.randint(1,n))
    print(random.randint(1,n))
    print(random.randint(1,n))
    print(random.randint(1,n))
    print(random.randint(1,n))
    