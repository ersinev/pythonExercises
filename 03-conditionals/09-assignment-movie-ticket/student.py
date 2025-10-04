# write your code here
from math import ceil
def movie_ticket(duration, imax, student, ticket_count):
    if(duration<90):
        cost = 10
        if(imax == True and student==True):
            return (ceil(cost*1.20) -3)* ticket_count
        elif(imax == True and student == False):
            return ceil(cost*1.20) * ticket_count 
        elif(imax == False and student == True):
            return (cost -3) * ticket_count
        else:
            return cost * ticket_count
    elif(duration<120):
        cost = 11
        if(imax == True and student==True):
            return (ceil(cost*1.20) -3)* ticket_count
        elif(imax == True and student == False):
            return ceil(cost*1.20) * ticket_count 
        elif(imax == False and student == True):
            return (cost -3) * ticket_count
        else:
            return cost * ticket_count
        
    elif(duration<150):
        cost = 12
        if(imax == True and student==True):
            return (ceil(cost*1.20) -3)* ticket_count
        elif(imax == True and student == False):
            return ceil(cost*1.20) * ticket_count 
        elif(imax == False and student == True):
            return (cost -3) * ticket_count
        else:
            return cost * ticket_count    

    else:
        cost = 15
        if(imax == True and student==True):
            return (ceil(cost*1.20) -3)* ticket_count
        elif(imax == True and student == False):
            return ceil(cost*1.20) * ticket_count 
        elif(imax == False and student == True):
            return (cost -3) * ticket_count
        else:
            return cost * ticket_count