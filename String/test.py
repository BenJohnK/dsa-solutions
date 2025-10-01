s = "ana"
for x in s:
    print(x.upper())
counter_dict = {}
for x in s:
    counter_dict[x.upper()] = 1

print(counter_dict)