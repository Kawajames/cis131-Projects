# File Name: Telephone Number Word Generator - CIS131
# Description: This program generates all possible seven letter word combinations corresponding to a given seven digit phone number
# Author: Dakota Kartchner
# Date Created: 2/5/2025

digit_map = {
    '2': 'ABC', '3': 'DEF', '4': 'GHI', '5': 'JKL',
    '6': 'MNO', '7': 'PRS', '8': 'TUV', '9': 'WXY'
}

def generate_combinations(prefix, remaining_digits, results):
    if not remaining_digits:
        results.append(prefix)
        return
    
    for letter in digit_map[remaining_digits[0]]:
        generate_combinations(prefix + letter, remaining_digits[1:], results)

def number_to_words(phone_number):
    if len(phone_number) != 7 or any(d in phone_number for d in '01'):
        return "Invalid input"
    
    results = []
    generate_combinations("", phone_number, results)
    return results

phone_number = input("Enter a 7-digit phone number (without 0 or 1): ")
words = number_to_words(phone_number)
if words != "Invalid input":
    print(f"Total combinations: {len(words)}")
    print("Sample words:", words[:10])
else:
    print(words)
