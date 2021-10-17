#import time
#from plyer import notification
#notification.notify(
    #title = "  WELCOME to hp ",
   # message = " ADDRESS BOOK IS RUNNING ",
   # app_icon = None,
    #timeout = 30
#)

from tkinter import *
root = Tk()
root.geometry('600x600')
root.config(bg = 'light Blue')
root.title('** ADDRESS BOOK **')    
root.resizable(0,0)
contactlist = [ ]

Name = StringVar()
Number = StringVar()
Gmail =StringVar()
Birthday =StringVar()
City   =StringVar()
Pincode=StringVar()

frame = Frame(root)
frame.pack(side = RIGHT)

scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set, height=12)
scroll.config (command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT,  fill=BOTH, expand=1)


########### function to get select value

def Selected():
    return int(select.curselection()[0])
    

def AddContact():
    contactlist.append([Name.get(), Number.get(), Gmail.get(), Birthday.get(), City.get(),Pincode.get()])
    Select_set()

# fun to edit existing contact(first select the contact then click on view button then edit the contact and then click on edit button)
def EDIT():
    contactlist[Selected()] = [Name.get(), Number.get(), Gmail.get(), Birthday.get(), City.get(),Pincode.get()]
    Select_set()
    
def Addmail():
    Gmail.append([Gmail.get()])
    Select_set()

def birthday():
    Birthday.append([Birthday.get()])
    Select_set()

def pincode():
    Pincode.append([Pincode.get()])

def city():
    City.append([City.get()])
    Select_set()

#to delete selected contact
def DELETE():
    del contactlist[Selected()]
    Select_set()
   
# to view selected contact(first select then click on view button)
def VIEW():
    NAME, PHONE ,GMAIL ,BIRTHDAY ,CITY , PINCODE= contactlist[Selected()]
    Name.set(NAME)
    Number.set(PHONE)
    Gmail.set(GMAIL)
    Birthday.set(BIRTHDAY)
    City.set(CITY)
    Pincode.set(PINCODE)


###exit game window   
def EXIT():
    root.destroy()

#empty name and number field
def RESET():
    Name.set('')
    Number.set('')
    Gmail.set('')
    Birthday.set('')
    City.set('')
    Pincode.set('')


def Select_set() :
    contactlist.sort()
    select.delete(0,END)
    for name,phone,gmail,birthday,city,pincode in contactlist :
        select.insert (END, name)
Select_set()



######define buttons #####labels and entry widget
Label(root, text = 'NAME', font='Cambria 14 bold', bg = 'SlateGray3').place(x= 30, y=20)
Entry(root, textvariable = Name).place(x= 100, y=20)
Label(root, text = 'PHONE NO.', font='Cambria 14  bold',bg = 'SlateGray3').place(x= 30, y=55)
Entry(root, textvariable = Number).place(x= 140, y=60)
Label(root, text = 'Gmail', font='Cambria 14  bold',bg = 'SlateGray3').place(x= 30, y=90)
Entry(root, textvariable = Gmail).place(x= 130, y=95)
Label(root, text = 'Birthday', font='Cambria 14  bold',bg = 'SlateGray3').place(x= 30, y=130)
Entry(root, textvariable = Birthday).place(x= 140, y=135)
Label(root, text = 'City', font='Cambria 14  bold',bg = 'SlateGray3').place(x= 38, y=170)
Entry(root, textvariable = City).place(x= 160, y=170)
Label(root, text = 'Pincode', font='Cambria 14  bold',bg = 'SlateGray3').place(x= 30, y=205)
Entry(root, textvariable = Pincode).place(x= 150, y=200)
Label(root, text = 'WELCOME TO ', font='Arial 22 bold',bg = 'Green').place(x= 320, y=10)
Label(root, text = 'MY PHONEBOOK', font='Arial 22 bold',bg = 'Green').place(x= 320, y=50)


Button(root,text=" ADD", font='Cambria 14 bold',bg='Red', command = AddContact).place(x= 100, y=250)
Button(root,text="EDIT", font='Cambria 14  bold',bg='light Blue',command = EDIT).place(x= 100, y=300)
Button(root,text="DELETE", font='Cambria 14  bold',bg='light Green',command = DELETE).place(x= 100, y=350)
Button(root,text="VIEW", font='Cambria 14  bold',bg='light Yellow', command = VIEW).place(x= 100, y=400)
Button(root,text="EXIT", font='Cambria 14  bold',bg='tomato', command = EXIT).place(x= 500, y=400)
Button(root,text="RESET", font='Cambria 14  bold',bg='SlateGray3', command = RESET).place(x= 100, y=450)
root.mainloop()