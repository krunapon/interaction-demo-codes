import sys

def magic(x, y):
    return x + y * 2

x = int(sys.argv[1])
y = int(sys.argv[2])

answer = magic(x, y)
print('The answer is: {}'.format(answer))
