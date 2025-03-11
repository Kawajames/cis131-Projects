# File Name: Class Fraction - CIS131
# Description: This code does arithmetic with fractions and complex numbers.
# Author: Dakota Kartchner 
# Date Created: 3/9/2025

from fractions import Fraction

# Fraction Section
# Define two fractions.
frac1 = Fraction(3, 4)  
frac2 = Fraction(2, 4)

# Adding two Fractions.
add_frac = frac1 + frac2

# Subtracting two Fractions.
sub_frac = frac1 - frac2

# Multiplying two Fractions.
mult_frac = frac1 * frac2

# Dividing two Fractions.
div_frac = frac1 / frac2

# Printing the fractions in the form a/b.
print("Fraction 1:", frac1)
print("Fraction 2:", frac2)
print()

print("Operations with Fractions:")
print("Addition:", add_frac)
print("Subtraction:", sub_frac)
print("Multiplication:", mult_frac)
print("Division:", div_frac)
print()

# Converting fractions to floating-point numbers.
print("Floating-point representations:")
print("Fraction 1 as float:", float(frac1))
print("Fraction 2 as float:", float(frac2))
print()

# Complex Numbers Section
# Define two complex numbers.
c1 = complex(2, 3)
c2 = complex(1, -1)

# Adding two complex numbers.
sum_complex = c1 + c2

# Subtracting two complex numbers.
diff_complex = c1 - c2

print("Complex Numbers:")
print("Complex number 1:", c1)
print("Complex number 2:", c2)
print()

print("Operations with Complex Numbers:")
print("Addition:", sum_complex)
print("Subtraction:", diff_complex)
print()

# Getting the real and imaginary parts.
print("Real and Imaginary Parts:")
print("Real part of c1:", c1.real)
print("Imaginary part of c1:", c1.imag)
print("Real part of c2:", c2.real)
print("Imaginary part of c2:", c2.imag)