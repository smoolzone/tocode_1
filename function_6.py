from random import randint


def guess_num():
    random_num = randint(1, 100)

    user_guess = int(input("Guess A num:"))

    if user_guess == random_num:
        print("Well done u guess the no.", random_num)
        return True
    else:
        print("You failed and the right no is:", random_num)
        return False


while not guess_num():
    print("Try Again")

"""
Uri's comments:
==============

* It's not what the assignment asked for. The assignment asked to print if
  the guess is too big or too small and then guess again, but the number
  should not change. Please try again.

"""
