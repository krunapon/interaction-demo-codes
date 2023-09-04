def check_str(arg):
    if str(arg).lower() == "fail":
        raise ValueError("Fail")
    return arg


