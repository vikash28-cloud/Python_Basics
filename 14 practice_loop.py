# multplies using for loop
'''num = int(input("ENTER no: "))
for i in range(1,11):
    print(str(num) + "x"+str(i) + "=" + str(i*num)) #or
       
    #print(f"{num}x{i}={num*i}")  # fstring'''

# multplies using while loop
'''num = int(input("Enter  no: "))
i=0
while i<10 :
    i=i+1
    print(str(num) + "x"+str(i) + "=" + str(i*num))'''

# start with statement
'''l1 = ["vikash","sachin","sohail","iron man"]
for name in l1:
    if name.startswith("s"):
        print("hello "+name )'''


# prime number
'''num = int(input("enter no: " ))
for i in range (2,num):
    if (num%i==0):
        print("not prime")
        break
else:
    print("prime ")'''

    #or
 
'''num = int(input("enter no: " ))
prime = True
for i in range (2,num):
    if (num%i==0):
        prime = False
if prime:
    print("the number is PRIME")
else:
    print("the number is NOT PRIME")'''


# sum of first n natural number using while loop
num = int(input("NATURAL NUMBER: " ))
n = 0
for i in range(1,num+1):

    n = n+i
print(F"THE SUM IS {n}")


# factorial
'''num = int(input("enter no. for factorial \n " ))
factorial = 1
for i in range(1,num+1):

    factorial = factorial * i
print(F"THE FACTORIAL OF {num} IS {factorial}")'''  


# printing stars
'''for i in range(5):
    print("*"*i)'''
   
    
num = int(input("ENTER no: "))
for i in range(1, 10):
    print(num*i)
    
    