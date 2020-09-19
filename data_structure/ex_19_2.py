#grades = [65, 88, 72, 91, 78, 96, 55, 98]

#high_grades_only = [i for i in grades if i > 70]

#print(high_grades_only)
#name = input('whats your name?')
#print(f'welcome {name}')
import sys
from statistics import mean


def get_above_average_grades(input_grades):
    grades = [int(n) for n in input_grades]
    average = mean(grades)
    above_average = [n for n in grades if n > average]
    return above_average


print(get_above_average_grades(sys.argv[1:]))



#high_grades = [int(i) for i in grades if i > 70]



#print(high_grades)