from get_int import get_num

def div(n1: int, n2: int):
    """Divides one integer with the other integer that is not zero.

        The result of division is an integer. If the divisor is zero,
        then the method return None

        Parameters
        ----------
        n1 : integer
            A divisor

        n2 : integer
            A dividend

        Raises
        ------
        NotImplementedError
            If no sound is set for the animal or passed in as a
            parameter.
        """
    if n2 != 0:
        return round(n1 / n2)
    else:
        return None

if (__name__ == '__main__'):
    in1 = get_num()
    in2 = get_num()
    print("{} / {} = {}".format(in1, in2, div(in1, in2)))
