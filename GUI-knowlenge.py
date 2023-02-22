from tkinter import *
from tkinter import ttk    #theme of tk
from tkinter import messagebox


GUI = Tk()         #นี่คือหน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล') #นี่คือชื่อโปรแกรม
GUI.geometry('500x400') #นี่คือขนาดของโปรแกรม ยาวxสูง

#B1 = ttk.Button(GUI,text='เงินมีอยู่กี่บาท')
#B1.pack(ipadx=20,ipady=20)

##################
def Button2():
    text = 'ตอนนี้มีเงินในบัญชี 300 บาท'
    messagebox.showinfo(' เงินในบัญชี ',text)
   #messagebox.showwarning(' เงินในบัญชี ',text)
  #messagebox.showerror(' เงินในบัญชี ',text)

L1 =Label(GUI,text='ประเมินเงินและวิชาที่จะเลือกเรียน',font=('JS Jetarin italic',20),fg='green',bg='pink')
L1.place(x=150,y=150)
   
FB1=Frame(GUI)   #คล้ายกระดาน
FB1.place(x=180,y=300)


B2 = ttk.Button(FB1,text='เงินมีอยู่กี่บาท',command = Button2)
B2.pack(ipadx=30,ipady=30)
#B2.place(x=50,y=200) #set location

def Button3():
    text = 'เรียนPython101'
    messagebox.showinfo(' เรียนวันที่10-20/2/66 ',text)
   
FB2=Frame(GUI)   #คล้ายกระดาน
FB2.place(x=180,y=200)


B3 = ttk.Button(FB2,text='สัปดาห์นี้เรียนวิชาอะไร',command = Button3)
B3.pack(ipadx=20,ipady=20)

#สร้างFileเมนู
menubar=Menu(GUI)
fileMenu=Menu(menubar)
fileMenu.add_command(label="New")
fileMenu.add_command(label="Open")
fileMenu.add_command(label="Save ..As")
fileMenu.add_command(label="Close")

#สร้างเมนูhelp
helpMenu=Menu(menubar)
helpMenu.add_command(label="About โปรแกรมบันทึกความรู้")
helpMenu.add_command(label="Document")


menubar.add_cascade(label="File",menu=fileMenu)
menubar.add_cascade(label="Help",menu=helpMenu)
GUI.config(menu=menubar)

#สร้างListBox
l1=Listbox()
l1.insert(1,'Python')
l1.insert(2,'JAVA')
l1.insert(3,'Database')
l1.insert(4,'Pygame')
l1.insert(5,'Electronic')
l1.insert(6,'Robotic')
l1.place(x=330,y=200)

#login
in1 =Label(text='Username :')
in2 =Label(text='Password :')
in1.grid(row=0)
in2.grid(row=1)
e1=Entry()
e2=Entry()
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)


btn1=Button(text='Login')
btn1.grid(row=2,column=2)

GUI.mainloop()
##################


GUI.mainloop()
