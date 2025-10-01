# write your code here
# 1h = 3600seconds

def hours(duration):
    return duration//3600


def minutes(duration):
    h= hours(duration)
    left_seconds= duration-h*3600
    return left_seconds//60 

def seconds(duration):
    
    leftseconds = duration -hours(duration)*60*60- minutes(duration)*60
    return leftseconds 

