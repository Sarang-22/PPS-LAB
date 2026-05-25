# Read input string
s = input()

# Define vowels
vowels = "aeiouAEIOU"

# Count vowels
count = 0
for char in s:
    if char in vowels:
        count += 1

# Print result
print(count)
