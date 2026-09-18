print("Star Pattern:")
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

print("\nNumber Pattern:")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("\nPyramid Pattern:")
rows = 5

for i in range(rows):
    for j in range(rows - i - 1):
        print(" ", end="")
    for k in range(2 * i + 1):
        print("*", end="")
    print()
