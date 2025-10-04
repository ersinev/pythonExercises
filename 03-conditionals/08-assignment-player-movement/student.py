# write your code here
def player_movement(position, left_arrow, right_arrow, shift):
    if(shift):
        if(left_arrow):
            position = position -2 
        if(right_arrow):
            position = position +2 
    else:        
        if(left_arrow):
            position = position - 1 
            
        if(right_arrow):
            position = position + 1        
            
    return position   