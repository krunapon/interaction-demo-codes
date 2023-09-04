my_action = input("Enter your action (r,c):")
my_string = input("Enter your string:")
def reverse(string):
    print("'%s' reversed is '%s'." % (string, string[::-1]))

def capitalise(string):
    print("'%s' capitalised is '%s'." % (string, string.upper()))

ACTIONS = {
    "r": reverse, # use the function name without brackets to refer to the function without calling it
    "c": capitalise,
}

my_function = ACTIONS[my_action] # now we retrieve the function
my_function(my_string) # and now we call it
