from tkinter import *
import pyshorteners
 

root=Tk()
root.title("URL Shortener using pyhton ")
root.geometry("800x300")

def myUrl():
    url_entry= url.get()
    result=pyshorteners.Shortener().tinyurl.short(url_entry) 
    #Access_Token = "3e1a2cd3a5fffc994978e4b32b20db1c48a5c7f7" #token was been created using bitly account
    #short_url = pyshorteners.Shortener(api_key = Access_Token)
    #result2=short_url.bitly.short(url_entry)
    urlEntry.insert(END,result)

Label(root,text="URL shortener using python ",font=('Ivy 20 bold'),fg="Purple").pack(pady=10)


frame1=Frame(root)
Label(frame1,text="Enter URL Here :", font=("Georgia 15 bold")).pack(side=LEFT)
url=Entry(frame1,width="40",font=("Georgia 15 "))
url.pack()
frame1.pack(pady=10)

Button(root,text="Generate Link ", font=('Georgia 15 bold'), command=myUrl).pack(pady=10)

#creating frame2
frame2=Frame(root)
Label(frame2, text="The tinyurl link  :" , font=("Georgia 12 bold")).pack(side=LEFT)
urlEntry = Entry(frame2, width="25" , fg="blue",font=("Georgia 15 "))
urlEntry.pack()
frame2.pack(pady=10)



root.mainloop()

