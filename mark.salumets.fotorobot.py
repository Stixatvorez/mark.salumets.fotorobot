from tkinter import *
a=0
b=0
c=0
d=0

def head():
	global a,draw
	if a==0:
		#draw.create_oval((5,5,290,290))
		a=1
	elif a==1:
		draw.create_rectangle((15, 15, 290, 290), fill="white", outline="black",width="2")
def nose():
	draw.create_polygon([(150, 163), (181, 163), (150,130 )],fill="grey")

def mouth():
	draw.create_line((213, 215, 90, 215),fill="black",width=3)

def eyes():
	draw.create_rectangle((72,72,130,130),fill="white")
	draw.create_oval((165,72,221,130),fill="white")
	draw.create_rectangle((82,82,117,120),fill="black")
	draw.create_oval((175,82,211,120),fill="black")

tk=Tk()
tk.title("ФОТОБОБЕР")
tk.geometry("700x300")
f1=Frame(tk,width=300,height=300)
f2=Frame(tk,width=400,height=300)
draw=Canvas(f2,width=300,height=300)
draw.pack()
f1.pack(side=LEFT)
f2.pack(side=RIGHT)
name=Label(f1,text="Создание фотобобра",font="Calibri 26",fg="black",bg="lightblue",justify=CENTER)
name.pack(side=TOP)
head=Checkbutton(f1,text="golova",font="Calibri 26",fg="black",bg="lightblue",relief=GROOVE,command=head)
eyes=Checkbutton(f1,text="glaza",font="Calibri 26",fg="black",bg="lightblue",relief=GROOVE,command=eyes)
nose=Checkbutton(f1,text="nos",font="Calibri 26",fg="black",bg="lightblue",relief=GROOVE,command=nose)
mouth=Checkbutton(f1,text="rotik",font="Calibri 26",fg="black",bg="lightblue",relief=GROOVE,command=mouth)

head.pack()
eyes.pack()
nose.pack()
mouth.pack()

tk.mainloop()


