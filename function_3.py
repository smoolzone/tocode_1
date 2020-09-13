
while True:
    try :
        print("Please Write something\n")
        user_input = input()
        print(f"You written : {user_input[::-1]}")
    except ValueError:
        print('Plz write somethings')
