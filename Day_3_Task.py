from tkinter import *
from tkinter import ttk

window = Tk()

window.title("Registration Screen")

window.geometry('1000x500')

window.configure(background = "blue");
Firstname = Label(window ,text = "First Name : ").grid(row = 0,column = 0)
LastName = Label(window ,text = "Last Name : ").grid(row = 1,column = 0)
Email = Label(window ,text = "Email Id : ").grid(row = 2,column = 0)
Mobile = Label(window ,text = "Phone Number : ").grid(row = 3,column = 0)

Firstname1 = Entry(window).grid(row = 0,column = 1)
Lastname1 = Entry(window).grid(row = 1,column = 1)
Email1 = Entry(window).grid(row = 2,column = 1)
Mobile1 = Entry(window).grid(row = 3,column = 1)

gender = Label(window,text='Gender : ').grid(row=4,column=0)
var = IntVar()
R1 = Radiobutton(window, text="Male", variable=var, value=1,).grid(row=4,column=1)

R2 = Radiobutton(window, text="Female", variable=var, value=2,).grid(row=4,column=2)

R3 = Radiobutton(window, text="Others", variable=var, value=3,).grid(row=4,column=3)
SelectAge = Label(window ,text = "Country : ").grid(row = 5,column = 0)
variable = StringVar(window)
variable.set('India') 

country = OptionMenu(window, variable,'India','America','Japan','Europe','Australia').grid(row=5,column=1)

LangKnown = Label(window ,text = "Languages Known : ").grid(row = 6,column = 0)
pythonCheck = Checkbutton(window,text='Python').grid(row=6,column=1)
cCheck = Checkbutton(window,text='C').grid(row=6,column=2)
cPlusPlusCheck = Checkbutton(window,text='C++').grid(row=6,column=3)
javaCheck = Checkbutton(window,text='Java').grid(row=6,column=4)
Skills = Label(window ,text = "Skills : ").grid(row = 7,column = 0)
SkillsTextBox = Text(window,width=20, height=3).grid(row=7,column=1)
yearsExp=Label(window ,text = "Years of experience : ").grid(row=8,column = 0)
yearsExpSpinBox = Spinbox(window, from_=0, to=50).grid(row=8,column=1)
Domain = Label(window ,text = "Domain : ").grid(row = 9,column = 0)
DomainEntry = Entry(window).grid(row = 9,column = 1)
SubmitButton=Button(window,text="Submit").grid(row=10,column=4)
window.mainloop()
