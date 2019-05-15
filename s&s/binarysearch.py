def binary_search (arr, l, r, x):
    if r >= l:
        mid = l + (r - l)/2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binary_search(arr, l, mid-1, x)
        else:
            return binary_search(arr, mid+1, r, x)
    else:
        return -1
    day = [5, 9, 12, 3]
    x = 3

    day_finder = binary_search(day, 0, len(day)-1, x)

    if day_finder != -1:
        print("This value is at the array index % d" % day_finder)
    else:
        print("This value is not in the array index")
