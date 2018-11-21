""" All tasks come from www.codewars.com """

"""
TASK: Leap Years

In this kata you should simply determine, whether a given year is a leap year or not. 
In case you don't know the rules, here they are:

years divisible by 4 are leap years
but years divisible by 100 are no leap years
but years divisible by 400 are leap years
"""

def isLeapYear(year):
    return (year % 100 != 0 and year % 4 == 0) or year % 400 == 0


"""
TASK: List Filtering

In this kata you will create a function that takes a list of non-negative integers and strings and 
returns a new list with the strings filtered out.

Example:
filter_list([1,2,'a','b']) == [1,2]
filter_list([1,'a','b',0,15]) == [1,0,15]
filter_list([1,2,'aasf','1','123',123]) == [1,2,123]
"""

def filter_list(l):
    list = []
    for item in l:
        if type(item) == int:
            list.append(item)
    return list

# More advanced (Pythonic) solution:
# def filter_list(l):
#     return [x for x in l if type(x) is not str]


"""
TASK: Credit Card Mask

Usually when you buy something, you're asked whether your credit card number, phone number or answer
to your most secret question is still correct. However, since someone could look over your shoulder, 
you don't want that shown on your screen. Instead, we mask it.

Your task is to write a function maskify, which changes all but the last four characters into '#'.

Examples:
maskify("4556364607935616") == "############5616"
maskify(     "64607935616") ==      "#######5616"
maskify(               "1") ==                "1"
maskify(                "") ==                 ""
"""

# Newbie style
def maskify(x):
    string = ''
    for e in x[:-4]:
        e = "#"
        string += e
    for e in x[-4:]:
        string += e
    return string

# More advanced (Pythonic) solution:
# def maskify(cc):
# #     return "#"*(len(cc)-4) + cc[-4:]

