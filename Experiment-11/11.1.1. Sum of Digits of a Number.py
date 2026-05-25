num = int(input("Enter a number: "))

# Type Content here...
digit_sum = 0
num = abs(num)  # handle negative numbers

while num > 0:
    digit_sum += num % 10
    num //= 10

print("Sum of digits:",digit_sum )
