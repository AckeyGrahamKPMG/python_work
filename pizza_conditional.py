prompt = "\nWhat film do you want to see?"
prompt += "\nEnter 'quit' to end the program. "

active = True

while True:
    topping = input(prompt)

    if topping == 'quit':
        active = False
        
    else:
        print(f"I'd love {topping.title()} on my pizza!")