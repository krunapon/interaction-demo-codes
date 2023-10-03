import random
import string

lower_char = random.choice(string.ascii_lowercase)
upper_char = random.choice(string.ascii_uppercase)
digit = random.choice(string.digits)
special_char = random.choice(string.punctuation)
mix_chars = string.ascii_letters + string.punctuation + string.digits 
free_chars = ''.join(random.choice(mix_chars) for i in range(0, 5))

password = free_chars + lower_char + upper_char + digit + special_char

print(f"password is {password}")