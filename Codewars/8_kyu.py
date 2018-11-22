""" All tasks come from www.codewars.com """

"""
TASK: Short-Long-Short

Given 2 strings, a and b, return a string of the form short+long+short, with the shorter string on the outside
and the longer string on the inside. The strings will not be the same length, but they may be empty (length0).

For example:
solution("1", "22") // returns "1221"
solution("22", "1") // returns "1221" 
"""

def solution(a, b):
    if len(a) < len(b):
        return a+b+a
    else:
        return b+a+b

    
"""
TASK: Is this my tail?

Some new animals have arrived at the zoo. The zoo keeper is concerned that perhaps the animals do not have the right tails.
To help her, you must correct the broken function to make sure that the second argument (tail), 
is the same as the last letter of the first argument (body) - otherwise the tail wouldn't fit!

If the tail is right return true, else return false.
The arguments will always be strings, and normal letters.

Example:
assert_equals(correct_tail("Fox", "x"), True)
assert_equals(correct_tail("Giraffe", "d"), False)
"""

def correct_tail(body, tail):
    return body[-1] == tail[0]

