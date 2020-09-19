grades = [99, 100, 88, 70]
fruits = ['apple', 'banana', 'lemon']


print(max(grades))

for index, grade in enumerate(grades):
    if 90 < grade:
        print(f"{index} => {grade}")

high_grades_only = [g for g in grades if g > 80]
lengths = [len(t) for t in fruits]

print(high_grades_only)
print(lengths)

for i in range(1, 101):
    pass

squares = [n * n for n in range(1, 101)]
print(sum(squares))


def add_2(list):
    list.append(10)
    list.append(20)


x = [10, 20, 30]
add_2(x)
print(x)
