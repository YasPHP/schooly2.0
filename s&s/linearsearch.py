import time
start = time.time()

def linear_search(availableDays, date):
    for i in range(len(availableDays)):
        if availableDays[i] == date:
            return i
    return None

availableDays = [1, 7, 6, 5, 8]
print("Available June Dates:", availableDays)
chosen = int(input("Which date in June would you like to search for? "))

result = linear_search(availableDays, chosen)
if result== None:
     print("Date is not found in the calendar list and is not available!")
else:
     print( "The date " + str(chosen) + " is found at the calendar position %d" %(result))

end = time.time()
print("Code Execution Runtime:", end - start)