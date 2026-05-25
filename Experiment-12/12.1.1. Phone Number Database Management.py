# Number of operations
n = int(input())

# Dictionary to store contacts
contacts = {}

for _ in range(n):
    operation = input().split()
    
    if operation[0] == "ADD":
        name = operation[1]
        phone = operation[2]
        contacts[name] = phone   # Add or update
    
    elif operation[0] == "REMOVE":
        name = operation[1]
        if name in contacts:
            del contacts[name]   # Remove if exists
    
    elif operation[0] == "DISPLAY":
        if not contacts:
            print("No contacts")
        else:
            for name in sorted(contacts):
                print(f"{name}: {contacts[name]}")
