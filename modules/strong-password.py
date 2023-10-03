import random
import string
pwd1 = random.choice(string.ascii_uppercase)
pwd2 = random.choice(string.ascii_lowercase)
pwd3 = random.choice(string.digits)
pwd4 = random.choice(string.punctuation)
characters = string.ascii_letters + string.digits + string.punctuation
pwd5 = ''.join(random.choice(characters) for i in range(5,10))
password = ''.join(pwd1 + pwd2 + pwd3 + pwd4 + pwd5)
print("Random password is:", password)