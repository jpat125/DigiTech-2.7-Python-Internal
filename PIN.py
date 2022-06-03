#Creating def for PIN access 

def PIN_access():
    while True:
        userpin=int(input("Enter PIN: "))
        if userpin == 1234:
            print ("access granted")
            print('\n')
            break
        else:
            print ("Please try again:")
            print ('\n')

PIN_access()
