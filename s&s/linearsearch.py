def linear_search(arr, n, x):
    for i in range (0,n):
        if (arr[i]==x):
            return i
        return -1

    array = [5,9,12,3]
    x=19
    solution=linear_search(arr, 0, len(array)-1, 19)

    if (solution== -1):
        print ("This value is in index", solution);
        
    else:
        print("This value is not in the array index")

    return solution

