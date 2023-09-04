months = ("January", "February")
days = (31, 28)
dicts = {}
dicts[months[0]] = days[0]
print(dicts[months[0]])
for m_d in zip(months,days):
    print(m_d)
months_days = dict((("January", 31), ("February", 28)))
print(months_days)
print(months_days["January"])

