def displayissue():
    while True:
        displayissue=(int(input("""Please type the number that best represents your display issue:
    1 - Issue with casting 
    2 - Issue with mirroring 
    3 - Issue with Apple TV
    4 - Other 

    """)))
        if displayissue == 1:
            print ("Casting")
        elif displayissue == 2:
            print ("Mirroring")

            
        print ('\n')
        contq = input("Do you wish to continue? (y or n) ").strip().lower()
        
        print ('\n')
        if contq == "y" or contq == "yes":
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