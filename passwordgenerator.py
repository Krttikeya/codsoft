import random
import string

list1 = list(string.ascii_uppercase)
list2 = list(string.ascii_lowercase)
list3 = list(string.digits)
list4 = list(string.punctuation)

length = int(input("How many characters do you want in your password? "))

random.shuffle(list1)
random.shuffle(list2)
random.shuffle(list3)
random.shuffle(list4)

strength = str(input("Choose password strength: (strong, medium, weak) "))

if strength == "strong" or strength == "Strong":
    punc, upper, lower, digits = True, True, True, True
elif strength == "medium" or strength == "medium":
    punc, upper, lower, digits = False, True, True, True
elif strength == "weak" or strength == "weak":
    punc, upper, lower, digits = False, False, True, True
else:
    print("Invalid strength choice. Defaulting to strong.")
    punc, upper, lower, digits = True, True, True, True

password = ""

while len(password) < length:
    if upper and len(password) < length:
        password += random.choice(list1)
    if lower and len(password) < length:
        password += random.choice(list2)
    if digits and len(password) < length:
        password += random.choice(list3)
    if punc and len(password) < length:
        password += random.choice(list4)

# Shuffle the password to mix the characters
password = ''.join(random.sample(password, len(password)))
print(password)
