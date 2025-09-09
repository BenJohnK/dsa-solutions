a = [10, 5, 30]
for i in range(1, len(a)):
    if a[i] < a[i-1]:
        print("No")
        break
else:
    print("Yes")