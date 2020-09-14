a = int(input("First Number..:"))
b = int(input("Second number...:"))
c = int(input("In Range Of..:"))
d = ((((c - 1) * b) + 2 * a) * c) / 2
print(d)

"""
Uri's comments:
==============

* Very good! This code works.
* The input is done in int, but the result is in float. Maybe it's better to
  convert it to int (it can't be a non-integer number).

"""
