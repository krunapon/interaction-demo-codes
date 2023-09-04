def avg(marks):
    assert len(marks) != 0,"List is empty."
    return sum(marks)/len(marks)

mark1 = [55,88,78,90,79]
print("Average of mark1:",avg(mark1))

mark2 = []
print("Average of mark2:",avg(mark2))
