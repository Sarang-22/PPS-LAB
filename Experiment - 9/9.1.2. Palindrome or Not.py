s = input()

# Check if string is equal to its reverse
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")
