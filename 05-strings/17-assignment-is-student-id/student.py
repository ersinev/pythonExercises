# write your code here
def is_student_id(string):
    if len(string) != 8:
        return False
    
    if string[0] not in ("r", "s", "R", "S"):
        return False
    
    if string[1:].isdigit():
        return True
    else:
        return False