# Input/Output operations such as open, close, read, write and append

# read a file programe
'''f = open("sample.txt")
data = f.read()    # read the file data
print(data)    # print the data
f.close     # close the file'''

# read opeations 
'''f = open("sample.txt")
data = f.read()    
   #or
#data = f.read(5) 
   #or
#data = f.readline()
print(data)    
#data = f.readline()
#print(data)
f.close'''     # close the file

# write a file programe
'''f = open('another.txt', 'w')
f.write('this a write programe of a text file in python\nand this work successfully')
f.write("my name is vikash sharma")
f.close()'''

# appending   # used for writing in a file end
'''f = open("another.txt", 'a')
f.write(" i am appending")
f.write ("\nwhat is m y name ?")
f.close'''

# with statement        # it is used to read and write a fle without close st.
from os import write

'''with open("sample.txt", 'r') as f:
   a=f.read()
   print(a)'''

'''with open('sample.txt','w') as f:
   a=f.write("hello world")
print(a)'''
