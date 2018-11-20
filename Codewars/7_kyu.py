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


# def filter_list(l):
#     # More advanced (Pythonic) solution:
#     return [x for x in l if type(x) is not str]

