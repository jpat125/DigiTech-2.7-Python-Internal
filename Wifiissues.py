def wifissue():
    while True:
        wifiissuev=(int(input("""I am having issues with:
1 - Connecting
2 - Remaining connected
3 - Other

""")))
        if wifiissuev == 1:
            print ("connecting issues")
            
        elif wifiissuev == 2:
            print("remaining connected issue")
            
        elif wifiissuev == 3:
            print ("Other")
        
        else:
            print ("Unrecognised input, please try again") 

        print ('\n')
        contq = input("Do you wish to continue? (y or n) ").strip().lower()
        print ('\n')
        if (contq == "y" or contq == "yes") and (wifiissuev == 1 or wifiissuev ==  2 or wifiissuev ==  3):
            print ("Continuing")
            print ('\n')
            break
        elif contq == "n" or contq == "no":
            print ("Stopping")
            print ('\n')                
        else:
            print("Unrecognised input")  
            print ('\n')

wifissue()