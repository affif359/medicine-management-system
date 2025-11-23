alphabets = "abcdefghijklmnopqrstuvwxyz"
inventory = []
prices = []  # Parallel array to store prices
for i in range(26):
    inventory.append([])
    prices.append([])

print("===========================")
print("MEDICINE MANAGEMENT SYSTEM")
print("===========================")
print("press 1 to add medicine to your list")
print("press 2 to search medicine from your list")
print("press 3 to delete medicine from your list")
print("press 4 to show the current list")
print("press 5 to create bill for customer")
print("press 6 to terminate the system")
n = int(input("enter your choice: "))


def medicine_add():
    medicine = input("Enter medicine name: ").lower()
    price = float(input("Enter medicine price: "))
    first_letter = medicine[0]
    index = -1
    for i in range(26):
        if alphabets[i] == first_letter:
            index = i  
            break 

    if index != -1:
        inventory[index].append(medicine)
        prices[index].append(price)
        print("Saved successfully!")
    else:
        print("Error: Please start the name with a letter a-z")


def medicine_search():
    medicine = input("enter the medicine name to be searched: ").lower()
    first_letter = medicine[0]
    index = -1
    for i in range(26):
        if alphabets[i] == first_letter:
            index = i
            break
    
    found = False
    if index != -1:
        for i in range(len(inventory[index])):
            if inventory[index][i] == medicine:
                print(f"Medicine is present in the list - Price: Rs.{prices[index][i]}")
                found = True
                break
    
    if not found:
        print("Medicine not found")


def medicine_listshow():
    print("----MEDICINE LIST----")
    for i in range(26):
        for j in range(len(inventory[i])):
            print(f"{inventory[i][j]} - Rs.{prices[i][j]}")


def medicine_delete():
    medicine = input("enter the medicine name to be deleted: ").lower()
    first_letter = medicine[0]
    index = -1
    for i in range(26):
        if alphabets[i] == first_letter:
            index = i
            break
    
    found = False
    if index != -1:
        for i in range(len(inventory[index])):
            if inventory[index][i] == medicine:
                del inventory[index][i]
                del prices[index][i]
                print("Medicine deleted successfully!")
                found = True
                break
    
    if not found:
        print("Medicine not found")


def create_bill():
    print("\n----CREATE CUSTOMER BILL----")
    cart = []
    cart_prices = []
    
    while True:
        medicine = input("Enter medicine name (or 'done' to finish): ").lower()
        if medicine == 'done':
            break
        
        first_letter = medicine[0]
        index = -1
        for i in range(26):
            if alphabets[i] == first_letter:
                index = i
                break
        
        found = False
        if index != -1:
            for i in range(len(inventory[index])):
                if inventory[index][i] == medicine:
                    cart.append(medicine)
                    cart_prices.append(prices[index][i])
                    print(f"Added {medicine} - Rs.{prices[index][i]}")
                    found = True
                    break
        
        if not found:
            print(f"Medicine '{medicine}' not found in inventory")
    
    if len(cart) > 0:
        print("\n----CUSTOMER BILL----")
        total = 0
        for i in range(len(cart)):
            print(f"{cart[i]}: Rs.{cart_prices[i]}")
            total += cart_prices[i]
        
        print(f"\nSubtotal: Rs.{total}")
        discount = total * 0.10
        final_total = total - discount
        print(f"Discount (10%): Rs.{discount}")
        print(f"Final Total: Rs.{final_total}")
        print("----Thank you for shopping!----\n")
    else:
        print("No items in cart")


while n != 6:
    if n == 1:
        medicine_add()
        n = int(input("give another task: "))
    elif n == 2:
        medicine_search()
        n = int(input("give another task: "))
    elif n == 3:
        medicine_delete()
        n = int(input("give another task: "))
    elif n == 4:
        medicine_listshow()
        n = int(input("give another task: "))
    elif n == 5:
        create_bill()
        n = int(input("give another task: "))
    else:
        print("Invalid choice")
        n = int(input("give another task: "))

if n == 6:
    print("session terminated ---THANK YOU---")
