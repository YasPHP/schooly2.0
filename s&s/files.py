class Filestuff():
    def __init__(self):



  def opening():
    f_input = open('notes.txt', 'r')
    file = f_input.readlines()  #reads all files to create list called file
    f_input.close() #closes file when reading complete

    for line in file:
      print(line)

  def writing():
    output_string = 'This is line 1\n'
    output_string += 'This is line 2\n'

    f_output = open('notes.txt', 'a')       #appends to file
    f_output.write(output_string)           #outputs string to txt file
    f_output.close()







    def main():

    file = open("notes.txt", "r")
    if file.mode == "r":
        contents = file.read()
        print(contents)

if __name__ == "__main__":
    main()


def main2():

