alphabets = "abcdefghijklmnopqrstuvwxyz"
inventory = []
for i in range(26):
        inventory.append([]) 

print("---MEDICINE MANAGEMENT SYSTEM---")
print("press 1 to add medicine to your list")
print("press 2 to search medicine from your list")
print("press 3 to delete medicine from your list")
print("press 4 to show the current list")
print("press 5 to terminate the system")
n=int(input("enter your choice"))


def medicine_add():
    medicine = input("Enter medicine name: ").lower()
    first_letter = medicine[0]
    index = -1
    for i in range(26):
        if alphabets[i] == first_letter:
            index = i  
            break 

    if index != -1:
        inventory[index].append(medicine)
        inventory[index].sort()
        print("Saved successfully!")
    else:
        print("Error: Please start the name with a letter a-z")


def medicine_search():
    medicine=input("enter the medicine name to be searched:")
    first_letter = medicine[0]
    index=-1
    for i in range(26):
        if alphabets[i] == first_letter:
            index=i
            break
    l=len(inventory[index])
    for i in range(0,l):
        if(inventory[index][i]==medicine):
            print("medicine is present in the list")
        else:
            print("medicine not found")


def medicine_listshow():
    print("----MEDICINE LIST----")
    for i in range(26):
        for j in range(len(inventory[i])):
            print (inventory[i][j])


def medicine_delete():
    medicine=input("enter the medicine name to be deleted:")
    first_letter = medicine[0]
    index=-1
    for i in range(26):
        if alphabets[i] == first_letter:
            index=i
            break
    l=len(inventory[index])
    for i in range(0,l):
        if(inventory[index][i]==medicine):
            del(inventory[index][i])
        else:
            print("medicine not found")
while(n!=5):
    if(n==1):
        medicine_add()
        n=int(input("give another task"))
    if(n==2):
        medicine_search()
        n=int(input("give another task"))
    if(n==3):
        medicine_delete()
        n=int(input("give another task"))
    if(n==4):
        medicine_listshow()
        n=int(input("give another task"))
if(n==5):
    print("session terminated ---THANK YOU---")


