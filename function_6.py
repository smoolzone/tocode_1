from random import randint


def guess_num():
    random_num = randint(1, 100)

    user_guess = int(input("Guess A num:"))

    if user_guess > random_num:
        print("You win!!", random_num)
        return True
    else:
        print("You lost and the right no is:", random_num)
        return False


while not guess_num():
    print("Try Again")
