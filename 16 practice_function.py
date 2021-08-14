# find greatest no. programme
'''if n1>n2:
    g = n1
else:
    g =n2
if g>n3:
    print(g, "is grater ")
else:
    print(n3, "is greater")'''

# find greatest no. programme using function
'''def greatest(n1,n2,n3):
    if n1>n2:
       g = n1
    else:
     g =n2
    if g>n3:
        return g, "is grater "
    else:
        return n3, "is greater"


n1 = int(input("Enter 1st no: "))
n2 = int(input("Enter 2st no: "))
n3 = int(input("Enter 3st no: "))
print(greatest(n1,n2,n3)'''

# programme to convert celsius to fehrienheit
# formula =   f =32+(c*9/5) 

'''tempr = float(input("enter tempreature in celsius: "))
fhr = 32+(c*9/5)
print(fhr)'''

#using function
'''def temp_convert(c):
    f = 32+(c*9/5)
    return f

c = float(input("enter tempreature in celsius: "))
print(f"{c} celsius in fahreinheit is "+str(temp_convert(c)))'''

# sum of first n natural number 
'''num = int(input ("Enter no: "))
n= 0
for i in range (1,num+1):
    n = n+i
print(n)'''

'''def natural_sum(num):
    n= 0
    for i in range (1,num+1):
        n = n+i
    return n


num = int(input("enter no.: "))
print(f"the sum of first {num} natural no is "+str(natural_sum(num)))'''

#python programm to convert inches to centimeters
# 1 inch = 2.54cm
'''print("\t\tconvert inch to meter")
n =float(input("inches = "))
cm = 2.54*n
print(cm,"cm")'''

'''def measure(n):
    cm = 2.54*n
    return cm 

n= float(input("inches = "))
print(f"{n} inches equals to "+str(measure(n))+"cm")'''

# multiplication table function


