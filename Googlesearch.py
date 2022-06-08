import webbrowser
import time
def googlesearch():
    taburl=("https://www.google.com/search?q=")
    querey=(input("Input query: "))
    search=(taburl+querey)
    webbrowser.open(search)
    time.sleep (1.5)

googlesearch()
