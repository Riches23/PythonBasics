
#%%writefile test2.txt
#Riches, a good boo
#I will never give up
#All things are perfect through Christ Jesus

with open("test2.txt",mode="a") as f: ##To add an item to a text file
    f.write("\nI love you")
with open("test2.txt",mode="r") as f:
    print(f.read())

## Another method to creating a text file
with open("test3.txt",mode="w") as f: 
    f.write("You don't know the weight of what you said")
    f.write("\nWho are you to question your abilities")
with open("test3.txt",mode="r") as f:
    print(f.read())