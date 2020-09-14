pick = int(input("Pick A Num...:" ))
if pick % 7 == 0:
    print("boom")


pick_2 = int(input("Pick A Number....:"))
if pick_2 % 7 == 0:
    print('Boom Boom')

if str(pick_2).find('7'):
    print('Booooom')

"""
Uri's comments:
==============

* This code works for numbers which are divisible by 7, but it doesn't
  work for numbers such as 71. Please try again.
* It's better to end a Python file with a line break.
  If you use PyCharm's Code -> Reformat Code feature, it will be done automatically.
  This is relevant to all your exercises.
* It's better to avoid using digits in variable names usually. You can separate 
  each exercise to a separate file.
* Your program outputs twice 'Boom Boom' and 'Booooom' for the number 49,
  which is not what the assignment asked for.
* In python you can use the operator "in" to check if a substring is contained
  in a string (or list).

"""
