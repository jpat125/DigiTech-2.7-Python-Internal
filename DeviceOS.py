
def deviceos():
    global deviceosv
    
    while True:
        deviceosv=(input("What is the Operating System of the device? eg. Windows 10, IpadOS, macOS (if unknown, type 'uknown') ").strip().lower())
        if deviceosv == "windows 10":
            print ("Windows 10")
        elif deviceosv =="windows 11":
           print ("Windows 11")
        elif deviceosv == "ipados":
            print ("IpadOS")
        elif deviceosv == "ios":
            print ("IOS")
        elif deviceos == "macos":
            print ("macOS")
        else:
            print ("That doesn't seem to be a supported Operating System, perphaps you have mispelt?")
            
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

deviceos()
