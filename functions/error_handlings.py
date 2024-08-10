def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero!")
        return None
    except TypeError:
        print("Error: Invalid input types!")
        return None
    else:
        print("Division successful!")
        return result
    finally:
        print("Division operation completed.")


print(divide_numbers(10, 2))  # Successful division
print(divide_numbers(10, 0))  # Division by zero
print(divide_numbers(10, "2"))  # Type error
