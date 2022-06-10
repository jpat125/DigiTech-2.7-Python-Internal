def fileissue():
    while True:
        fileissuev=(int(input("""I am having issues with:
1 - Zipping & Un-zipping files
2 - 
3 - Other

""")))
        if fileissuev == 1:
            print ("Zipping & unzipping")
            
        elif fileissuev == 2:
            print("remaining connected issue")
            
        elif fileissuev == 3:
            print ("Other")
        
        else:
            print ("Unrecognised input, please try again") 

        print ('\n')
        contq = input("Do you wish to continue? (y or n) ").strip().lower()
        print ('\n')
        if (contq == "y" or contq == "yes") and (fileissuev == 1 or fileissuev ==  2 or fileissuev ==  3):
            print ("Continuing")
            print ('\n')
            break
        elif contq == "n" or contq == "no":
            print ("Stopping")
            print ('\n')                
        else:
            print("Unrecognised input")  
            print ('\n')

fileissue()