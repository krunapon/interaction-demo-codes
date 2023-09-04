def headline(text, align=True):
    if align:
        return f"{text.title()}\n{'-' * len(text)}"
    else:
        return f"{text.title()}".center(50, "o")

print(headline("python type checking"))
print(headline("python type checking", align=False))
