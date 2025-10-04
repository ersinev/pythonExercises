# write your code here

def is_valid_month(month):
    return 1<= month<= 12

def is_leap_year(year):
    return (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))
                   #false        true         false              
                   #1             #0  


#4 ile bolunebilecek
#100 ile bolunmeyecek
#400 ile bolunebilecek

def has_30_days(month):
    return(max((month==4),(month==6),(month==9),(month==11)))

    #4,6,9,11

def has_31_days(month):
    return(max((month==1),(month==3),(month==5),(month==7),(month==8),(month==10),(month==12)))

def has_29_days(month, year):
    return (month == 2) and is_leap_year(year)

def has_28_days(month, year):
    return (month == 2) and not is_leap_year(year)


def is_valid_date(day, month, year):
    return (
        is_valid_month(month)
        and (
            (has_31_days(month) and 1 <= day <= 31)
            or (has_30_days(month) and 1 <= day <= 30)
            or (has_29_days(month, year) and 1 <= day <= 29)
            or (has_28_days(month, year) and 1 <= day <= 28)
        )
    )