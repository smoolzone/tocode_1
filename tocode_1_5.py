a = int(input("Pick A Num...:"))
b = int(input("Pick another Num...:"))
c = int(input("And pick another Num....:"))
if a > b and a > c:
    print("AAAA")
if b > a and b > c:
    print("BBBBB")
if c > a and c > b:
    print("CCCCC")

"""
Uri's comments:
==============

* Your code prints a string, but the assignment asked to print a number (the biggest number).
* You can use the max built-in function instead of lines 4 to 9.
  Built-in Functions in Python: https://docs.python.org/3/library/functions.html

"""
