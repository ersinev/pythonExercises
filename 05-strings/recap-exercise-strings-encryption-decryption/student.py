# write your code here
def decode1(text):
    return text.replace("A","o")


# print(decode1('SchAAl'))


def decode2(text):
   new_text = text[0::2]
   return new_text

# print(decode2('hqovtzdpozgm'))


def decode3(text):
    new_text =  text.split(" ")
    # print(new_text)
    new_text[0] = new_text[0][::-1] 
    joined_text = " ".join(new_text)
    return joined_text


# decode3("sepocseleT are too expensive.")    

def decode4(text):
    length = 0
    
    if len(text)%2 ==0:
        length= len(text)//2+2
    else:
        length = len(text)//2+3
        

    return text[2:length]

# print(decode4('oddolfijnnjifls'))