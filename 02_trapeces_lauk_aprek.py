"""
Trapeces laukuma aprēķināšana. 
"""

a = float(input("1. pamata garums: "))
b = float(input("2. pamata garums: "))
h = float(input("Trapeces augstums: "))

laukums = ((a + b) / 2) * h
print(f"Trapeces laukums ir: {laukums}")