def AddContact(details):
    name = input("Enter the name: ")
    phone_no = int(input("Enter the phone number: "))
    email = input("Enter the email: ")
    address = input("Enter the address: ")
    details[name]={"Phone_no":phone_no , "Email": email , "Address": address}
    return details

def ViewContact(details):
    for names in details:
        print(names, details[names]["Phone_no"], end="\n")

def SearchContact(details, name="NULL", phone_no = 0):
    if name!="NULL" and phone_no==0:
        for names in details:
            if names == name:
                return (names,details[names])
        return ("No such Contact exits")
    elif name=="NULL" and phone_no!=0:
        for names in details:
            if details[names]["Phone_no"]==phone_no:
                return (names,details[names])
        return ("No such Contact exits")
    else:
        for names in details:
            if details[names]["Phone_no"]==phone_no and names == name :
                return (names,details[names])
        return ("No such Contact exits")

def UpdateContact(details):
    ch = input("Want to update contact name (Y/N)")
    if ch.upper() =="Y":
        old_name = input("Enter the old name: ")
        new_name = input("Enter the updated name: ")
        item = details[old_name]
        del details[old_name]
        details[new_name]=item

    ch = input("Want to update Phone number (Y/N)")
    if ch.upper()=="Y":
        name = input("Enter the name of the Contact: ")
        new_phone_no = int(input("Enter the updated phone number: "))
        details[name]["Phone_no"] = new_phone_no

    ch = input("Want to update email (Y/N)")
    if ch.upper() == "Y":
        name = input("Enter the name of the Contact: ")
        new_email = input("Enter the updated email: ")
        details[name]["Email"] = new_email
    
    ch = input("Want to update address (Y/N)")
    if ch.upper() == "Y":
        name = input("Enter the name of the Contact: ")
        new_address = input("Enter the updated address: ")
        details[name]["Address"] = new_address
    
    return details

def DeleteContact(details):
    ch = input("Want to delete the Contact by Name (N) or Phone number (P): ")
    if ch.upper() =="N":
        name = input("Enter the Name of the contact to delete: ")
        del details[name]
    elif ch.upper() == "P":
        phone_no = int(input("Enter the Phone number of the contact to delete: "))
        for names in details:
            if details[names]["Phone_no"]==phone_no :
                del details[names]
                break
    return details



print("\t--------------------CONTACT BOOK--------------------\n")
details = {"Sachin":{"Phone_no":7864678898, "Email":"sachin123@gamil.com", "Address":"Colen,UK"},
           "Naveen":{"Phone_no":9167345698, "Email":"navven778@gamil.com", "Address":"Burlington, UP"},
           "John":{"Phone_no":8967345687, "Email":"john657332@gamil.com", "Address":"Mohbillapur, USA"}}
while True:
    print("\nFor Adding new contact , -------------press 1")
    print("For Viewing contact list , -----------press 2")
    print("For Updating the contacts ,---------- press 3")
    print("For Searching the contact ,---------- press 4")
    print("For Deleting contact ,--------------- press 5")
    print("For exiting the Contact book, --------press 6\n")
    choice = int(input("Enter the choice: "))
    if choice == 1:
        details = AddContact(details)
    elif choice == 2:
        ViewContact(details)
    elif choice == 3:
        details = UpdateContact(details)
    elif choice == 4:
        name = input("Enter the name of the contact to search otherwise enter null: ")
        phone_no = int(input("Enter the phone number to search otherwise enter 0: "))
        if name == "null":
            search = SearchContact(details, phone_no)
        elif phone_no==0:
            search = SearchContact(details, name)
        else:
            search = SearchContact(details, name, phone_no)
        print(search)
    elif choice == 5:
        details = DeleteContact(details)
    elif choice == 6:
        print("Exiting the Contact Book :)")
        break
    else:
        print("Wrong input")











