def linear_search(day, n, x):
    for i in range(0, n):
        if day[i] == x:
            return i
        return -1

    day = [5, 9, 12, 3]
    x = 3
    day_finder = linear_search(day, 0, len(day)-1, x)

    if day_finder == -1:
        print ("This value is in index", day_finder)

    else:
        print("This value is not in the array index")
