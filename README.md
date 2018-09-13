# Tasks with Python
## List of tasks broken down by the level of difficulty

### Level 1 :chicken:
Python_basic_tasks.py

#### TASK 01 - Lesser of two evens

Write a function that returns the lesser of two given numbers *if* both numbers are even,
but returns the greater if one or both numbers are odd
```
lesser_of_two_evens(2,4) --> 2
lesser_of_two_evens(2,5) --> 5
```

#### TASK 02 - Words crackers

Write a function that takes a two-word string and returns True if both words begin with same letter
```
words_crackers('Awesome Avengers') --> True
words_crackers('Awesome avengers') --> False
words_crackers('Dark Knight') --> False

words_crackers_second_option('Awesome Avengers') --> True
words_crackers_second_option('Awesome avengers') --> True 
words_crackers_second_option('Dark Knight') --> False
```

#### TASK 03 - Makes twenty

Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False
```
makes_twenty(20,10) --> True
makes_twenty(12,8) --> True
makes_twenty(2,3) --> False
```


### Level 2 :panda_face:
Python_elementary_tasks.py


#### TASK 04 - MacDonald

Write a function that capitalizes the first and fourth letters of a name
```
macdonald('macdonald') --> MacDonald
```

#### TASK 05 - Master Yoda

Given a sentence, return a sentence with the words reversed
```
master_yoda('I am home') --> 'home am I'
master_yoda('We are ready') --> 'ready are We'
```

#### TASK 06 - Almost there

Given an integer n, return True if n is within 10 of either 100 or 200
```
almost_there(90) --> True
almost_there(104) --> True
almost_there(150) --> False
almost_there(209) --> True
```

#### TASK 07 - Find 33

Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
```
has_33([1, 3, 3]) → True
has_33([1, 3, 1, 3]) → False
has_33([3, 1, 3]) → False
```

#### TASK 08 Paper Doll

Given a string, return a string where for every character in the original there are three characters
```
paper_doll('Hello') --> 'HHHeeellllllooo'
paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'
```

#### TASK 09 Blackjack

Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum. 
If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. 
Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
```
blackjack(5,6,7) --> 18
blackjack(9,9,9) --> 'BUST'
blackjack(9,9,11) --> 19
```

#### TASK 10 Summer of '69'

Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending
to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers.
```
summer_69([1, 3, 5]) --> 9
summer_69([4, 5, 6, 7, 8, 9]) --> 9
summer_69([2, 1, 6, 9, 11]) --> 14
```

#### TASK 11 James Bond

Write a function that takes in a list of integers and returns True if it contains 007 in order
```
spy_game([1,2,4,0,0,7,5]) --> True
spy_game([1,0,2,4,0,5,7]) --> True
spy_game([1,7,2,0,4,5,0]) --> False
```
