# Bubble Sort works by repeatedly swapping the adjacent elements/values if they are in wrong order.
def bubbleSort(notes):
    n = len(notes)
    for i in range (0, n-1):
        for j in range(0, n -1 -i):
            if notes[j] > notes[i+1]:
                notes[j], notes[j+1] = notes[j+1], notes[j]
    with open('notes.txt', 'r') as f:
        notes = [line.strip() for line in f]
    
    return(notes)
    print(notes)