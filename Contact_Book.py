
print("WELCOME TO THE CONTACT DIRECTORY\n")

filename = "Contack Book.txt"  
file=open(filename, "a+")  
file.close

def main_menu(): 
    print("1.Show all existing Contacts")  
    print("2.Add a new Contact")  
    print("3.Search the existing Contact")
    print("4.Update Contact")
    print("5.Delete Contack")
    print("6. Exit")  
    choice=input("Enter your choice:")  
    if choice=="1":  
        file=open(filename,"r")  
        filecontents=file.read()  
        if len(filecontents)==0:  
            print("There is no contact in the Contact Book.")  
        else:  
            print(filecontents)  
        file.close  
        enter=input("Press Enter to continue")  
        main_menu()  
    elif choice=="2":  
        newcontact()  
        enter=input("Press Enter to continue")  
        main_menu()  
    elif choice=="3":  
        searchcontact()  
        enter=input("Press Enter to continue")  
        main_menu()
    elif choice=="4":  
        updatecontact()  
        enter=input("Press Enter to continue")  
        main_menu()
    elif choice=="5":  
        deletecontact()  
        enter=input("Press Enter to continue")  
        main_menu()
    elif choice=="6":  
        print("Thank you for using Contact BooK!")  
    else:  
        print( "Please provide a valid input!\n")  
        enter=input("Press Enter to continue")  
        main_menu()  
           
def searchcontact():  
    searchname=input( "Enter First name for Searching contact record: ")  
    remname=searchname[1:]  
    firstchar=searchname[0]  
    searchname=firstchar.upper()+remname  
    file=open(filename, "r")  
    filecontents=file.readlines()  
       
    found=False  
    for line in filecontents:  
        if searchname in line:  
            print("Your Required Contact Record is:", end = " ")  
            print(line)  
            found=True  
            break  
    if found == False:  
        print("The Searched Contact is not available in the Phone Book", searchname)  
  
def input_firstname():  
    first=input("Enter your First Name:")  
    remfname=first[1:]  
    firstchar=first[0]  
    return firstchar.upper()+remfname  
  

def input_lastname():  
    last=input( "Enter your Last Name: ")  
    remlname=last[1:]  
    firstchar=last[0]  
    return firstchar.upper() + remlname  
  

def newcontact():  
    firstname=input_firstname()  
    lastname=input_lastname()  
    phoneNum=input( "Enter your Phone number: ")  
    emailID=input( "Enter your E-mail Address: ")
    address=input("Enter your Address:")
    contactDetails=("[" + firstname + " " + lastname + ", " + phoneNum + ", " + emailID +  ","+address+"]\n")
    file=open(filename, "a")  
    file.write(contactDetails)  
    print("The following Contact Details:\n "+ contactDetails + "\nhas been stored successfully!")

def updatecontact():
    searchname=input("Enter the First name of the contact to update: ")  
    remname=searchname[1:]  
    firstchar=searchname[0]  
    searchname=firstchar.upper()+remname
    file=open(filename, "r")  
    filecontents=file.readlines()  
    file.close()
    found=False
    index_to_update=None
    for index,line in enumerate(filecontents):  
        if searchname in line:  
            print("Your required contact record is:",end = " ")  
            print(line)  
            found=True  
            index_to_update=index
            break
    if found:
        firstname=input_firstname()
        lastname=input_lastname()
        phoneNum=input("Enter the new phone number: ")
        emailID=input("Enter the new email address: ")
        address=input("Enter the new address: ")
        contactDetails=f"[{firstname} {lastname}, {phoneNum}, {emailID}, {address}]\n"
        filecontents[index_to_update] = contactDetails
        file=open(filename, "w")
        file.writelines(filecontents)
        file.close()
        print("The contact has been updated successfully!")
    else:
        print(f"The searched contact '{searchname}' is not available in the Phonebook.")


def deletecontact():
    searchname=input("Enter the First name of the contact to delete: ")  
    remname=searchname[1:]  
    firstchar=searchname[0]  
    searchname=firstchar.upper() + remname
    file=open(filename, "r")  
    filecontents=file.readlines()  
    file.close()
    found=False
    index_to_delete=None
    for index,line in enumerate(filecontents):  
        if searchname in line:  
            print("The contact to be deleted is:",end = " ")  
            print(line)  
            found=True  
            index_to_delete=index
            break
    if found:
        filecontents.pop(index_to_delete)
        file=open(filename,"w")
        file.writelines(filecontents)
        file.close()
        print("The contact has been deleted successfully!")
    else:
        print(f"The searched contact'{searchname}'is not available in the Contact List.")
main_menu()  
