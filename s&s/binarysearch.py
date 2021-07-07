import time
start = time.time()

def binary_search(availableDays, left, right, date):
    if right >= left:
        mid = left + (right - left)//2
        if availableDays[mid] == date:
            return mid
        elif availableDays[mid] > date:
            return binary_search(availableDays, left, mid-1, date)
        else:
            return binary_search(availableDays, mid+1, right, date)
    else:
        return None
availableDays = [3, 5, 12, 20]
print("Available June Dates:", availableDays)
chosen = int(input("Which date in June would you like to search for? "))

result = binary_search(availableDays, 0, len(availableDays)-1, chosen)
if result == None:
    print("Date is not found in the calendar list and is not available!")
else:
    print("The date " + str(chosen) + " is found at the calendar position %d" %(result))

end = time.time()
print("Code Execution Runtime:", end - start)