s = "a "
for x in s:
    print(x.lower())
counter_dict = {}
for x in s:
    counter_dict[x.upper()] = 1

print(counter_dict)