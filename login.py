from tkinter import * 
import tkinter
import pymysql
  
from tkinter import messagebox
conobj = pymysql.connect (host= 'localhost', user= 'root', password='')
curobj = conobj.cursor () 
#curobj . execute ('create database MCQEXAM;')
#curobj . execute ('use MCQEXAM;' )
#curobj .execute ('create table UESR (FName varchar (30), LName varchar (20), UserId varchar(30) primary key , Gender varchar (7), Dept varchar (20), Password  varchar (20)); ')
curobj.close ()
conobj.close()
#print (dir (tkinter))
win = Tk () 
#win. geometry ('450x450')
win.maxsize(700, 500)
win.minsize(700, 500)
win.title("login Page")

def Login ():
	user = uid.get ()
	dept=  menu.get ()
	password =  pwd.get ()
	#print ("user id", user, "dept=", dept, "password=", password)
	conobj = pymysql.connect(host='localhost', user='root', password= '')
	curobj= conobj.cursor()
	curobj.execute('use MCQEXAM;')
	test = f'select * from uesr where UserId = "{user}" and Password= "{password}" and Dept = "{dept}";'
	curobj.execute(test) 
	record = curobj.fetchall () 
	if len (record) : 
		#print ("welcome to home page ")
		messagebox.showinfo ( "Title", "Welcome to home page")
		win.destroy()
		from mcq import myQuiz
		quiz = myQuiz()
	else : 
		#print ("try again")
		messagebox.showinfo ( "my message ", "Try Again")
		win.destroy() 

	curobj.close()
	conobj.close()
def NewUser() :
	win.destroy () 
	win1 = Tk ()
	def Submit () :
		conobj = pymysql.connect (host= 'localhost', user= 'root', password='')
		curobj = conobj.cursor () 
		curobj . execute ('use MCQEXAM;' )
		fn =nfname . get ()
		ln= nlname . get ()
		nuser= nuid .get ()
		ge = var . get	()
		ndept = nmenu .get ()
		npassword= npwd . get ()
		#print (fn , " ", ln, " ", nuser, " ", ge, " ", ndept, " ", npassword)
		r1 ='insert into UESR values("{FName}","{LName}","{UserId}", "{Gender}","{Dept}", "{Password}");'
		r = r1.format (FName=fn,LName=ln,UserId=nuser,Gender=ge,Dept=ndept, Password = npassword)
		curobj.execute(r)
		conobj.commit () 
		curobj.close ()
		conobj.close()
		win1.destroy() 

	def SignReSet () :
		nfname . delete(0, END) 
		nlname . delete(0,END)
		nuid . delete (0,END)
		var . set (None)
		nmenu . set (None)
		npwd . delete(0,END)

	win1.maxsize(900, 700)
	win1.minsize(900, 700)
	win1.title("SignUp Page")
	Label (win1, text = "Please SignUp Here", font = ('Condensed', 20), fg = "red", bg = "blue" ).place (x= 250, y = 30)

	Label (win1, text = "Enter First Name", font = ('Condensed', 15), fg = "black", bg = "#c0c0c0",relief= RAISED, width= 30 ).place (x= 100, y = 100)

	nfname= Entry (win1,font = ('Condensed', 15), bg="#c1c1c1", fg= "blue", width= 22 )
	nfname.place(x= 450 , y = 100)

	Label (win1, text = "Enter Last Name", font = ('Condensed', 15), fg = "black", bg = "#c0c0c0",relief= RAISED, width= 30 ).place (x= 100, y = 170)

	nlname= Entry (win1,font = ('Condensed', 15), bg="#c1c1c1", fg= "blue", width= 22 )
	nlname.place(x= 450 , y = 170)

	Label (win1, text = "Enter UserId", font = ('Condensed', 15), fg = "black", bg = "#c0c0c0" ,relief= RAISED, width= 30).place (x= 100, y = 240)
	nuid= Entry (win1,font = ('Condensed', 15), bg="#c1c1c1", fg= "blue", width= 22 )
	nuid.place(x= 450 , y = 240)

	Label (win1, text = "Select Gender", font = ('Condensed', 15), fg = "black", bg = "#c0c0c0" ,relief= RAISED, width= 30).place (x= 100, y = 310)
	var = StringVar()
	r1= Radiobutton(win1, text= "Male", value = "male", variable = var).place(x= 450, y= 310)
	r2= Radiobutton(win1, text= "FeMale", value="female", variable= var ).place(x= 550, y= 310)

	Label (win1, text = "Select Dept / Branch Name", font = ('Condensed', 15), fg = "black", bg = "#c0c0c0",relief= RAISED, width= 30 ).place (x= 100, y = 380)
	nmenu = StringVar()
	ndrop = OptionMenu (win1,nmenu, "BCA", "BSc.ITM", "BSc. CS", "EEE", "EE", "ME", "Civil")
	ndrop.place(x= 450, y = 380)

	Label (win1, text = "Set New Password", font = ('Condensed', 15), fg = "black", bg = "#c0c0c0",relief= RAISED, width= 30 ).place (x= 100, y = 450)
	npwd= Entry (win1,font = ('Condensed', 15), bg="#c1c1c1", fg= "blue", width= 22, show= "*" )
	npwd.place(x= 450 , y = 450)

	Button (win1, text = "Submit", bg= "brown", fg= "white", width= 10, height= 2,font = ('Condensed', 15), command=Submit).place(x= 250, y = 550)
	Button (win1, text = "ReSet", bg= "brown", fg= "white", width= 10, height= 2,font = ('Condensed', 15), command = SignReSet).place(x= 450, y = 550)

	win1.mainloop () 
def ReSet() :
	uid.delete (0, END)
	menu.set(None) 
	pwd.delete(0,END)

Label (win, text = "Please Login Here", font = ('Condensed', 20), fg = "red", bg = "blue",relief= RAISED, width= 30 ).place (x= 110, y = 50)

Label (win, text = "Enter User Id", font = ('Condensed', 20), fg = "red", bg = "blue",relief= RAISED, width= 15  ).place (x= 120, y = 150)
uid = Entry (win, font = ('Condensed', 18), bg="brown", fg= "white", width= 15	)
uid.place(x= 380, y = 150)

Label (win, text = "Select Dept/ Branch", font = ('Condensed', 20), fg = "red", bg = "blue", relief= RAISED, width= 15 ).place (x= 120, y = 250)
menu = StringVar()
drop = OptionMenu (win,menu, "BCA", "BSc.ITM", "BSc. CS", "EEE", "EE", "ME", "Civil")
drop.place(x= 450, y = 250)

Label (win, text = "Enter Password", font = ('Condensed', 20), fg = "red", bg = "blue",relief= RAISED, width= 15 ).place (x= 120, y = 350, )
pwd= Entry (win, font = ('Condensed', 18), bg="brown", fg= "white", show = "*", width= 15)
pwd.place(x= 380, y = 350)

Button (win, text = "Login", font = ('Condensed', 15), bg= "orange", fg= "blue", command = Login).place(x = 200, y =450)
Button (win, text = "SignUp", font = ('Condensed', 15), bg= "white", fg= "black", command= NewUser).place(x = 350, y =450)
Button (win, text = "ReSet", font = ('Condensed', 15), bg= "orange", fg= "blue", command = ReSet).place(x = 500, y =450)

win.mainloop () 