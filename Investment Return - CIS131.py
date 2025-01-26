# File Name: Investment Return - CIS131
# Description: This program calculates the future value of a $1000 investment at a 7% annual return after 10, 20, and 30 years using the formula a = p(1 + r)^n.
# Author: Dakota Kartchner 
# Date Created: 1/25/2025

"""
a = p(1 + r)^n
where
p is the original amount invested (i.e., the principal of $1000),
r is the annual rate of return (7%),
n is the number of years (10, 20 or 30) and
a is the amount on deposit at the end of the
nth year.
"""

# Constants
principal = 1000     # Initial Investment
rate = 0.07          # Annual return rate
years = [10, 20, 30] # Calculating years

# Calculate Amounts
def calculate_return(principal, rate, years):
    return principal * (1 + rate) ** years  # (1 + rate) makes the interest positive

# Print Results
for years_value in years:
    amount = calculate_return(principal, rate, years_value)
    print("After", years_value, "years, the investment will grow to $", round(amount, 2))