num_list = [500, 600, 700]
alpha_list = ['x', 'y', 'z']


def nested_loop():
    for number in num_list:
        print(number)
        for letter in alpha_list:
            print(letter)


nested_loop()

