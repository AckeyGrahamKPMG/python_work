# First way to use variables an present in a sentence
# f" means f-string and uses that sentence literally, ada lovelace.
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

#calling the variable, then using the title method to capitilise each start of first and last name
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")

#combining two variables into 1, then printing out that full name variable.
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"
print(message)