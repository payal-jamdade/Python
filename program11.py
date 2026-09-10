bus = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]


def display_seats():
    print("\n========== BUS SEAT LAYOUT ==========")

    for row in range(len(bus)):
        print("Row", row + 1, end=" : ")

        for seat in range(len(bus[row])):
            if bus[row][seat] == 0:
                print(f"[{seat + 1} Available]", end=" ")
            else:
                print(f"[{seat + 1} Reserved]", end=" ")

        print()

    print("=====================================")


def reserve_seat():
    try:
        row = int(input("Enter row number (1-5): "))
        seat = int(input("Enter seat number (1-4): "))

        # Convert to list index
        row -= 1
        seat -= 1

        if row < 0 or row >= len(bus):
            print("Invalid row number!")
            return

        if seat < 0 or seat >= len(bus[row]):
            print("Invalid seat number!")
            return

        if bus[row][seat] == 1:
            print("Sorry! This seat is already reserved.")
        else:
            bus[row][seat] = 1
            print("Seat reserved successfully!")

    except ValueError:
        print("Please enter numbers only.")


def cancel_seat():
    try:
        row = int(input("Enter row number (1-5): "))
        seat = int(input("Enter seat number (1-4): "))

        row -= 1
        seat -= 1

        if row < 0 or row >= len(bus):
            print("Invalid row number!")
            return

        if seat < 0 or seat >= len(bus[row]):
            print("Invalid seat number!")
            return

        if bus[row][seat] == 0:
            print("This seat is already available.")
        else:
            bus[row][seat] = 0
            print("Reservation cancelled successfully!")

    except ValueError:
        print("Please enter numbers only.")


def main():
    while True:
        print("\n========== BUS RESERVATION SYSTEM ==========")
        print("1. Display Seat Layout")
        print("2. Reserve Seat")
        print("3. Cancel Seat")
        print("4. Exit")
        print("============================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_seats()

        elif choice == "2":
            reserve_seat()

        elif choice == "3":
            cancel_seat()

        elif choice == "4":
            print("Thank you for using the Bus Reservation System!")
            break

        else:
            print("Invalid choice! Please try again.")


# Start program
main()