from get_int import get_num

def sub(n1: int, n2: int) -> int:
    return n1 - n2

if (__name__ == '__main__'):
    in1 = get_num()
    in2 = get_num()
    print("{} - {} = {}".format(in1, in2, sub(in1, in2)))
