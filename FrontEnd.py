import crawler
import Twitter_Hashtag_Scraper as hash
import Twitter_IPScraper as ips
import tkinter as tk

window = tk.Tk()
window.geometry("770x600")
window.title("OSINT Dashboard")

key_var = tk.StringVar()
sKey_var = tk.StringVar()
token_var = tk.StringVar()
sToken_var = tk.StringVar()
hashtag_var = tk.StringVar()
date_var = tk.StringVar()
id_var = tk.StringVar()
num_var = tk.StringVar()
url_var = tk.StringVar()

def crawlerSumbit():
    url = url_var.get()
    print("URL is: " + url)
    url_var.set("")

def hashSumbit():
    key = key_var.get()
    sKey = sKey_var.get()
    token = token_var.get()
    sToken = sToken_var.get()
    hashtag = hashtag_var.get()
    date = date_var.get()

    print("key is: " + key)
    print("sKey is: " + sKey)
    print("Token is: " + token)
    print("sToken is: " + sToken)
    print("Hashtag is: " + hashtag)
    print("Date is: " + date)

    key_var.set("")
    sKey_var.set("")
    token_var.set("")
    sToken_var.set("")
    hashtag_var.set("")
    date_var.set("")
    
def idSumbit():
    key = key_var.get()
    sKey = sKey_var.get()
    token = token_var.get()
    sToken = sToken_var.get()
    twitterId = id_var.get()
    num = num_var.get()

    print("key is: " + key)
    print("sKey is: " + sKey)
    print("Token is: " + token)
    print("sToken is: " + sToken)
    print("Twitter ID is: " + twitterId)
    print("Num is: " + num)

    key_var.set("")
    sKey_var.set("")
    token_var.set("")
    sToken_var.set("")
    id_var.set("")
    num_var.set("")

#hides Twitter Inputs
def hideTwitterWidget(widget1, widget2, widget3, widget4, widget5, widget6, widget7, widget8, widget9, widget10, widget11, widget12, widget13, widget14):
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
    widget12.grid_remove()
    widget13.grid_remove()
    widget14.grid_remove()

def clearCrawler(widget1, widget2, widget3, widget4):
    widget1.grid_remove()
    widget2.grid_remove()
    widget3.grid_remove()
    widget4.grid_remove()
    
def crawler():
    lblUrl = tk.Label(window, text= "Enter URL:", font = ("Helvetica", 15))
    lblUrl.grid(row = 2, column = 0)
    urlEntry = tk.Entry(window, font = ("Helvetica", 15), textvariable = url_var)
    urlEntry.grid(row=2, column = 1)

    bSumbit = tk.Button(window, text = "Sumbit", font = ("Helvetica", 15), bg = "#c7c7c7", relief = tk.RAISED, command=lambda: crawlerSumbit())
    bSumbit.grid(row = 3, column = 1, pady = 10)
    
    bClear = tk.Button(window, text = "Clear", font = ("Helvetica", 15), bg = "#c7c7c7",relief = tk.RAISED,
                    command=lambda:clearCrawler(lblUrl, urlEntry, bClear, bSumbit))
    bClear.grid(row = 3, column = 0, pady = 10)

#Display Twitter Extracting Window     
def twitterId():
    #Token, Number, Id, and Key entry
    lblKey = tk.Label(window, text= "Enter Consumer Key:", font = ("Helvetica", 15))
    lblKey.grid(row = 5, column = 0)
    keyEntry = tk.Entry(window, font = ("Helvetica", 15), textvariable = key_var)
    keyEntry.grid(row=5, column = 1)
    
    lblSecret = tk.Label(window, text= "Enter Consumer Key Secret:", font = ("Helvetica", 15))
    lblSecret.grid(row = 6, column = 0)
    secretEntry = tk.Entry(window, font = ("Helvetica", 15), textvariable = sKey_var)
    secretEntry.grid(row=6, column = 1)
    
    lblToken = tk.Label(window, text= "Enter Access Token:", font = ("Helvetica", 15))
    lblToken.grid(row = 8, column = 0)
    tokenEntry = tk.Entry(window, font = ("Helvetica", 15), textvariable = token_var)
    tokenEntry.grid(row=8, column = 1)

    lblTokenSecret = tk.Label(window, text= "Enter Secret Access Token:", font = ("Helvetica", 15))
    lblTokenSecret.grid(row = 9, column = 0)
    tokenSecretEntry = tk.Entry(window, font = ("Helvetica", 15), textvariable = sToken_var)
    tokenSecretEntry.grid(row=9, column = 1)
    
    lblTwitterId = tk.Label(window, text= "Enter Twitter ID:", font = ("Helvetica", 15))
    lblTwitterId.grid(row = 10, column = 0)
    twitterIdEntry = tk.Entry(window, font = ("Helvetica", 15), textvariable = id_var)
    twitterIdEntry.grid(row=10, column = 1)
    
    lblNum = tk.Label(window, text= "Enter Number of Tweets Extracted:", font = ("Helvetica", 15))
    lblNum.grid(row = 11, column = 0)
    numEntry = tk.Entry(window, font = ("Helvetica", 15), textvariable = num_var)
    numEntry.grid(row=11, column = 1)
    
    #Clear, and Sumbit button
    bSumbit = tk.Button(window, text = "Sumbit", font = ("Helvetica", 15), bg = "#c7c7c7", relief = tk.RAISED, command=lambda: idSumbit())
    bSumbit.grid(row = 13, column = 1, pady = 10)
    
    bClear = tk.Button(window, text = "Clear", font = ("Helvetica", 15), bg = "#c7c7c7",relief = tk.RAISED,
                    command=lambda: hideTwitterWidget(lblKey, keyEntry, lblSecret, secretEntry, lblToken, tokenEntry, lblTokenSecret,
                                                      tokenSecretEntry, lblTwitterId, twitterIdEntry, lblNum, numEntry, bSumbit, bClear))
    bClear.grid(row = 13, column = 0, pady = 10)
    
def twitterHashtag():
    #Token, Hashtag, date, and Key entry
    lblKey = tk.Label(window, text= "Enter Consumer Key:", font = ("Helvetica", 15))
    lblKey.grid(row = 5, column = 0)
    keyEntry = tk.Entry(window, font = ("Helvetica", 15), textvariable = key_var)
    keyEntry.grid(row=5, column = 1)
    
    lblSecret = tk.Label(window, text= "Enter Consumer Key Secret:", font = ("Helvetica", 15))
    lblSecret.grid(row = 6, column = 0)
    secretEntry = tk.Entry(window, font = ("Helvetica", 15), textvariable = sKey_var)
    secretEntry.grid(row=6, column = 1)
    
    lblToken = tk.Label(window, text= "Enter Access Token:", font = ("Helvetica", 15))
    lblToken.grid(row = 8, column = 0)
    tokenEntry = tk.Entry(window, font = ("Helvetica", 15), textvariable = token_var)
    tokenEntry.grid(row=8, column = 1)

    lblTokenSecret = tk.Label(window, text= "Enter Secret Access Token:", font = ("Helvetica", 15))
    lblTokenSecret.grid(row = 9, column = 0)
    tokenSecretEntry = tk.Entry(window, font = ("Helvetica", 15), textvariable = sToken_var)
    tokenSecretEntry.grid(row=9, column = 1)

    lblHashtag = tk.Label(window, text= "Enter Twitter Hashtag to Search:", font = ("Helvetica", 15))
    lblHashtag.grid(row = 10, column = 0)
    hashtagEntry = tk.Entry(window, font = ("Helvetica", 15), textvariable = hashtag_var)
    hashtagEntry.grid(row=10, column = 1)
    
    lblDate = tk.Label(window, text= "Enter date since the Tweets \n(yyyy-mm--dd):", font = ("Helvetica", 15))
    lblDate.grid(row = 11, column = 0)
    dateEntry = tk.Entry(window, font = ("Helvetica", 15), textvariable = date_var)
    dateEntry.grid(row=11, column = 1)
    
    #Clear, and Sumbit button
    bSumbit = tk.Button(window, text = "Sumbit", font = ("Helvetica", 15), bg = "#c7c7c7", relief = tk.RAISED, command=lambda: hashSumbit())
    bSumbit.grid(row = 13, column = 1, pady = 10)
    
    bClear = tk.Button(window, text = "Clear", font = ("Helvetica", 15), bg = "#c7c7c7",relief = tk.RAISED,
                    command=lambda: hideTwitterWidget(lblKey, keyEntry, lblSecret, secretEntry, lblToken, tokenEntry, lblTokenSecret,
                                                      tokenSecretEntry, lblHashtag, hashtagEntry, lblDate, dateEntry, bSumbit, bClear))
    bClear.grid(row = 13, column = 0, pady = 10)

def mainApp():
    #Main Dashboard Widgets
    lbl=tk.Label(window, text="OSINT Dashboard", fg='white', bg = "#68befc",  font=("Helvetica", 70))
    lbl.grid(row = 0, column = 0,columnspan = 3)

    bTwitterHash = tk.Button(window, text = "Twitter \nScrapping\nUsing Hashtag", fg = 'white', bg = "#2b4ed9", font=("Helvetica", 20), relief = tk.RAISED,command=lambda: twitterHashtag())
    bTwitterHash.grid(row = 1, column = 0, pady = 35)

    bTwitterId = tk.Button(window, text = "Twitter \n   Scrapping   \nUsing ID", fg = 'white', bg = "#2b4ed9", font=("Helvetica", 20), relief = tk.RAISED,command=lambda: twitterId())
    bTwitterId.grid(row = 1, column = 1, pady = 35)

    bWebCrawler = tk.Button(window, text = "\n  WebCrawler  \n", fg = 'white', bg = "#2b4ed9", font=("Helvetica", 20), relief = tk.RAISED,
                     command=lambda: crawler())
    bWebCrawler.grid(row = 1, column = 2, pady = 35)

    window.mainloop()

mainApp()


