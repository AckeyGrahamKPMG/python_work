person1 = {
    'firstname' : 'Elaine',
    'lastname' : 'Graham',
    'Age' : '46',
    'City' : 'Glasgow'
}
firstname = person1['firstname']
print(f"First name is {firstname}")

lastname = person1['lastname']
print(f"Last name is {lastname}")

age = person1['Age']
print(f"Age is {age}")

City = person1['City']
print(f"City of residence is {City}")

luckynumber = {
    'Tom' : '1',
    'Dick': '12',
    'Harry': '67',
    'Rod' :'45',
    'Jane' : '13',
}

tom = luckynumber['Tom']
print(f"tom's number is {tom}")

dick = luckynumber['Dick']
print(f"dick's number is {dick}")

harry = luckynumber['Harry']
print(f"harry's number is {harry}")

jane = luckynumber['Jane']
print(f"jane's number is {jane}")

rod = luckynumber['Rod']
print(f"Rod's number is {rod}")

# Creating the glossary
glossary = {
    "variable": "A placeholder for storing data values.",
    "function": "A block of organized, reusable code that performs a specific task.",
    "loop": "A control flow statement for executing a block of code repeatedly.",
    "list": "A collection which is ordered and changeable. Allows duplicate members.",
    "dictionary": "A collection which is unordered, changeable, and indexed. No duplicate members."
}

# Printing each word and its meaning
for word, meaning in glossary.items():
    print(word.capitalize() + ":")
    print(meaning + "\n")
