"""name = input("What is your name?")
while name.startswith('a'):
    print("thats not good name Try again")
    name = input("who are you?")"""

while True:
    name = input("name?")
    if name.startswith('a'):
        break
    print("no good")

"""text = "yo yo mayb thats's gonna work"

 
for i in text.split():
    print(f"Word = {i}; len = {len(i)}")"""

for i in range(1, 11):
    for j in range(1, 11):
        print(f" {i * j:2} ", end="")
    print()