while True:
    # Ask the user for their age
    age = input("Please enter your age (or 'q' to quit): ")

    # Check if the user wants to quit
    if age.lower() == 'q':
        print("Goodbye!")
        break

    # Convert age to an integer
    age = int(age)

    # Determine the cost of the movie ticket based on the age
    if age < 3:
        ticket_price = 0
    elif 3 <= age <= 12:
        ticket_price = 10
    else:
        ticket_price = 15

    # Display the cost of the movie ticket to the user
    print(f"The cost of your movie ticket is ${ticket_price}.")
