print("\n******************** FOR LOOP *****************\n")

numbers = [1,2,3,4,5,6,7,8]
sq = 0
for val in numbers : 
    sq = val*val
    print(sq)
    
print("\n************ LOOP THROUGH A LIST ****************\n")
fruits =["Apple","Banana","Orange"]
for fruit in fruits : 
    print(fruit)
    
print("\n********** USING RANGE FUNCTION ****************\n")
for i in range (1,6) :
    print(i)

print("\n******************* USING RANGE IN FOR FUNCTION *************\n")
sum = 0
for val in range (1,6) :
    sum = sum + val
    print(sum,"is the sum of natural numbers")
    
print("\n************ WHILE LOOP *******************\n")
n =int(input("Enter the number :"))
while n!=0 :
    d = n%10
    print(d,end =" ")
    n//=10
    
print("\n**************** BREAK STATEMENT ******************\n")
for i in range (1,7) :
    if i == 4 :
        break
    print("Loop ended")
    
print("\n******** WORKING OF BREAK STATEMENT IN WHILE LOOP ************************\n")
count = 1
while count <= 6 :
    if count == 4 :
        break
    print(count)
    count += 1
    print("Loop Termination")
    
print("\n*********** CONTINUE IN FOR LOOP ***************\n")
for i in range (1,7) :
    if i == 4 :
        continue
    print(i)
    
print("\n******************* CNTINUE IN WHILE LOOP ******************\n")
count = 0
while count <5:
    if count == 4:
        count +=1
        continue
    print(count)
    count +=1