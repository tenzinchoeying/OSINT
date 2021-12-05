from tkinter import *
window = Tk()
window.geometry("770x600")
window.title("OSINT Dashboard")

#hides Twitter Inputs
def hideTwitterWidget(widget1, widget2, widget3, widget4, widget5, widget6, widget7, widget8, widget9, widget10, widget11):
    widget1.grid_remove()
    widget2.grid_remove()
    widget3.grid_remove()
    widget4.grid_remove()
    widget5.grid_remove()
    widget6.grid_remove()
    widget7.grid_remove()
    widget8.grid_remove()
    widget9.grid_remove()
    widget10.grid_remove()
    widget11.grid_remove()

def clearCrawler(widget1, widget2, widget3, widget4):
    widget1.grid_remove()
    widget2.grid_remove()
    widget3.grid_remove()
    widget4.grid_remove()
    
def crawler():
    lblUrl = Label(window, text= "Enter URL:", font = ("Helvetica", 15))
    lblUrl.grid(row = 2, column = 0)
    urlEntry = Entry(window, font = ("Helvetica", 15))
    urlEntry.grid(row=2, column = 1)

    bSumbit = Button(window, text = "Sumbit", font = ("Helvetica", 15), bg = "#c7c7c7", relief = RAISED, command=lambda: func("Sumbit Button Works"))
    bSumbit.grid(row = 3, column = 1, pady = 10)
    
    bClear = Button(window, text = "Clear", font = ("Helvetica", 15), bg = "#c7c7c7",relief = RAISED,
                    command=lambda:clearCrawler(lblUrl, urlEntry, bClear, bSumbit))
    bClear.grid(row = 3, column = 0, pady = 10)
#prints message in console    
def func(message):
    print(message)

#display Complete Widget    
def complete(win, message, row, column):
    lblComplete = Label(win, text= message, font = ("Helvetica", 15))
    lblComplete.grid(row = row, column = column)

#Display Twitter Scraping Window                         
def twitterScraping():
    scraping = Tk()
    scraping.geometry("400x250")
    scraping.title("Scraping Window")
    
    lblHashtag = Label(scraping, text= "Enter Twitter Hashtag to Search:", font = ("Helvetica", 15))
    lblHashtag.grid(row = 0, column = 0)
    hashtagEntry = Entry(scraping, font = ("Helvetica", 15))
    hashtagEntry.grid(row=1, column = 0)
    
    lblDate = Label(scraping, text= "Enter date since the Tweets (yyyy-mm--dd):", font = ("Helvetica", 15))
    lblDate.grid(row = 2, column = 0)
    dateEntry = Entry(scraping, font = ("Helvetica", 15))
    dateEntry.grid(row=3, column = 0)

    bSumbit = Button(scraping, text = "Sumbit", font = ("Helvetica", 15), bg = "#c7c7c7", relief = RAISED, command=lambda: complete(scraping, "Scraping Complete! Close Window.", 5, 0))
    bSumbit.grid(row = 4, column = 0)
    
#Display Twitter Extracting Window     
def twitterExtracting():
    extracting = Tk()
    extracting.geometry("350x250")
    extracting.title("Extracting Window")
    
    lblTwitterId = Label(extracting, text= "Enter Twitter ID:", font = ("Helvetica", 15))
    lblTwitterId.grid(row = 0, column = 0)
    twitterIdEntry = Entry(extracting, font = ("Helvetica", 15))
    twitterIdEntry.grid(row=1, column = 0)
    
    lblNum = Label(extracting, text= "Enter Number of Tweets Extracted:", font = ("Helvetica", 15))
    lblNum.grid(row = 2, column = 0)
    numEntry = Entry(extracting, font = ("Helvetica", 15))
    numEntry.grid(row=3, column = 0)

    bSumbit = Button(extracting, text = "Sumbit", font = ("Helvetica", 15), bg = "#c7c7c7", relief = RAISED,
                     command=lambda: complete(extracting, "Extracting Complete! Close Window.", 5, 0))
    bSumbit.grid(row = 4, column = 0)
    
def twitterSearch():
    #Token and Key entry
    lblKey = Label(window, text= "Enter Consumer Key:", font = ("Helvetica", 15))
    lblKey.grid(row = 5, column = 0, columnspan = 2)
    keyEntry = Entry(window, font = ("Helvetica", 15))
    keyEntry.grid(row=5, column = 1, columnspan = 3)
    
    lblSecret = Label(window, text= "Enter Consumer Key Secret:", font = ("Helvetica", 15))
    lblSecret.grid(row = 6, column = 0, columnspan = 2)
    secretEntry = Entry(window, font = ("Helvetica", 15))
    secretEntry.grid(row=6, column = 1, columnspan = 3)
    
    lblToken = Label(window, text= "Enter Access Token:", font = ("Helvetica", 15))
    lblToken.grid(row = 8, column = 0, columnspan = 2)
    tokenEntry = Entry(window, font = ("Helvetica", 15))
    tokenEntry.grid(row=8, column = 1, columnspan = 3)

    lblTokenSecret = Label(window, text= "Enter Secret Access Token:", font = ("Helvetica", 15))
    lblTokenSecret.grid(row = 9, column = 0, columnspan = 2)
    tokenSecretEntry = Entry(window, font = ("Helvetica", 15))
    tokenSecretEntry.grid(row=9, column = 1, columnspan = 3)
    
    #Clear, Extracting and Scraping Button
    bScraping = Button(window, text = "Scraping", font = ("Helvetica", 15), bg = "#c7c7c7", relief = RAISED, command=lambda: twitterScraping())
    bScraping.grid(row = 10, column = 1, columnspan = 2, pady = 10)

    bExtracting = Button(window, text = "Extracting", font = ("Helvetica", 15), bg = "#c7c7c7", relief = RAISED, command=lambda: twitterExtracting())
    bExtracting.grid(row = 10, column = 3, columnspan = 2, pady = 10)
    
    bClear = Button(window, text = "Clear", font = ("Helvetica", 15), bg = "#c7c7c7",relief = RAISED,
                    command=lambda: hideTwitterWidget(lblKey, keyEntry, lblSecret, secretEntry, lblToken, tokenEntry, lblTokenSecret, tokenSecretEntry, bScraping, bExtracting, bClear))
    bClear.grid(row = 10, column = 0, pady = 10)

#Main Dashboard Widgets
lbl=Label(window, text="OSINT Dashboard", fg='white', bg = "#68befc",  font=("Helvetica", 70))
lbl.grid(row = 0, column = 0,columnspan = 4)

bTwitter = Button(window, text = "\n   Twitter   \n", fg = 'white', bg = "#2b4ed9", font=("Helvetica", 20), relief = RAISED,command=lambda: twitterSearch())
bTwitter.grid(row = 1, column = 0, pady = 35)

bWebCrawler = Button(window, text = "\n  WebCrawler  \n", fg = 'white', bg = "#2b4ed9", font=("Helvetica", 20), relief = RAISED,
                     command=lambda: crawler())
bWebCrawler.grid(row = 1, column = 1, pady = 35)

bGIR = Button(window, text = "Generate \nIntelligence \nReport", fg = 'white', bg = "#f5b36c", font=("Helvetica", 20), relief = RAISED,command=lambda: func("GIR Button Works"))
bGIR.grid(row =1, column = 2, pady = 35)

bCGM = Button(window, text = "Capture And \nGenerate \nMetadata", fg = 'white', bg = "#f5b36c", font=("Helvetica", 20), relief = RAISED,command=lambda: func("CGM Button Works"))
bCGM.grid(row = 1, column = 3, pady = 35)

window.mainloop()

'''
bFacebook = Button(window, text = "Facebook", fg = 'white', bg = "#2b4ed9", font=("Helvetica", 20), relief = RAISED,command=lambda: func("Facebook Button Works"))
bFacebook.grid(row = 1, column = 0, pady = 35)

bGoogle = Button(window, text = "Google+", fg = 'white', bg = "#2b4ed9", font=("Helvetica", 20), relief = RAISED,command=lambda: func("Google+ Button Works"))
bGoogle.grid(row = 1, column = 2, pady = 35)


bMetaData = Button(window, text = "MetaData \nSearch", fg = 'white', bg = "#2b4ed9", font=("Helvetica", 20), relief = RAISED,command=lambda: func("Metasearch Data Button Works"))
bMetaData.grid(row = 1, column = 4, pady = 35)


bInsta = Button(window, text = "Instagram", fg = 'white', bg = "#2b4ed9", font=("Helvetica", 20), relief = RAISED,command=lambda: func("Instagram Button Works"))
bInsta.grid(row = 2, column = 2, pady = 35)


bEXIF = Button(window, text = "EXIF Data \nSearch", fg = 'white', bg = "#2b4ed9", font=("Helvetica", 20), relief = RAISED,command=lambda: func("EXIF Data Button Works"))
bEXIF.grid(row = 2, column = 4, pady = 35)


bLinkedin = Button(window, text = "Linkedin", fg = 'white', bg = "#2b4ed9", font=("Helvetica", 20), relief = RAISED,command=lambda: func("Linkedin Button Works"))
bLinkedin.grid(row = 3, column = 0, pady = 35)

bOther = Button(window, text = "Other \nSearch", fg = 'white', bg = "#2b4ed9", font=("Helvetica", 20), relief = RAISED,command=lambda: func("Other Button Works"))
bOther.grid(row = 3, column = 4, pady = 35)


bGDC = Button(window, text = "Generate \nData \nCollection", fg = 'white', bg = "#f5b36c", font=("Helvetica", 20), relief = RAISED,command=lambda: func("GDC Button Works"))
bGDC.grid(row = 4, column = 4, pady = 35)
'''

