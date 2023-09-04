print('Writing to file test.txt')
with open('test.txt', 'a') as f:
    value = ('the answer', 88)
    s = str(value)
    f.write(s)
f.close()
print('Finish writing file test.txt')
