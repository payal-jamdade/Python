days = ["Mon", "Tue", "Wed", "Thu", "Fri"]

schedule = [
    ["Math", "Python", "DBMS", "AI", "English"],
    ["AI", "Math", "Python", "DBMS", "AI"],
    ["DBMS", "AI", "Math", "Python", "DBMS"]
]

for i in range(3):
    print(i + 1, schedule[i])

row = int(input("Enter hour (1-3): "))
col = int(input("Enter day (1-5): "))

subject = input("Enter new subject: ")
schedule[row - 1][col - 1] = subject

print("\nUpdated Schedule:")
for row in schedule:
    print(row)