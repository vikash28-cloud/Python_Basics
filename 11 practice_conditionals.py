#  find greatest of four numbers entered by the user
'''a = int(input("enter 1st no: "))
b = int(input("enter 2st no: "))
c = int(input("enter 3st no: "))
d = int(input("enter 4st no: "))
if(a>b):
    f1 =a
else:
    f1 =b
if(c>d):
    f2 = c
else:
    f2 = d
if(f1>f2):
    print(str(f1) + " is greatest")
else:
    print(str(f2) + " is greatest")'''

# program pass or fail
'''sub1 =int(input("enter sub1 marks: "))
sub2 =int(input("enter sub2 marks: "))
sub3 =int(input("enter sub3 marks: "))
sub4 =int(input("enter sub4 marks: "))
if(sub1>100 or sub2>100 or sub3>100 or sub4>100):
    print("sorry! please enter the valid marks")
 
elif sub1<33 or sub2<33 or sub3<33 or sub4<33:
    print("FAIL ")
    print("Total marks:",sub1+sub2+sub3+sub3+sub4,"\nout of: 400")
 
elif (sub1+sub2+sub3+sub3)/4<40:
    print("FAIL")
else:   
    print("YOU ARE PASSED")
    print("Total marks:",sub1+sub2+sub3+sub3+sub4,"\nout of : 400")
'''

# detecting spam 
'''text = input("Enter the message: ")
if("make a lot of money" in text):
    spam =True
elif "click on this " in text:
    spam = True
elif "subscribe now" in text:
    spam = True
elif "share this and earn" in text:
    spam = True
else:
    spam = True

if (spam):
    print("this message is a spam")
else:
    print("this is not a spam")'''

# username programme
'''uname = input("Enter username : ")
if(len(uname)<10):
    print("enter valid username of 10 characters")
else:
    print("Thank you!")'''

# grade programme
'''marks = int(input("Enter marks:\n"))
if (marks>90):
    grade = "A++"
elif marks>80:
    grade = "A"
elif marks>70:
    grade = "B"
elif marks>60:
    grade = "c"
elif marks>50:
    grade = "D"
elif marks>40:
    grade = "E"
else:
    grade = "E"

print(grade)'''
   
