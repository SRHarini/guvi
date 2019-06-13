get=input()
if any(char.isalpha() for char in get):
    print("No")
elif any(char.isdigit() for char in get):
    print("yes")
