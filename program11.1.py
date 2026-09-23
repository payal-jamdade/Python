seats = [["O", "O", "O"],
         ["O", "O", "O"],
         ["O", "O", "O"]]

for row in seats:
    print(row)

r = int(input("Enter row (1-3): "))
c = int(input("Enter column (1-3): "))

if seats[r-1][c-1] == "O":
    seats[r-1][c-1] = "X"
    print("Seat Reserved!")
else:
    print("Seat already reserved!")

for row in seats:
    print(row)