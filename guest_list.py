famous = [
    'nicola sturgeon',
    'jimmy saville',
    'gary linekar'
]

print(f"Would you like to come for dinner {famous[0].title()}?")

print(f"Would you like to come for dinner {famous[1].title()}?")

print(f"Would you like to come for dinner {famous[2].title()}?")

print(f"Sadly {famous[-1].title()} cant make it tonight for dinner")
guestleft = 'gary linekar'
famous.remove(guestleft)
newgest = 'joe tortolano'
famous.append(newgest)

print(f"Would you like to come for dinner {famous[-1].title()}?")

print(f"{famous[0].title()} is still coming for dinner")

print(f"{famous[1].title()} is still coming for dinner")

print(f"{famous[2].title()} is still coming for dinner")

print(f"We've now got a bigger dining table, we'll add more guests")

famous.insert(0,'elvis presley')
famous.insert(2,'donald trump')
famous.append('mark hughes')

print(f"{famous[0].title()} is coming for dinner")
print(f"---------------------------------")

print(f"{famous[1].title()} is coming for dinner")
print(f"---------------------------------")

print(f"{famous[2].title()} is coming for dinner")
print(f"---------------------------------")

print(f"{famous[3].title()} is coming for dinner")
print(f"---------------------------------")

print(f"{famous[4].title()} is coming for dinner")
print(f"---------------------------------")

print(f"{famous[5].title()} is coming for dinner")

print(f"---------------------------------")
print(f"\nThe table is not arriving on time")

first_guest_remove = famous.pop(5)
print(f"\nSorry but guest {first_guest_remove.capitalize()} is removed due to table")
print(f"---------------------------------")

second_guest_remove = famous.pop(4)
print(f"\nSorry but guest {second_guest_remove.capitalize()} is removed due to table")
print(f"---------------------------------")

third_guest_remove = famous.pop(3)
print(f"\nSorry but guest {third_guest_remove.capitalize()} is removed due to table")
print(f"---------------------------------")

fourth_guest_remove = famous.pop(2)
print(f"\nSorry but guest {fourth_guest_remove.capitalize()} is removed due to table")
print(f"---------------------------------")

print(famous)

del famous[-2:]
print(f"Now the list is empty: {famous}")