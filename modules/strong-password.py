import random
import string

upper = random.choice(string.ascii_uppercase)
lower = random.choice(string.ascii_lowercase)
digit = random.choice(string.digits)
punct = random.choice(string.punctuation)
characters = string.ascii_letters + string.digits + string.punctuation
chars = ''.join(random.choice(characters) for i in range(5,10))
password = ''.join(upper + lower + digit + punct + chars)
print("Random password is:", password)
password = ''.join(random.sample(password, len(password)))
print("Random password is:", password)