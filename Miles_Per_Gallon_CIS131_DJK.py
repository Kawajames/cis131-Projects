# File Name: Miles Per Galon - CIS131
# Description: This program calculates miles per gallon (MPG) for each tank of gas.
# Author: Dakota Kartchner 
# Date Created: 1/29/2025

total_miles = 0
total_gallons = 0

while True:
    gallons = float(input("Enter the gallons used: "))  # Ask user for gallons used
    if gallons == -1: # Check for sentinel value to exit loop
        break # Exit the loop if the sentinel value is entered
    
    miles = float(input("Enter the miles driven: ")) # Ask user for miles driven
    mpg = miles / gallons # Calculates the miles per gallon for this tank
    print("The miles/gallon for this tank was", mpg) # Print the MPG for this tank
    
    # Accumulate totals
    total_miles += miles
    total_gallons += gallons

if total_gallons > 0:
    overall_mpg = total_miles / total_gallons # Calculates the overall MPG
    print("The overall average miles/gallon was", round(overall_mpg, 6)) # Displays the overall MPG
else:
    print("No data entered.") # Error if no valid data is entered