# File Name: Towers Of Hanoi.py
# Description: This script solves the Tower of Hanoi problem using a recursive
#              function with the following four parameters: the number of disks to be moved, the starting peg,
#              the destination peg, and the auxiliary peg.
# Author: Dakota Kartchner
# Date Created: 4/5/2025
# With Help from: https://www.youtube.com/watch?v=rf6uf3jNjbo&ab_channel=Reducible

# Symbol for later use: →

def towers_of_hanoi(n, start, destination, auxiliary, counter):
    """
    Recursively solves the Tower of Hanoi puzzle and prints each move with a step number.
    
    Parameters:
        n (int): Number of disks in the gaame.
        start: The peg from which the disk is moved.
        destination: The peg to which the disk is moved.
        auxiliary: The peg used as a holding area.
        counter (list): Numbers each step.
    """
    if n == 1:
        counter[0] += 1
        print(f"{counter[0]}. {start} → {destination}")
    else:
        towers_of_hanoi(n - 1, start, auxiliary, destination, counter)
        counter[0] += 1
        print(f"{counter[0]}. {start} → {destination}")
        towers_of_hanoi(n - 1, auxiliary, destination, start, counter)


def main():
    """
    Ask the user for the number of disks and displays the number of moves required
    to solve the puzzle. Defaults to 3 disks.
    """
    try:
        disks_input = input("Enter the number of disks (default is 3): ").strip()
        disks = int(disks_input) if disks_input else 3
    except ValueError:
        print("Invalid input. Please input an integer")
        return

    print(f"\nThe moves to solve Towers of Hanoi for {disks} disk{'s' if disks > 1 else ''} are:\n")
    counter = [0]  # Using a mutable list to keep track of the move count for testing
    towers_of_hanoi(disks, 1, 3, 2, counter)


if __name__ == "__main__":
    main()