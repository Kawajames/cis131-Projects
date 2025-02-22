# Telephone Number Word Generator - CIS131
# Description: This program generates all possible seven-letter word combinations corresponding to a given (And then outputs the results to a text file)
# seven-digit phone number and writes the output to a text file.
# Author: Dakota Kartchner
# Date Created: 2/5/2025

# Map digits to corresponding letters based on a telephone keypad.
digit_map = {
    '2': 'ABC', '3': 'DEF', '4': 'GHI', '5': 'JKL',
    '6': 'MNO', '7': 'PRS', '8': 'TUV', '9': 'WXY'
}

# Generate letter combinations recursively.
def generate_combinations(prefix, remaining_digits, results):
    if not remaining_digits:
        results.append(prefix)  # Add the complete word to results.
        return
    for letter in digit_map[remaining_digits[0]]:
        generate_combinations(prefix + letter, remaining_digits[1:], results)

# Validate input and generate the words.
def number_to_words(phone_number):
    if len(phone_number) != 7 or any(d in phone_number for d in '01'):
        return "Invalid input"
    
    results = []
    generate_combinations("", phone_number, results)
    return results

# Get user input.
phone_number = input("Enter a 7-digit phone number (without 0 or 1): ")
words = number_to_words(phone_number)

# Display results and write output to a text file.
if words != "Invalid input":
    output_filename = "telephone_number_words.txt"
    with open(output_filename, 'w') as outfile:
        outfile.write(f"Total combinations: {len(words)}\n")
        outfile.write("Sample words (first 10): " + ", ".join(words[:10]) + "\n\n")
        outfile.write("All combinations:\n")
        for word in words:
            outfile.write(word + "\n")
    print(f"Output written to {output_filename}.")
else:
    print(words)