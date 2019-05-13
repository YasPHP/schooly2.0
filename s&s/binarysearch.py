# Recursive binary search. 
  
#We basically ignore half of the elements just after one comparison.

#Compare x with the middle element.
#If x matches with middle element, we return the mid index.
#Else If x is greater than the mid element, then x can only lie in right half subarray after the mid element. So we recur for right half.
#Else (x is smaller) recur for the left half.

# Returns index of x in arr if present, else -1 
def binary_search (arr, l, r, x): 
  
    # Checking base case 
    if r >= l: 
  
        mid = l + (r - l)/2
  
        # If element is present at the middle itself 
        if arr[mid] == x: 
            return mid 
          
        # If element is smaller than mid, then it can only 
        # be present in left subarray 
        elif arr[mid] > x: 
            return binary_search(arr, l, mid-1, x) 
  
        # Else the element can only be present in right subarray 
        else: 
            return binary_search(arr, mid+1, r, x)
        
    else:
        return -1

    array = [5,9,12,3]
    x=19

    solution=binary_search(arr, 0, len(array)-1, 19)

    if solution != -1:
        print ("This value is at the array index %d") % solution
        
    else:
        print("This value is not in the array index")

    return solution
