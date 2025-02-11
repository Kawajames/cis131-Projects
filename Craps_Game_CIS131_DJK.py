# File Name: Analyzing The Game of Craps - CIS131
# Description: This script simulates 1,000,000 craps games and tracks wins and losses for each roll. It the calculated the total wins and losses.
# Author: Dakota Kartchner
# Date Created: 2/6/2025

import random # Calls random.randint to generate random numbers.

def roll_dice():
    """Simulate a six sides dice roll and return the sum of both"""
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1 + die2

def play_craps():
    """Simulate one game of craps and return the number of rolls and whether the player won."""
    rolls = 1
    first_roll = roll_dice()
    
    # Return Boolean based on outcome.
    if first_roll in (7, 11):
        return rolls, True  # Win on first roll.
    elif first_roll in (2, 3, 12):
        return rolls, False  # Lose on first roll.
    
    # Otherwise, establish a point.
    point = first_roll
    while True:
        rolls += 1
        roll = roll_dice()
        if roll == point:
            return rolls, True  # Win by making the point.
        elif roll == 7:
            return rolls, False  # Lose if 7 is rolled.

def simulate_craps_games(num_games=1_000_000):
    print("Simulation started...")  # Trying to fix and issue, this checks if its running.
    """Simulate one million games of craps and analyze results."""
    # Win and Loss Dictionary.
    wins = {}
    losses = {}
    # Tracks overall wins and Losses.
    total_wins = 0
    total_losses = 0
    
    # Runs the play_craps() function and records outcome.
    for _ in range(num_games):
        rolls, won = play_craps()
        if won:
            total_wins += 1
            wins[rolls] = wins.get(rolls, 0) + 1
        else:
            total_losses += 1
            losses[rolls] = losses.get(rolls, 0) + 1
    
    # Calculated Percentage
    total_games = total_wins + total_losses
    win_percentage = (total_wins / total_games) * 100
    loss_percentage = (total_losses / total_games) * 100
    
    print(f"Percentage of wins: {win_percentage:.1f}%")
    print(f"Percentage of losses: {loss_percentage:.1f}%")
    print("\nPercentage of wins/losses based on total number of rolls")
    print("% Resolved        Cumulative %")
    print("Rolls   on this roll   of games resolved")
    
    resolved_per_roll = {}
    for rolls in set(wins.keys()).union(set(losses.keys())):
        resolved_per_roll[rolls] = wins.get(rolls, 0) + losses.get(rolls, 0)
    
    sorted_rolls = sorted(resolved_per_roll.keys())
    cumulative_percentage = 0
    
    for rolls in sorted_rolls:
        percentage_resolved = (resolved_per_roll[rolls] / total_games) * 100
        cumulative_percentage += percentage_resolved
        print(f"{rolls:<7} {percentage_resolved:.2f}% {cumulative_percentage:.2f}%")

simulate_craps_games()