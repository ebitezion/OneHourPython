data=[
    {"name":"Efe", "age":"24"},
    {"name":"Emma", "age":"23"},
    {"name":"Ray", "age":"20"}
    ]
with open("dummy.csv","a") as f:

    if not f=="":
        print("file created")
     
    
       # key,"value"
    for item in data:
        x=item["name"]
        y=item["age"]
        print(f'{x} , {y}',file=f)          
        
    #read the file to stdout

fr=open("dummy.csv","r")
print(fr.readlines(2))