rivers = {
    'nile' : 'egypt',
    'clyde' : 'glasgow',
    'siene' : 'paris'
    }

print("The following rivers have been mentioned:")
for river, city in rivers.items():
    print(f"The river {river.title()} is from the city {city.title()}")
