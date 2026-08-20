transactions = []

for i in range(5):
    amount = float(input(f"Enter transaction amount {i + 1}: "))
    transactions.append(amount)

largest = max(transactions)
average = sum(transactions) / len(transactions)

print("\n----- Transaction Summary -----")
print("Transaction Values:", transactions)
print(f"Largest Transaction: {largest:.2f}")
print(f"Average Spend: {average:.2f}")