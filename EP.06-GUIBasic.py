 
from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime
import csv


GUI = Tk()
GUI.title("Expense Calculation Program")
GUI.geometry("600x700")

#-----Menu--------------------------
menubar = Menu(GUI)
GUI.config(menu=menubar)

# file menu
filemenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='File',menu=filemenu)
filemenu.add_command(label='Open')
# help menu
def About():
	messagebox.showinfo('About','Hello this is my first program')

helpmenu = Menu(menubar,tearoff=0)
menubar.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_command(label='About',command=About)




#--------Add Tab Into Program------------
Tab = ttk.Notebook(GUI)
T1 = Frame(Tab)
T2 = Frame(Tab)
Tab.pack(fill=BOTH,expand=1)

icon_T1 = PhotoImage(file='t1_btc.png').subsample(2) # .subsample(2) ย่อรูปลง 2 เท่า
icon_T2 = PhotoImage(file='t2_eth.png').subsample(2) 


Tab.add(T1,text=f'{"Add Expense":^{60}}',image=icon_T1,compound="left")       # ใช้ f-string ทำให้ข้อความอยู่กลาง Tab ที่มีขนาด60ตัวอักษร
Tab.add(T2,text=f'{"Total Expense":^{60}}',image=icon_T2,compound="left")

#----------------------------------------------------------

F1=Frame(T1)
F1.place(x=125,y=50)

days = {"Mon":"จันทร์",
		"Tue":"อังคาร",
		"Wed":"พุธ",
		"Thu":"พฤหัสบดี",
		"Fri":"ศุกร์",
		"Sat":"เสาร์",
		"Sun":"อาทิตย์"}

def save(event = None):
	
	item = v_item.get()
	price = v_price.get()
	quan = v_quan.get()
	
	if item == "" and price == "" and quan == "":
		messagebox.showwarning("Error","กรุณากรอกข้อมูลให้ครบ")
		return
	elif item =="":
		messagebox.showwarning("Error","Please Insert Item")
		return	
	elif price =="":
		messagebox.showwarning("Error","Please Insert Price")
		return	
	elif quan =="":
		messagebox.showwarning("Error","Please Insert Quantity")
		return

	try:

		total = int(price)*int(quan)
		today = datetime.now().strftime("%a")
		dt = datetime.now().strftime(f"%Y-%m-%d-%H:%M:%S")
		dt = days[today] + "-" + dt
	
		print(f"You buy : {item}\nprice : {price}\nquantity : {quan}\ntotal cost : {total}")
		print(f"saved time : {dt}")

		text = f"You buy : {item}\nprice : {price}\nquantity : {quan}\ntotal cost : {total}"

		v_result.set(text)
		v_item.set("")
		v_price.set("")
		v_quan.set("")
		Slot1.focus()
			
		with open("savefile.csv","a",encoding="utf-8",newline="") as d:
			fw = csv.writer(d)
			data = [item,price,quan,total,dt]
			fw.writerow(data)
	except:
		print("Error")
		#messagebox.showerror("Error","กรุณากรอกข้อมูลใหม่คุณกรอกเลขผิด")
		#messagebox.showwarning("Error","กรุณากรอกข้อมูลใหม่คุณกรอกเลขผิด")
		messagebox.showinfo("Error","กรุณากรอกข้อมูลใหม่คุณกรอกเลขผิด")
		v_item.set("")
		v_price.set("")
		v_quan.set("")
		Slot1.focus()

	update_data()

GUI.bind("<Return>",save)


FONT = ("Hack",10)

#----------------------------------------------------------
L = ttk.Label(F1,text="Item",font=FONT)
L.pack()
v_item = StringVar() 
Slot1 = ttk.Entry(F1,textvariable=v_item,font=FONT)
Slot1.pack()
#----------------------------------------------------------

#----------------------------------------------------------
L = ttk.Label(F1,text="Price",font=FONT).pack()
v_price = StringVar()  
Slot2 = ttk.Entry(F1,textvariable=v_price,font=FONT).pack()
#----------------------------------------------------------

#----------------------------------------------------------
L = ttk.Label(F1,text="Quantity",font=FONT).pack()
v_quan = StringVar()
Slot3 = ttk.Entry(F1,textvariable=v_quan,font=FONT).pack()
#----------------------------------------------------------

icon_B1 = PhotoImage(file="b_save.png")

B1 = ttk.Button(F1,text=f'{"save":^{10}}',command=save,image=icon_B1,compound="left")
B1.pack()

#----------------Tab 2------------------------------------
F2 = Frame(T2)
F2.pack()

#############################################################
def read_csv():
	with open('savefile.csv',newline='',encoding='utf-8') as f:
		fr = csv.reader(f)
		fr_data=list(fr)
		print(fr_data)
	return fr_data			# return เพื่อนำค่าไปใช้งานต่อได้****

read_csv()


# table

L = ttk.Label(T2,text='Result',font=FONT)
L.pack()

header = ['List','Price','Quantity','Total','Date']
resulttable = ttk.Treeview(T2,columns=header,show='headings',height=10)
resulttable.pack()

#for i in range(len(header)):
#	resulttable.heading(header[i],text=header[i])

for h in header:
	resulttable.heading(h,text=h)

headerwidth = [100,100,100,100,100]


for h,w in zip(header,headerwidth):
	resulttable.column(h,width=w)

#resulttable.insert('','end',value=[1,2,3,4,5])

def update_data():
	resulttable.delete(*resulttable.get_children())
	#for c in resulttable.get_children():
	#	resulttable.delete(c)
	data = read_csv()
	for d in data:
		resulttable.insert('',0,value=d)

update_data()










v_result = StringVar()
v_result.set("Result")
result = ttk.Label(F1,textvariable=v_result,font=FONT)
result.pack(ipady=20)



GUI.mainloop()
