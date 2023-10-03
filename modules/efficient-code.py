import random
import string
import time
start = time.time()
password = random.choice(string.ascii_lowercase)
password += random.choice(string.ascii_uppercase)
for i in range(5000000):
    password += random.choice(string.ascii_letters)
end = time.time()
print(f"password is using += takes {end - start} seconds")
start = time.time()
lower_char = random.choice(string.ascii_lowercase)
upper_char = random.choice(string.ascii_uppercase)
chars = ''.join(random.choice(string.ascii_letters) for i in range(5000000))
password = ''.join(chars + lower_char + upper_char)
end = time.time()
print(f"password is using join takes {end - start} seconds")


