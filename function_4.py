from random import randint


while True:
    Number = (randint(1, 1000000))
    if Number % 7 == 0 and Number % 13 == 0 and Number % 15 == 0:
        print(f"The number {Number} is divided by 7 and 13 and 15")
        
        break
    else:
        print(f"The number {Number} is not divided by 7 and 13 and 15 ")
        continue





