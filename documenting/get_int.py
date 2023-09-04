def get_int() -> int:
    """Keep asking an integer from a user until the user enters a valid integer

        Returns
        -------
            int: Returning a valid integer entered by a user

        Raises
        ------
            ValueError
                If a user enters text that is not an integer
        """
    while True:
        try:
            num = int(input("Please enter an integer:"))
            return num
        except ValueError:
            print("Please enter only an integer")

if (__name__ == '__main__'):
    print(get_int())
    help(get_int)
