def selection_sort(notes):
    for i in range(0, len(notes) - 1):
        min_index = i
        for j in range(i+1, len(notes)):
            if notes[j] < notes[min_index]:
                min_index = j
        if min_index != i:
            notes[i], notes[min_index] = notes[min_index], notes[i]

        with open('notes.txt', 'r') as f:
            notes = [line.strip() for line in f]
