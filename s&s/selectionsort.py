#The selection sort algorithm sorts an array by repeatedly finding the minimum 
# element (considering ascending order) from unsorted part and putting it at the 
# beginning. The algorithm maintains two subarrays in a given array.
# 1) The subarray which is already sorted.
# 2) Remaining subarray which is unsorted.
#In every iteration of selection sort, the minimum element (considering ascending order) 
# from the unsorted subarray is picked and moved to the sorted subarray.

def selection_sort(notes):
    for i in range (0, len(notes) - 1):
        minIndex = i
        for j in range (i+1, len(notes)):
            if notes[j] < notes[minIndex]:
                minIndex=j
        if minIndex != i:
            notes[i], notes[minIndex] = notes[minIndex], notes[i]

        with open('notes.txt', 'r') as f:
            notes = [line.strip() for line in f]