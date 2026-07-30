day = int(input("Enter the number of days in the month :"))
monthly_total = 0

for day in range(1, day + 1):
    print("\nDay",day)
    daily_total = 0
    
    while True:
        expense = float(input("Enter grocery expense :$"))
        daily_total += expense
        choice = input("Add another expense for this day? (yes/no):").lower()
        
        if choice == "no":
            break
        print("Total expense fpr Day", day,"=$, daily_total")
        
        monthly_total += daily_total
        
        print("\n*************** MONTHLY GROCERY EXPENSE REPORT *****************\n")
        print("Total Grocery Expense =$",monthly_total)
        
            
        
            