

oerrorc=input("""What catagory is the isssue related to? 

1 - Display issue (including projecting)
2 - Wi-Fi issues
3 - Printing issues
4 - Audio issues
5 - Other

*Type the number next to option below and press 'ENTER' after typing*

""")

oerrordos = input("""What device and Operating System are you using?

*Type then press 'ENTER' after typing*

""")

oerrordesc = input("""Please describe the error in full detail and how you came across it:

*Type out then press 'ENTER' after typing*

""")


oerrorlformat={"Catagory":oerrorc,
"Device type and OS":oerrordos,
"Description":oerrordesc
}

othererrorslog = [] 

othererrorslog.append(oerrorlformat)

print (othererrorslog)

oels=str(othererrorslog)

file_object = open('othererrors.txt', 'a')
file_object.write('\n')
file_object.write(oels)

file_object.close()