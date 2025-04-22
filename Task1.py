
def checkFileIsExist(filename):
    try:
    	file = open(filename,'r')
    	readMyfile = file.read()
    	print(readMyfile)
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")


checkFileIsExist('sample1.txt')

