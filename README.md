# ASSIGNMENT4

### Task 1: `checkFileIsExist(filename)`

This program attempts to check if a file exists by:
1. **Opening the file** in read mode (`'r'`).
2. If the file exists, it **reads and prints** the content of the file.
3. If the file does not exist, it **catches the error** and prints a message saying that the file could not be found.

**How it works:**
- The program tries to open the file `sample1.txt` and prints its content.
- If the file doesn't exist, it informs the user with an error message.

### Task 2: Writing, Appending, and Reading from a File

This program includes three functions to:
1. **Write to a file**: 
   - Prompts the user to **enter text**.
   - Opens the file `output.txt` in **write mode (`'w'`)**, meaning the file is overwritten with the new data.
   - The data entered by the user is **written to the file** and a success message is shown.

2. **Append to a file**:
   - After writing, the program prompts the user to **enter additional text**.
   - The program then opens the same file in **append mode (`'a'`)** and **adds** the new data at the end of the existing content.
   - It prints a success message when the new data is appended.

3. **Read and display the file contents**:
   - The program then opens the file in **read mode (`'r'`)** to display the entire content of the file after the writing and appending.
   - If the file does not exist at this point, an error message is displayed instead of attempting to read the non-existent file.

**How it works:**
- First, you **write** some text to `output.txt` (overwriting any previous content).
- Then, you **append** additional text to the same file.
- Finally, the program reads the **final content** of the file and displays it.

**Example of what happens:**
1. Write `"Hello, Python!"` to the file.
2. Append `"Learning file handling in Python."` to the same file.
3. The program then displays both `"Hello, Python!"` and `"Learning file handling in Python."` as the final content of the file.
