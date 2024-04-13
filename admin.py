usernames = ['gary', 'valerie', 'ross','peter','john', 'admin']

for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    elif username != 'admin':
        print(f"Hello {username} thank you for logging in again.")
    

available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
     if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
     else:
        print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")

numbers = list(range(1, 10))

for number in numbers:
    if number == 1:
        print(f"{number}st")
    elif number == 2:
        print(f"{number}nd")
    elif number == 3:
        print(f"{number}rd")
    if number == 4:
        print(f"{number}th")
    elif number == 5:
        print(f"{number}th")
    elif number == 6:
        print(f"{number}th")
    if number == 7:
        print(f"{number}th")
    elif number == 8:
        print(f"{number}th")
    elif number == 9:
        print(f"{number}th")
    elif number == 10:
        print(f"{number}th")
