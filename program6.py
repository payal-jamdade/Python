print("\n*************** SQUARE STAR PATTERN ****************\n")

rows = 5

for i in range(rows):
    for j in range(rows):
        print("*", end=" ")
    print()

print("\n+++++++++++++++++++++++ INVOICE PATTERN ++++++++++++++++++++++++++++++++\n")

rows = 5
cols = 20

for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

print("\n################### RIGHT TRIANGLE STAR PATTERN ###########################\n")

rows = 5

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()

print("\n !!!!!!!!!!!!!!!!!!!!!!!! NUMBER TRIANGLE PATTERN !!!!!!!!!!!!!!!!!!!!!!!!!!\n")

for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()