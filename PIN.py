#Creating def for PIN access 

def PIN_access():
    userpin=int(input("Enter PIN: "))
    if userpin == 1234:
        print ("access granted")

PIN_access()
