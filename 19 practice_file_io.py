# --------------find a word in a file-------------/
from os import close, read, write

'''f = open("another.txt", 'r')
a =f.read()
word = input("enter word to find: ")
if word in a:
    print(f"the word {word} is present")
else:
    print(f"not present")
f.close()'''

# --------------game score update--------------/
# if score is incresed from previous score then the value is updated 

'''score=int(input("enter your score: "))
f = open('sample.txt', 'r')
a = f.read()

if a=="":
    f = open("sample.txt", 'w')
    f.write(str(score))
    print("Congratulations! \nyou set a new record")

elif int(a)<score :
    f = open("sample.txt", 'w')
    f.write(str(score))
    print("Congratulations! \nyou break the record ")
    print("score is updated")

else :
    f = open("sample.txt", 'w')
    f.write(str(a))
    print("you not break the record\ntry again!")
f.close()'''

#  --------------replace a word in a file-------------/
'''with open('another.txt') as f:
    a=f.read()
    print("\n",a,"\n")
word = input("enter the word for replacement: ")
replace = input("enter the new word: ")
a  =a.replace(str(word),str(replace))
with open('another.txt', 'w') as f:
    f.write(str(a))
    print("\n",a,"\n")'''

# -----------  multiplication tables --------/

'''for i in range (2,21):
    with open(f"tables/table{i}.txt","w") as f:
        for j in range(1,11):
            f.write(f"{i}x{j} = {i*j}\n")'''
            

# - -- -- - mining in a log file -----------/
'''content = True
i = 1
with open("log.txt", "r") as f:
    word = input("enter word: ")
    while content:
        content  =f.readline().lower()  # lower for lowercase letters
 
        if word in content:
            print(f"\nyes {word} is present on line number {i}")
            print(content)
        i+=1'''
    
# -----------copy a file---------/
'''with open("another.txt", 'r') as f:
    content  = f.read()
with open("copy.txt", 'w') as f:
    f.write(content) '''

# -----check two files are identical or not------/
'''file1 = input("enter file name: ")
file2 = input("enter file name: ")

with open(file1) as f:
    f1 = f.read()
with open(file2) as f:
    f2 = f.read()
if f1==f2:
    print("files are identical")
else:
    print("files are not identical'''

#  -----------wipe the content of a file ------/
'''with open("wipe.txt", 'w') as f: # all content erase in copy.txt
    f.write(" ")'''     

# -------------delete a file-----------/
'''import os
os.remove("delete a file.txt")'''

# --------------rename a file name -------------/
'''import os
oldname = 'oldname.txt'
newname = "newname_rename.txt"

with open(oldname, 'r') as f:
    content = f.read()
with open(newname, 'w') as f:
    f.write(content)

os.remove("oldname.txt")'''