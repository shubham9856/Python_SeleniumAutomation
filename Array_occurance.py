arr = [1, 4, 1, 3, 3, 7, 1, 2, 5]

dup = set()

for i in range(len(arr)):
    if arr[i] in dup:
        continue
    else:
        dup.add(arr[i])
    count = 0
    for f in range(len(arr)):
        if arr[i] == arr[f]:
            count = count + 1

    print(f"count of {arr[i]} is : ", count)

