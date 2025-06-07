print("Welcome to Decision Tree")

print("Is it raining?")
choice = input()
if choice == "y":
    print("Can you see the sun?")
    choice = input()
    if choice == "n":
        print("It is raining heavy")
    else:
        print("It might be drizzling")
else:
    print("The sun is out")

