def election_winner(arr):
    # Your code here
    # return the name of the winning candidate and the votes he recieved
    counter = {}
    max_count = 0
    winner = None
    for x in arr:
        counter[x] = counter.get(x, 0) + 1
    for k in counter:
        if counter[k] > max_count:
            max_count = counter[k]
            winner = k
        elif counter[k] == max_count:
            if k < winner:
                winner = k
        else:
            continue
    return [winner, str(max_count)]

print(election_winner(["john","johnny","jackie"]))