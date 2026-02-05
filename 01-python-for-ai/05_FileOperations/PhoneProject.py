from phone_class import PhoneBook

pb = PhoneBook()

while(True):
    print("\n+--- Phone Book ---+")
    print("1 -> Add contact")
    print("2 -> List contact")
    print("3 -> Delete contact")
    print("4 -> Exit")

    choice = int(input("Make your choice: "))

    if(choice == 1):
        name = input("Name: ")
        surname = input("Surname: ")
        phoneN = input("Phone number: ")
        pb.add_contact(name,surname,phoneN)
    elif(choice == 2):
        pb.list_contacts()
    elif(choice == 3):
        name = input("Enter the name of the contact you want to delete: ")
        pb.delete_contact(name)
    elif(choice == 4):
        print("Exiting...")
        break
    else:
        print("Invalid choice, please try again!")