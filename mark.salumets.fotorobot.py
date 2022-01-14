from tkinter import *
a=0
b=0
c=0
d=0


def head():	 
	
	if a==0:
		draw.create_rectangle((15, 15, 290, 290), fill="white", outline="black",width="2")
	
	elif a==1:
		draw.create_oval((15,15,290,290))
def nose():
	 
	
	if a==0:
	 draw.create_polygon([(150, 163), (181, 163), (150,130 )],fill="grey")



def mouth():
	global c,draw
	
	if a==0:
	 draw.create_line((213, 215, 90, 215),fill="black",width=3)

def eyes():
	if a==0:
	 draw.create_rectangle((72,72,130,130),fill="white")
	 draw.create_oval((165,72,221,130),fill="white")
	 draw.create_rectangle((82,82,117,120),fill="black")
	 draw.create_oval((175,82,211,120),fill="black")
	elif a==1:
	 draw.create_oval((72,72,130,130),fill="white")
	 draw.create_oval((165,72,221,130),fill="white")
	 draw.create_oval((82,82,117,120),fill="black")
	 draw.create_oval((175,82,211,120),fill="black")


def recycle():
	draw.create_rectangle((15, 15, 290, 290), fill="white", outline="white",width="2")

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
head=Checkbutton(f1,text="GOLOVA",font="Calibri 26",fg="black",bg="lightblue",relief=GROOVE,command=head)
eyes=Checkbutton(f1,text="GLAZA",font="Calibri 26",fg="black",bg="lightblue",relief=GROOVE,command=eyes)
nose=Checkbutton(f1,text="NOS",font="Calibri 26",fg="black",bg="lightblue",relief=GROOVE,command=nose)
mouth=Checkbutton(f1,text="ROTIK",font="Calibri 26",fg="black",bg="lightblue",relief=GROOVE,command=mouth)
recycle=Checkbutton(f1,text="режим бога",font="Calibri 26",fg="black",bg="lightblue",relief=GROOVE,command=recycle)

head.pack()
eyes.pack()
nose.pack()
mouth.pack()

recycle.pack()

tk.mainloop()


