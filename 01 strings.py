
#text = ''' dear <|name|> 
#           you are selected for airfoce x group test
  #         <|date|>'''

'''name = str(input("enter your name: "))
date = "18/05/2021"
text = text.replace("<|name|>" , name)
text = text.replace("<|date|>", date)

print(text)'''

text = "hello  world my  name is vikash     sharma"
print(text.replace("  ", " "))
