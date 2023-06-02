# I am starting project with repetition of 3X
for i in range (3):
    print("     Welcome to the PhoneBook")
    print("\n")
# Its my project in this code I will made a code to enter contact numbers with their names.
    print("     Here is the Phonebook Menu")
    print("\n")
    print("Select the following option")
    print("  1. Add contact")
    print("  2. Delete contact")
    print("  3. Edit contact")
    select= int(input("Type here: "))

#this is the basic info about the project
    contact_dict={"Ahmed" : 92302038660, "Ali": 92330554846, "Abdullah": 92305788564, "Mama": 923048426600, "SE Hira 21": 923269664645} 
    search=set(contact_dict)
    print("\n   Total contacts in the phonebook are: ", search)
    if select==1:
        # for the option 1 I want to add the contact number
        add_contact=int(input("How many contact do you want to add in the phonebook: "))

        for i in range(add_contact):
            key=input("Enter the name: ")
            value=input("Enter the mobile number: ")
            contact_dict[key]=value

            search_name=set(contact_dict)
    # its not a convinent way
    #search_no=set(value)
# contact added in the phonebook
# this is ordinary approach
# search={key for key in contact_dict}
# print(search)
        print(search_name)
        #print(search_no)
        print("Contacts are save in the phonebook")
    
#-------------------------------------------------------
    elif select==2:
        #contact_dict[key]=value
        del_contact=int(input("Enter how many numbers you want to delete from the phonebook: "))
        search_name=set(contact_dict)
        for i in range (del_contact):
            con=input("Enter the name of contact that you want to delete: ")
            if con in search_name:
                print("Contact Found")
                search_name.remove(con)
                print("Contact delete successfully")
                print("Remaining Contacts: ", search_name)
            else:
                print("Contact not found")
#-----------------------------------------
    elif select==3:
        search_name=set(contact_dict)
        key=input("Enter the contact name that you want to edit it the phonebook: ")
        if key in contact_dict:
            print("Contact found")
            new_value=input("Enter the new mobile number: ")
            contact_dict[key]=new_value
            search_name=set(contact_dict)
            print("\n \n")
            print(contact_dict)
        #---------------
    # elif key in contact_dict:
    #     new_key=input("Enter new name: ")
    #     value=contact_dict[new_key]
    #     print(contact_dict)



