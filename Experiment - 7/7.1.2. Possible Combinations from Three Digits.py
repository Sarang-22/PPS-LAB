# Read input digits
a, b, c = input().split()

# Print all permutations
print(a + b + c)
print(a + c + b)
print(b + a + c)
print(b + c + a)
print(c + a + b)
print(c + b + a)
