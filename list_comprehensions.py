for numbers in range(1,21):
    print(numbers)



digits = [1, 2, 3000, 40000, 5, 7, 8, 90, 1000000]

print(min(digits))
print(max(digits))
print(sum(digits))

for numbers in range(2,21, 2):
    print(numbers)

# Create an empty list to store the multiples of 3
multiples_of_3 = []

# Use a for loop to generate multiples of 3 from 3 to 30
for number in range(3, 31, 3):
    multiples_of_3.append(number)

# Print each number in the list
for number in multiples_of_3:
    print(number)

# Create an empty list to store the cubes
cubes = []

# Use a for loop to calculate and append the cubes of numbers from 1 to 10
for number in range(1, 11):
    cube = number ** 3
    cubes.append(cube)

# Print the value of each cube
for cube in cubes:
    print(cube)
