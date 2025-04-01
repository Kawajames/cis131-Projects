# File Name: Recursive Fibonacci Modification - CIS131
# Description: 
# Author: Dakota Kartchner 
# Date Created: 3/29/2025

# Global variable to count the number of function calls
call_count = 0

def fibonacci(n):
    """
    action: Recursively computes the nth Fibonacci number while incrementing a global call counter for every function call.
    
    input: 
        n - an integer representing the position in the Fibonacci sequence to compute.
        
    output: 
        (None) - This function does not print output by itself.
        
    return: 
        The nth Fibonacci number.
    """
    global call_count
    # Increment the counter each time the function is invoked
    call_count += 1

    # Check the base cases: when n is 0 or 1, return n directly.
    if n in (0, 1):
        return n
    else:
        # Recursively calculate the Fibonacci number by summing the two preceding values
        return fibonacci(n - 1) + fibonacci(n - 2)

def test_fibonacci(n):
    """
    action: Resets the global call counter, computes the nth Fibonacci number using the recursive function,
            and prints the result along with the total number of function calls.

    input: 
        n - an integer representing the position in the Fibonacci sequence to test.
        
    output: 
        Prints the computed Fibonacci number and the total function calls.
        
    return: 
        None.
    """
    global call_count
    # Reset the counter before starting a new computation
    call_count = 0
    
    # Compute the Fibonacci number for the given n
    result = fibonacci(n)
    
    # Print the result and the total number of calls made during the computation
    print(f"fibonacci({n}) = {result} with {call_count} function calls.")

# Test and display the number of function calls for fibonacci(10), fibonacci(20), and fibonacci(30)
test_fibonacci(10)  # Expected: 55 with approximately 177 calls
test_fibonacci(20)  # Expected: 6765 with approximately 21891 calls
test_fibonacci(30)  # Expected: 832040 with approximately 2692537 calls
