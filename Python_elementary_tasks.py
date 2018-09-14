
"""
TASK 07 - MacDonald

Write a function that capitalizes the first and fourth letters of a name

macdonald('macdonald') --> MacDonald
"""

def macdonald(name):
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        return 'Name is too short!'


def macdonald_second_option(name):
    # as you can see this method is longer, but for beginners could be more understandable
    string = ""

    for index, letter in enumerate(name):
        if index == 0:
            string += letter.upper()
        elif index == 3:
            string += letter.upper()
        else:
            string += letter.lower()
    return string


"""
TASK 08 - Master Yoda

Given a sentence, return a sentence with the words reversed

master_yoda('I am home') --> 'home am I'
master_yoda('We are ready') --> 'ready are We'
"""

def master_yoda(text):
    return ' '.join(text.split()[::-1])


"""
TASK 09 - Almost there

Given an integer n, return True if n is within 10 of either 100 or 200

almost_there(90) --> True
almost_there(104) --> True
almost_there(150) --> False
almost_there(209) --> True
"""

def almost_there(n):
    return n in range(90,110) or n in range(190,210)

def almost_there_second_option(n):
    return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))


"""
TASK 10 - Find 33

Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False
"""

def has_33(nums):
    for x in range(len(nums) - 1):
        if nums[x] == 3 and nums[x + 1] == 3:
            return True
    return False


"""
TASK 11 Paper Doll

Given a string, return a string where for every character in the original there are three characters

paper_doll('Hello') --> 'HHHeeellllllooo'
paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'
"""

def paper_doll(text):
    new_lst = ''

    for i in text:
        new_lst += i * 3
    return new_lst


"""
TASK 12 Blackjack

Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. 
If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. 
Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

blackjack(5,6,7) --> 18
blackjack(9,9,9) --> 'BUST'
blackjack(9,9,11) --> 19
"""

def blackjack(a, b, c):
    if sum((a, b, c)) <= 21:
        return sum((a, b, c))
    elif sum((a, b, c)) <= 31 and 11 in (a, b, c):
        return sum((a, b, c)) - 10
    else:
        return 'BUST'


"""
TASK 13 Summer of '69'

Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending
to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.

summer_69([1, 3, 5]) --> 9
summer_69([4, 5, 6, 7, 8, 9]) --> 9
summer_69([2, 1, 6, 9, 11]) --> 14
"""

def summer_69(arr):
    flag = False
    sum_of_nums = 0

    for num in arr:
        if num == 6:
            flag = True         # Turn the flag on if the number is 6
            continue
        if num == 9:
            flag = False        # Turn the flag Off when 9 is seen after 6
            continue
        if flag == False:
            sum_of_nums += num  # Keep on adding the nums otherwise
    return sum_of_nums


"""
TASK 14 James Bond

Write a function that takes in a list of integers and returns True if it contains 007 in order
 
spy_game([1,2,4,0,0,7,5]) --> True
spy_game([1,0,2,4,0,5,7]) --> True
spy_game([1,7,2,0,4,5,0]) --> False
"""

def spy_game(nums):
    code = [0, 0, 7, 'x']
    # Using for loop we can delete elements [0,0,7] from the list.
    # Therefore, in the end, the length of the list = 1 and that means the only 'x' remain
    # [0,7,'x']
    # [7,'x']
    # ['x'] length = 1

    for num in nums:
        if num == code[0]:
            code.pop(0)  # code.remove(num) also works

    return len(code) == 1
