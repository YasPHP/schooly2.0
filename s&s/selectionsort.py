import time
start = time.time()

def selection_sort(dates):
   for chosen in range(len(dates)-1, 0, -1):
       maxPosition = 0
       for location in range(1, chosen+1):
           if dates[location] > dates[maxPosition]:
               maxPosition = location

       temporary = dates[chosen]
       dates[chosen] = dates[maxPosition]
       dates[maxPosition] = temporary

dates = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selection_sort(dates)
print(dates)

end = time.time()
print("Code Execution Runtime:", end - start)