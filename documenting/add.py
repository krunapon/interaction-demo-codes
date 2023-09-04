from get_int import get_int

def add(n1: int, n2: int) -> int:
    """Add two integers and return the result as an integer

        Parameters
        ----------
            n1 : integer
                the first integer
            n2 : integer
                the second integer

        Returns
        -------
            result: The result of adding two integer arguments

    """
    return n1 + n2

if (__name__ == '__main__'):
    in1 = get_int()
    in2 = get_int()
    print("{} + {} = {}".format(in1, in2, add(in1, in2)))
