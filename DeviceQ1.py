
def devq1():
    
    while True:
        global devq1v
        devq1v = (int(input("""Please select one of the options below:
1 - Display issue (including projecting)
2 - Wi-Fi issues
3 - File issues
4 - Audio issues
5 - Error codes
6 - Other


""").strip().lower()))
        if devq1v == 1:
            print("display issues")#leads to display issues question
        elif devq1v == 2:
            print ("wifi issues")#leads to wifi issues question
        elif devq1v == 3:
            print ("file issues")#leads to file issues issues question
        elif devq1v == 4:
            print ("audio issues")#leads to audio issues question
        elif devq1v == 5:
            print ("Error code")#leads to google search
        elif devq1v == 6:
            print ("other")#lead to google search
        else:
            print ("Unrecognised input")
        
        print ('\n')
        contq = input("Do you wish to continue? (y or n) ").strip().lower()
        print ('\n')
        if (contq == "y" or contq == "yes") and (devq1v == 1 or devq1v == 2 or devq1v == 3 or devq1v == 4):    
            print ("Continuing")
            print ('\n')
            break
        elif contq == "n" or contq == "no":
                    print ("Stopping")
                    print ('\n')
                            
        else:
            print("Unrecognised input")  
            print ('\n')

devq1()