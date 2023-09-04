# Write a program which keeps prompting the user to guess a word. 
# The user is allowed up to ten guesses – write your code in such a 
# way that the secret word and the number of allowed guesses are 
# easy to change. Print messages to give the user feedback.
secret = "kku"
count = 0
MAX_NUM_GUESSES = 3 
num_guesses_left = MAX_NUM_GUESSES
while num_guesses_left:
     word = input("Enter a word:")
     num_guesses_left = num_guesses_left - 1
     if word == secret:
        print("Congrats that you can guess the secret word correctly")
        exit()
     else:
        print("Incorrect! You have %d guesses left." % num_guesses_left)
print("Thanks for trying, but the secret word is actullay kku")

