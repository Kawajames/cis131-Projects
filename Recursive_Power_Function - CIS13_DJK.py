# File Name: Recursive Power Function - CIS131
# Description: 
# Author: Dakota Kartchner 
# Date Created: 3/26/2025

def power(base, exponent):
    """
    Recursively computes the power of a base raised to a given exponent.
    
    input: 
        base - a numeric value representing the base.
        exponent - an integer (>= 1) representing the exponent.
    
    return:
        The result of base raised to the power of exponent.
    """
    # Base case: if exponent is 1, simply return the base.
    if exponent == 1:
        return base
    else:
        # Recursive step: multiply base by the result of power(base, exponent - 1)
        return base * power(base, exponent - 1)

def main():
    """
    Prompts the user for a base and an exponent, computes the power using the recursive function,
    and prints the computed result.
    """
    try:
        # Prompt the user to enter the base as a float.
        base = float(input("Enter the base: "))
        
        # Prompt the user to enter the exponent as an integer.
        exponent = int(input("Enter the exponent (an integer >= 1): "))
        
        # Validate that the exponent is at least 1.
        if exponent < 1:
            print("Error: Exponent must be an integer greater than or equal to 1.")
            return
    except ValueError:
        # Handle invalid input where conversion to float/int fails.
        print("Invalid input. Please enter numeric values.")
        return

    # Compute the power using the recursive function.
    result = power(base, exponent)
    
    # Display the computed result.
    print(f"{base}^{exponent} = {result}")

if __name__ == "__main__":
    main()
