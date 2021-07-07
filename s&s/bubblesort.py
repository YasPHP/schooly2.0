import time
start = time.time()

def bubble_sort(dates):
    valueExchanges = True
    nextNum = len(dates)-1
    while nextNum > 0 and valueExchanges:
        valueExchanges = False
        for i in range(nextNum):
            if dates[i] > dates[i+1]:
                valueExchanges = True
                temporary = dates[i]
                dates[i] = dates[i+1]
                dates[i+1] = temporary
        nextNum = nextNum-1

dates = [53, 12, 1, 879, 34]
bubble_sort(dates)
print(dates)

end = time.time()
print("Code Execution Runtime:", end - start)