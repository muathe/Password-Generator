import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")

l = int(input("Please enter the amount of letters you would like to generate\n"))

n = int(input("Please enter the amount of numbers you would like to generate\n"))

s = int(input("Please enter the amount of symbols you would like to generate\n"))

password_list = []

for pw in range(0, l):
    password_list += random.choice(letters)

for pw in range(0, n):
    password_list += random.choice(numbers)
    
for pw in range(0, s):
    password_list += random.choice(symbols)
    
print(password_list)
random.shuffle(password_list)

password = ""
for pw in password_list:
    password += pw
print(f"Your password is {password}")


#shuffle the deck x27
