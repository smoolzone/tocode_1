from random import randint


while True:
    Number = (randint(1, 1000000))
    if Number % 7 == 0 and Number % 13 == 0 and Number % 15 == 0:
        print(f"The number {Number} is divided by 7 and 13 and 15")
        
        break
    else:
        print(f"The number {Number} is not divided by 7 and 13 and 15 ")
        continue


"""
Uri's comments:
==============

* Very good! This code works.
* `if Number % 7 == 0 and Number % 13 == 0 and Number % 15 == 0` is correct, 
  however I recommend adding parentheses so it would be more readable.
* In Python it's common to use variable names in lowercase. You can use "_" to separate between words.
  For example, use "number" instead of "Number".
* "continue" is not necessary here.
* "divisible" is the correct English word.
* Here is how your code looks reformatted:

from random import randint

while True:
    number = (randint(1, 1000000))
    if (number % 7 == 0) and (number % 13 == 0) and (number % 15 == 0):
        print(f"The number {number} is divisible by 7 and 13 and 15")

        break
    else:
        print(f"The number {number} is not divisible by 7 and 13 and 15 ")

"""
