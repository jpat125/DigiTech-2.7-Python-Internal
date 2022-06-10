def audioissue():
    while True:
        audioissuev=(int(input("""I am having issues with:
1 - Connecting to projector or TV
2 - Connecting to speakers
3 - Other

""")))
        if audioissuev == 1:
            print ("connecting to projector/tv")
            
        elif audioissuev == 2:
            print("connecting to speakers")
            
        elif audioissuev == 3:
            print ("Other")
        
        else:
            print ("Unrecognised input, please try again") 

        print ('\n')
        contq = input("Do you wish to continue? (y or n) ").strip().lower()
        print ('\n')
        if (contq == "y" or contq == "yes") and (audioissuev == 1 or audioissuev ==  2 or audioissuev ==  3):
            print ("Continuing")
            print ('\n')
            break
        elif contq == "n" or contq == "no":
            print ("Stopping")
            print ('\n')                
        else:
            print("Unrecognised input")  
            print ('\n')

audioissue()