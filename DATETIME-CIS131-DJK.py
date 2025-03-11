# File Name: DATETIME - CIS131
# Description: This programs captures two current datetime values at slightly different times and it
#              displays their individual attributes, compares them, and calculates the time difference between them.
# Author: Dakota Kartchner 
# Date Created: 3/7/2025

from datetime import datetime
import time

# Get the current date and time and store it in variable x.
x = datetime.now()
print("Datetime object x:", x)
print()  # Blank line

# Pause briefly to ensure x and y are different.
time.sleep(777)

# Get the current date and time again and store it in variable y.
y = datetime.now()
print("Datetime object y:", y)
print()

# Display data attributes of x individually.
print("Data attributes of x:")
print("Year:", x.year)
print("Month:", x.month)
print("Day:", x.day)
print("Hour:", x.hour)
print("Minute:", x.minute)
print("Second:", x.second)
print("Microsecond:", x.microsecond)
print()

# Display data attributes of y individually.
print("Data attributes of y:")
print("Year:", y.year)
print("Month:", y.month)
print("Day:", y.day)
print("Hour:", y.hour)
print("Minute:", y.minute)
print("Second:", y.second)
print("Microsecond:", y.microsecond)
print()

# Compare the datetime objects.
if x < y:
    print("x is earlier than y")
elif x > y:
    print("x is later than y")
else:
    print("x and y are the same")
print()

# Calculate and display the difference between y and x.
difference = y - x
print("Difference between y and x:", difference)
