fruit = 'apple'
print("is the fruit == 'apple'? I predict it's true.")
print(fruit == 'apple')

fruit = 'orange'
print("is the fruit == 'apple'? I predict it's false.")
print(fruit == 'apple')

fruit = 'apple'
print("is the fruit in lower case == 'apple'? I predict it's true.")
print(fruit.upper == 'apple')

num1 = 10
num2 = 5

print("Equality test:", num1 == num2)  # False
print("Inequality test:", num1 != num2)  # True
print("Greater than test:", num1 > num2)  # True
print("Less than test:", num1 < num2)  # False
print("Greater than or equal to test:", num1 >= num2)  # True
print("Less than or equal to test:", num1 <= num2)  # False

# Tests using the and keyword and the or keyword
bool1 = True
bool2 = False

print("And keyword test:", bool1 and bool2)  # False
print("Or keyword test:", bool1 or bool2)  # True

# Test whether an item is in a list
my_list = [1, 2, 3, 4, 5]

print("Item in list test:", 3 in my_list)  # True

# Test whether an item is not in a list
print("Item not in list test:", 6 not in my_list)  # True