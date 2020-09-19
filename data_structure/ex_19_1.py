user_info = {
    'apple' : 'red',
    'lettuce' : 'green',
    'lemon' : 'yellow',
    'orange' : 'orange'

}
user_name = input("please enter your user name: ")
password = input("please enter your password: ")


if user_name in user_info:
    login = user_info[user_name]
    if password == login:
        print("welcome")
    else:
        print("go away")

