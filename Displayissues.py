def displayissue():
    while True:
        displayissue=(int(input("""Please type the number that best represents your display issue:
    1 - Issue with Apple TV
    2 - Issue with mirroring 
    3 - Issue with connecting to monitor/projector
    4 - Other 

    """)))
        if displayissue == 1:
            print ("Apple TV")
        elif displayissue == 2:
            print ("Mirroring")
        elif displayissue == 3:
            print ("Monitor")
        elif displayissue == 4:
            print ("Other")
        else:
            print("unrecognised input, please try again")


            
        print ('\n')
        contq = input("Do you wish to continue? (y or n) ").strip().lower()
        
        print ('\n')
        if contq == "y" or contq == "yes" and displayissue == 1 or displayissue == 2 or displayissue == 3 or displayissue == 4 :
            print ("Continuing")
            print ('\n')
            break
        elif contq == "n" or contq == "no":
            print ("Stopping")
            print ('\n')                
        else:
            print("Unrecognised input")  
            print ('\n')




displayissue()