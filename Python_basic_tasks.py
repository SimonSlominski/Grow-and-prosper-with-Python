"""
TASK 01 - Lesser of two evens

Write a function that returns the lesser of two given numbers *if* both numbers are even,
but returns the greater if one or both numbers are odd

lesser_of_two_evens(2,4) --> 2
lesser_of_two_evens(2,5) --> 5
"""

def lesser_of_two_evens(a,b):
    if a % 2 == 0 and b % 2 ==0:
        # Both numbers are even
        return min(a,b)
    else:
        # One or both number are odd
        return max(a,b)


"""
TASK 02 - Words crackers

Write a function that takes a two-word string and returns True if both words begin with same letter

words_crackers('Awesome Avengers') --> True
words_crackers('Awesome avengers') --> False
words_crackers('Dark Knight') --> False

words_crackers_second_option('Awesome Avengers') --> True
words_crackers_second_option('Awesome avengers') --> True 
words_crackers_second_option('Dark Knight') --> False
"""

def words_crackers(text):
    wordlist = text.split()
    # Get two words that can be compared using indexing
    return wordlist[0][0] == wordlist[1][0]

def words_crackers_second_option(text):
    wordlist = text.lower().split()
    # In this case, get two words that start with a lowercase letter, that why capitalization does't matter
    return wordlist[0][0] == wordlist[1][0]


"""
TASK 03 - Makes twenty

Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False

makes_twenty(20,10) --> True
makes_twenty(12,8) --> True
makes_twenty(2,3) --> False
"""

def makes_twenty(n1,n2):
    return n1+n2==20 or n1==20 or n2==20
