import random
import string

a = int(input('How many characters should the password be? The minimum is 6 characters.\n'))
uppercase = list(string.ascii_uppercase)
lowercase = list(string.ascii_lowercase)
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_character = ['!', '@', '#', '$', '%', '&', '*']
password_list = [random.choice(uppercase), random.choice(lowercase), random.choice(lowercase), random.choice(number),
                 random.choice(number), random.choice(special_character)]
b = ''
for i in range(len(password_list)):
    y = random.randrange(len(password_list))
    b = b+password_list[i]

if a > 6:
    x = a-6
    for i in range(x):
        y = random.randrange(len(password_list))
        list1 = [random.choice(uppercase), random.choice(lowercase), random.choice(lowercase), random.choice(number),
                 random.choice(special_character), random.choice(number)]
        b = b+list1[y]

if a > 6 or a == 6:
    sr = ''.join(random.sample(b, len(b)))
    print(sr)
else:
    print('Minimum characters is 6. Please try again.')
