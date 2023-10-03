import random
import string

# getting a lowercase letter
letters1 = string.ascii_lowercase
lower_char1 = ''.join(random.choice(letters1) for i in range(1))

# getting an uppercase letter
letters2 = string.ascii_uppercase
upper_char1 = ''.join(random.choice(letters2) for i in range(1))

lower_char2 = random.choice(string.ascii_lowercase)
upper_char2 = random.choice(string.ascii_uppercase)
print(f"lower_char: {lower_char1} {lower_char2}" )
print(f"upper_char: {upper_char1} {upper_char2}" )