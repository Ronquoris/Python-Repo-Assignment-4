# Python-Repo-Assignment-4
Task 1:
This code reads a file named "sample.txt" and prints each line if the file exists.
The first method checks for the file using "os.path.exists()" before opening it, which prevents errors.
The second method uses "try-except" to handle errors automatically if the file is missing or cannot be opened.

Task 2:
This program takes user input and writes it to a file called "output.txt", creating the file if it does not already exist.
It then asks for additional input and appends that text to the same file without deleting the previous content.
Finally, it reads the entire file and prints each line to display the saved data.
