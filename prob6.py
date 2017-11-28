names=[]
ages=[]
emails=[]
for i in range(0,3):
    print("Enter Details for person ",i+1,":")
    names.append(input("\nEnter name:\n"))
    ages.append(input("Enter age:\n"))
    emails.append(input("Enter email:\n"))
print("\n\n")
for i in range(0,3):
    print("\nPerson ",i+1," Details: ")
    print(names[i]+ages[i]+emails[i])
