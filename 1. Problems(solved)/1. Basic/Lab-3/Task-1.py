#Task-1 b)
i = -10
while(i<=20):
    if i==20:
        print(i, end=" ")
    else:
        print(i, end=",")
    i+=5

print("\n")
# c)
start = 18
while (start<=63):
    if (start == 63):
        print(start, end=" ")
    else:
        print(start, end=",")
    start+=9

print("\n")

# d)
start = 18
while (start<=63):
    if (start%2==0):
        print(start, end=",")
    else:
        if start == 63:
            print(start*(-1), end=" ")
        else:
            print(start*(-1), end=",")
    start+=9
    
# Task-2
#car = input("Enter the name of car: ")
#num = int(input("Enter the number: "))

#for i in range(num):
#    print(car)
    
# Task-4
sum = 0
for i in range(601):
    if(i%7==0 and i%9==0):
        sum = sum+i
print(sum)

# Task-5
sum = 0
for i in range(601):
    if(i%7==0 or i%9==0):
        if(i%7==0 and i%9==0):
            continue
        else:
            sum+=i
print(sum)

#Task-6
#for i in range(10,51):
#    print(i, end=" ")
    
#Task-7
num = int(input("Enter a number"))
sum = 0
for i in range(1,num+1):
    if(i%2==0):
        sum = sum-(i**2)
    else:
        sum = sum+(i**2)
print(sum)
    
#Task-18:
num = int(input("Enter a number"))
val1 = int(input("Enter the value"))
maxval = 
minval = val1
for i in range(num):
    val2 = int(input("Enter the value"))
    if()