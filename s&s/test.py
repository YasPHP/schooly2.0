import os
import glob

prefix_path = open(r"C:\\Users\\yasme\\Desktop\\schooly\\s&s\\timing.txt")
prefix_path = open('timing.txt', mode='r', encoding='utf-8')
file_array = [f for f in os.listdir(prefix_path) if f.endswith('.txt')]
file_array.sort() # file is sorted list

file_array = [os.path.join(prefix_path, name) for name in file_array]

for filename in file_array:
     log = open(filename, 'r')
