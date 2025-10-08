# write your code here
def fix_date(date):
    new_date = date[6:] +"/"+ date[0:3] +date[3:5] 
    return new_date