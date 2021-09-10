import sys

print("====================================================================================")
#The sole purpose of section is show how strings can be sliced
#prompt user for input
tokens=input("Enter a word or a sentence")

#A word is a bunch of characters that ends with a tab
sentence=False
for token in tokens:
    
    if token == " ":
        sentence=True  
        break 

if sentence == True:
    toks=tokens.split(" ")
    print(f"The first word in your sentence is {toks[0]}")
elif sentence==False:
    print(f"The first letter in your word is {tokens[0]}")

print("====================================================================================")

#what is number? A number is anything that begins with 0,1,2,3...9
#prompt user for input
entry=input("Type a thing and i would guess if it is a no:  ")
#convert str to list
i=0
entry_list=[]
while(True):
    if len(entry)==i:
        break
    entry_list.append(entry[i])
    i=i+1

count=0


is_number=True
for entry_list[0] in ["0","1","2","3","4","5","6","7","8","9"]:
    for no in entry_list:
        if is_number==False:
            print("This is not a number")
            sys.exit(0)

        if  no in ["0","1","2","3","4","5","6","7","8","9"]:
            is_number=True
        else:
            is_number=False
                        
if is_number==True and entry_list[0] in ["0","1","2","3","4","5","6","7","8","9"]:
    print("This is a number")
else:
    print("This is not a number")


print("====================================================================================")
