def valid_parentheses(string):
    if string == "":
        return True
    
    if len(string) % 2 != 0:
        return False

    if string[0] != "(":
        return False

    if string[-1] != ")":
        return False
    
    count= 0
    
    for char in string:
        if char == "(":
            count +=1
        else:
            count -=1

        if count<0:
            return False            

    return count == 0
    


