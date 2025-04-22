def writeToFile(filename):
    data = input("Enter text to write to the file: ")
    file = open(filename, 'w')
    file.write(data+'\n')
    # with open(filename, 'w') as file:
    #     file.write(data + '\n')
    print(f"Data successfully written to {filename}.\n")

def appendToTextIntoFile(filename):
    append_data = input("Enter additional text to append: ")
    file = open(filename, 'a')
    file.write(append_data+'\n')
    # with open(filename, 'a') as file:
    #     file.write(more_data + '\n')
    print("Data successfully appended.\n")

def readContentsInFile(filename):
    try:
        print(f"Final file contents of {filename}:")
        file = open(filename,'r')
        readContents = file.read()
        print(readContents)
        # with open(filename, 'r') as file:
        #     print("Final file contents of '{filename}':")
        #     for line in file:
        #         print(line.strip())
    except FileNotFoundError:
        print(f"Error: The file {filename} does not exist.")

# Main execution
filename = 'output.txt'
writeToFile(filename)
appendToTextIntoFile(filename)
readContentsInFile(filename)
