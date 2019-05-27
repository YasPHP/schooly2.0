# Open a file
fileName = input("Enter the file Name:")
inputFile = open(r'C:\timing.txt')
lineList = inputFile.readlines()
lineList.sort()
print('The input in alphabetical order below :')
for line in  lineList:
    print(line)