text = input()

# Initialize empty string
result = ""

# Loop through each character
for ch in text:
    if ch.isalnum() or ch == " ":
        result += ch

# Print result
print(result)
