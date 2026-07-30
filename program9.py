print("! ********************* USE BREAK ********************* !")

password = "Butterflay"

while True:
    user_password = input("Enter password :")
    
    if user_password == password:
        print("Access Granted")
        break
    else:
        print("Wrong password")
        print("Try Again")
        
print("\n! *************** WITOUT BREAK ************** !\n")
        
password = "payal"
user_password == ""

while user_password != password:
    user_password = input("Enter password :")
    
    if user_password == password:
        print("Access Granted")
    else :
        print("Wrong Password")
        print("Try Again!")
print("Login Successful")
        