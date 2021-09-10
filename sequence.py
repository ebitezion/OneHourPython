""" The list """
items=[]
def add(item):
    if not item:
        print("Empty request")
    items.append(item)

def delete_by_index(index):
    items.pop(index)

def update(newItem,oldItemIndex=0):
    items[oldItemIndex]=newItem

def search(item):
    if item in items:
        return True
    return False
########################################################
    # Dictionary
#########################################################
person={}


def rDict():
    #populate dict
    person["name"]="Zion"
    person["age"]="26"
    person["gender"]="Male"

    # display dict
    print(f"This is the dictionary {person}")

    #update the dictionary
    person["age"]="23"
    # display dict
    print(f"This is the update dictionary with change in age {person}")


# use it to perform a test
def main():
    #Run dictionary code
    rDict()
    print("\n")
    #Add to the list
    add("Mango")
    add("Apple")
    add("Orange")
    add("Pear")

    #Display the list
    print(f"The list is {items}")

    #Remove the pear item at index 4
    delete_by_index(3)
    
    #Display the list
    print(f"The list after delete is {items}")

    #search if apple is in the list
    if search("Apple"):
        #Display the result
        print(f"Yes Apple is in {items}")
    else:
        #Display the result
        print(f"No Apple is not in {items}")
    
    #Update this list so apple is now pawpaw
    update("Pawpaw",2)
    #Display the result
    print(f"Yes Orange is replaced by Pawpaw in {items}")



if __name__ == "__main__":
    main()