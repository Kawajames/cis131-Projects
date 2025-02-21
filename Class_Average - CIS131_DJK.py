# File Name: Plain Text Class Average Calculator - CIS131
# Description: This script collects user grades and writes them to a file.
# Author: Dakota Kartchner 
# Date Created: 2/19/2025

#FIRST SECTION
# Opens the file "grades.txt" in write mode or creates the files if missing.
with open('grades.txt', 'w') as file:
    while True:
        # Ask user to enter a grade, convert input to an integer.
        grade = int(input('Enter grade, -1 to end: '))
        if grade == -1: #Exit.
            break
        file.write(f"{grade}\n")

print("Grades have been saved to 'grades.txt'.")