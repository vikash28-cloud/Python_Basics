              #  conditionals :  if, elif and else

# check th greater number and use of if ,elif and else----/
'''x = int(input("enter the 1st no: "))
a = int(input("enter the 2nd no: "))
if(x>a) :
    print(a,"is Lesser than",x)
elif(x<a):
    print(a,"is Greater than",x)
else:
    print('both no. you entered are  equal',a,'=',x)
'''

# we can use multiple elif statements
'''b = 50
if (b<10):
    print(b,"is lesser than 10")
elif (b<20):
    print(b,"is lesser tha 20")
elif (b<10):
    print(b,"is less than 10")
elif (b>60):
    print(b,"is greater than 60")
else:
    print("both are equal")'''

#multiple if statements 
'''b = 50
if (b>10):
    print(b,"is greater than 10")
if (b>20):
    print(b,"is greater tha 20")
if (b<10):
    print(b,"is less than 10")

if (b>60):
    print(b,"is lesser than 60")
else:
    print("both are equal")'''

#        Logical operators---

# and : true if both operators are true else false
# or  : true if at least one opreator is true else false
# not :inverts true to false and false to true

'''x = 50
if (x>20 and x<30):
    print("true")
else:
    print("false")'''

'''y = 50
if (y>20 or y<30):
    print("true")
else:
    print("false")'''

# last else condition apply if all the elifs are fail


