import time
def returntomenu():

    returno=((input("Would you like to re-use this tool?")).strip().lower())

    if returno == "y" or returno == "yes":
        print ("continuing")
        returnq=(input("""Please select an option below:
1 - KAMAR
2 - Google Classroom
3 - Google Drive  
4 - Google docs/slides
5 - Other

""").strip().lower())



    if returnq == "1":
        print ("'Main menu' selected")
    elif returnq == "2":
        print ("'Device Type menu' selected")
    elif returnq == "3":
        print("'Device OS menu' selected")
    elif returnq == "4":
        print ("'Issues menu' selected")
    else:
        print ("Unrecognised input, please try again")

    print ('\n')
    
    if returnq == "1" or returnq =="2" or returnq =="3" or returnq=="4" or returnq=="5":
        contq = input("Have you selected the correct option? (y or n) ").strip().lower()
        print ('\n')
        if (contq == "y" or contq == "yes"):
            if returnq == "1":
                print ("mm")
            elif returnq == "2":
                print ("DT")
            elif returnq == "3":
                print ("DOS")
            elif returnq == "4":
                print ("I")
            else:
                ()
            print ("Continuing")
            print ('\n')
            
        elif contq == "n" or contq == "no":
            print ("Stopping")
            print ('\n')
                                
        else:
            print(f"Unrecognised input")  
            print ('\n')
    

    elif returno == "n" or returno == "no":
        print ("Exiting...")
        exit()

    else:
        ()
    











def returntomenu2():
    while True:
        global returnq
        returno = (input("Would you like to re-use this tool? "))
        returnol = returno.strip().lower()
        if returnol == "y" or returnol == "yes":
            print("continuing")
            print ('\n')
            returnq = (input("""Please select an option below:
    1 - Main menu
    2 - Device Type menu
    3 - Device OS menu
    4 - Issues menu
    5 - Exit this program (Choosing this option will close this program)

    """))
            returnql=returnq.strip().lower()

            if returnql == "1":
                print("'Main menu' selected")
            elif returnql == "2":
                print("'Device Type menu' selected")
            elif returnql == "3":
                print("'Device OS menu' selected")
            elif returnql == "4":
                print("'Issues menu' selected")
            elif returnql == "5":
                print("'Exit program' selected")
            else:
                print("Unrecognised input, please try again")

            print('\n')

            if returnql == "1" or returnql == "2" or returnql == "3" or returnql == "4" or returnql == "5":
                contq = input("Have you selected the correct option? (y or n) ")
                contql = contq.strip().lower()
                print('\n')
                if (contql == "y" or contql == "yes"):
                    if returnql == "1":
                        print ("IQ")
            
                    elif returnql == "2":
                        print ("DT")
                    elif returnql == "3":
                        print ("DOS")
                    elif returnql == "4":
                        print ("MM")
                    elif returnql == "5":
                        print("Exiting...")
                        time.sleep(3)
                        exit()
                    else:
                        ()

                elif contql == "n" or contql == "no":
                    print("Stopping")
                    print('\n')

                else:
                    print(f"Unrecognised input")
                    print('\n')

        elif returnol == "n" or returnol == "no":
            print("Exiting...")
            time.sleep(3)
            exit()

        else:
            print(f"Unrecognised input 2")
            print ('\n')

returntomenu2()