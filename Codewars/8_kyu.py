""" All tasks come from www.codewars.com """

"""
TASK: 

Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside
and the longer string on the inside. The strings will not be the same length, but they may be empty (length0).

For example:
solution("1", "22") // returns "1221"
solution("22", "1") // returns "1221" 
"""

# def solution1(a, b):
#     return a+b+a if len(a)<len(b) else b+a+b
#
# def solution(a, b):
#     return '{0}{1}{0}'.format(*sorted((a, b), key=len))

def solution(a, b):
    if len(a) < len(b):
        return a+b+a
    else:
        return b+a+b


x = solution('1', '22')
y = solution('1', '22')

print(x, y)
print('-'*10)


