# ----- function calling-------/
'''def greet(name):                    #function 1
    print("Good morning, " +name) 

def vikash(marks):                     #function 2 
    return (sum(marks)/400)*100   
     #or 
   #return (marks[0]+marks[1]+marks[2]+marks[3])/400*100
name = input("Enter your name: ")
m1 = int(input("hindi: "))
m2 = int(input("physics: "))
m3 = int(input("mathematics: "))
m4 = int(input("english: "))
marks = [m1,m2,m3,m4]
greet(name)
print("Your percentage is "+str(vikash(marks)))
print("Thank you")'''

# ----------default argument--------/
'''def greet(name ="user"):
    print("Good morning, " +name)
    
greet("vikash")
greet()'''


'''def mysum(num1, num2):
    return num1+num2


print(mysum(1,2))'''


#-------- factorial function-----/
'''num = 5    # simple factorial programme
fact = 1
for i in range(1,num+1):
    fact = fact*(i+1)
print(fact)'''

# factorial using function
'''def factorial(num):
    fact = 1
    for i in range(1,num+1):
        fact = fact*i
    return fact

print("\t\t\tFACTORIAL PROGRAMME")
num = int(input("Enter number: "))
print(f"factorial of {num} is "+str(factorial(num)))'''