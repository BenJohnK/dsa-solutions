
def isPanagram(s):
    #your code here
    if len(s) < 26:
        return False
    counter_dict = {f"{chr(i)}":0 for i in range(65, 91)}
    for x in s:
        counter_dict[x.upper()] = 1
    for k in counter_dict:
        if counter_dict[k] == 0:
            return False
    return True

print(isPanagram("CNoeIsyDkScKaTupgmBoPeSswOMfCDqoPeLAGvxsxEiwngUwUylljXYnDgdQAETqPgisLTqJRMjRTMcjaqNYKGYrshcQytCNC"))