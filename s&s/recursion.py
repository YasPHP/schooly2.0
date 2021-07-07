def BubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
       exchanges = False
       for i in range(passnum):
           if alist[i] > alist[i+1]:
               exchanges = True
               temp = alist[i]
               alist[i] = alist[i+1]
               alist[i+1] = temp
       passnum = passnum-1

alist = [20, 30, 40, 90, 50, 60, 70, 80, 100, 110]
print(alist)
picked_number = input("Which number do you want?")
picked_number = True

for i in range (int(picked_number), alist)
    if picked_number == False:
        print("Thus value is not in the array index")
    else:
        BubbleSort(alist)
        print(alist)

