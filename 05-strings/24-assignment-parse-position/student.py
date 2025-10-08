# write your code here
string = "(0.453, 9.120)"

def parse_position_x(string):
    index_commo = string.find(",")
    #print(index_commo)
    string_new = string[1:len(string)-1]   #12.453, 9.120
    #print("string_new:", string_new)
    x_string = string_new[:index_commo-1] #"12.453"
    #print("x_string:", x_string)
    x_float = float(x_string) #12.453
    #print("x_float:", x_float)
    return x_float
    # return x_float






def parse_position_y(string):
    index_commo = string.find(",")
    string_new = string[1:len(string)-1]   #12.453, 9.120
    y_string = string_new[index_commo + 1:] #"12.453"
    y_float = float(y_string) #12.453
    return y_float

