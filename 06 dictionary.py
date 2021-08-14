            #keys     values
mydict = { "keys"  : "values",
          "vikash" : 'hello',
             "open":"close", 
           "hello" :"hy", 
             "shut":'down',
          "genius" :"intelligent",
            "list" : [1,2,3,4],
           'anothdict' : {"false":"true"},
                2   : 3               }
print(mydict)

'''print("\t\t DICTIONARY\n")
word = input("Enter word: ")
print("\n meaning: ",mydict[word],"\n")'''

'''print(mydict["list"])
print(mydict["anothdict"] ["false"])
mydict['keys'] = 'lock'
print(mydict['keys'])
print(mydict[2])'''

#---------------- methods of dictionary ------/

'''print(list(mydict.keys()),"\n\n")#print all the keys in a list
print(list(mydict.values()),"\n") # print all the values in a list
print(mydict.items(),"\n") #print the (key , value) of dictionary'''

# update method 
'''print(mydict,"\n\n")         
updatdict = {"come": "out", "get":"in",
                "vikash":"intelligent","keys":"lock"}  # update dictionary 
mydict.update(updatdict)
print(mydict)'''

# get method (important)
'''print(mydict.get("vikash"))  #what is the difference between (get) and ([]) method
print(mydict["vikash"],"\n\n")

print(mydict.get("vikash2")) #it returns value "none" when the key is not present in dictionary
print(mydict["vikash2"])     # it throws an "error"'''
