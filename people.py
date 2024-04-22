# Exercise 6-7: People
person1 = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30,
    'city': 'New York',
}

person2 = {
    'first_name': 'Alice',
    'last_name': 'Smith',
    'age': 25,
    'city': 'Los Angeles',
}

person3 = {
    'first_name': 'Bob',
    'last_name': 'Johnson',
    'age': 35,
    'city': 'Chicago',
}

people = [person1, person2, person3]

for person in people:
    print("\nPerson:")
    for key, value in person.items():
        print(f"\t{key.title()}: {value}")

# Exercise 6-8: Pets
pet1 = {'animal': 'dog', 'owner': 'John'}
pet2 = {'animal': 'cat', 'owner': 'Alice'}
pet3 = {'animal': 'parrot', 'owner': 'Bob'}

pets = [pet1, pet2, pet3]

for pet in pets:
    print("\nPet:")
    for key, value in pet.items():
        print(f"\t{key.title()}: {value}")


# Exercise 6-9: Favorite Places
favorite_places = {
    'John': ['New York', 'Paris'],
    'Alice': ['Los Angeles', 'London'],
    'Bob': ['Chicago', 'Tokyo', 'Sydney'],
}

for person, places in favorite_places.items():
    print(f"\n{person.title()}'s Favorite Places:")
    for place in places:
        print(f"\t- {place}")


# Exercise 6-10: Favorite Numbers
favorite_numbers = {
    'John': [7, 12, 15],
    'Alice': [3, 8, 9],
    'Bob': [10, 25],
}

for person, numbers in favorite_numbers.items():
    print(f"\n{person.title()}'s Favorite Numbers:")
    for number in numbers:
        print(f"\t- {number}")


# Exercise 6-11: Cities
cities = {
    'New York': {
        'country': 'USA',
        'population': '8.4 million',
        'fact': 'The Statue of Liberty is located here.'
    },
    'London': {
        'country': 'UK',
        'population': '8.9 million',
        'fact': 'The River Thames flows through the city.'
    },
    'Tokyo': {
        'country': 'Japan',
        'population': '13.5 million',
        'fact': 'Tokyo Tower is a major landmark.'
    }
}

for city, info in cities.items():
    print(f"\nCity: {city}")
    for key, value in info.items():
        print(f"\t{key.title()}: {value}")
