def add(*args):
    sum = 0
    for arg in args:
        sum = sum + float(arg)
    return sum


def universities(**kwargs):
    for k, v in kwargs.items():
        print(f'{k} has full name as {v}')


if __name__ == '__main__':
    sum1 = add(1, 2, 3)
    sum2 = add(1, 2, 3, 4)
    print(f'{sum1}\n{sum2}')

    universities(kku="Khon Kaen University",cmu="Chiang Mai University")
    universities(cu="Chulalongkorn  University")
