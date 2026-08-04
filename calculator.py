print("\n================== CALCULATOR =====================\n")

customer_name=input("Enter customer name :")

item1 = input("Enter Item 1 Name :")
price1 = float(input("Enter Item 1 Price :"))
qty1 = int(input("Enter Item 1 Quantity :"))
amount1 = price1 * qty1

item2 = input("\nEnter Item 2 Name :")
price2 = float(input("Enter Item 2 Price :"))
qty2= int(input("Enter Item 2 Quantity :"))
amount2 = price2 * qty2

item3 = input("\nEnter Item 3 Name :")
price3 = float(input("Enter Item 3 Price :"))
qty3 = int(input("Enter Item 3 Quantity :"))
amount3 = price3 * qty3

total_bill = amount1 + amount2 + amount3
    
if(total_bill >= 6000):
    discount = total_bill * 0.40
elif(total_bill >= 3000):
    discount = total_bill * 0.30
elif(total_bill >= 2000):
    discount = total_bill * 0.20
else:
    discount = 0
    
final_amount = total_bill - discount

print("\n======================= CUSTOMER BILL =======================\n ")
print(customer_name,"your bill is : \n")
print("Total Bill   :", total_bill)
print("discount     :", discount)
print("final amount :", final_amount)

print("\n********************* THANK YOU VISIT AGAIN ************************\n")