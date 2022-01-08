from tkinter import *
from tkinter import ttk, messagebox
import csv
from datetime import datetime

GUI = Tk()
GUI.title('โปรแกรมบันทึกค่าใช้จ่าย by JAMENINE')
GUI.geometry('500x500+500+50')

###################MENU####################
menubar = Menu(GUI)
GUI.config(menu=menubar)

# Help
def About():
	messagebox.showinfo('About','Hello This is To Do List Program\nDevelop by JAMENINE')

helpmenu = Menu(menubar)
menubar.add_cascade(label='Help',menu=helpmenu)
helpmenu.add_command(label='About',command=About)

###########################################

#GUI.configure(bg='#0928C8')
F1 = Frame(GUI)
F1.pack()

days = {'Mon':'จันทร์',
		'Tue':'อังคาร',
		'Wed':'พุธ',
		'Thu':'พฤหัสบดี',
		'Fri':'ศุกร์',
		'Sat':'เสาร์',
		'Sun':'อาทิตย์'}

def Save(event=None):
	s_list = v_list.get()

	if s_list == '':
		print('No Data')
		messagebox.showwarning('Error','Please Enter To Do List')
		return
	
	try:
		# บันทึกข้อมูลลง csv อย่าลืม import csv ด้วย
		today = datetime.now().strftime('%a') # days['Mon'] = 'จันทร์'
		print(today)
		dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		dt = days[today] + '-' + dt
		with open('savedata.csv','a',encoding='utf-8',newline='') as f:
		    #with คือสั่งเปิดไฟล์แล้วปิดอัตโนมัติ
			#'a' การบันทึกเรื่อยๆ เพิ่มข้อมูลต่อจากข้อมูลเก่า
			#newline='' ทำให้ข้อมูลไม่มีบรรทัดว่าง
			fw = csv.writer(f) #สร้างฟังชั่นสำหรับเขียนข้อมูล
			data = [dt,s_list]
			fw.writerow(data)

		# ทำให้เคอเซอร์กลับไปตำแหน่งช่องกรอก E1
		E1.focus()
		update_table()

	except:
		print('ERROR')
		messagebox.showwarning('Error','Please Enter Again')
		v_list.set('')
	
# ทำให้สามารถกด enter ได้
GUI.bind('<Return>',Save) #ต้องเพิ่มใน def Save(event=None) ด้วย

FONT1 = ('Times',16) # None เปลี่ยนเป็น 'Angsana New'

#------text1--------
L = ttk.Label(F1,text='To Do List',font=FONT1)
L.pack()
v_list = StringVar()
# StringVar() คือ ตัวแปรพิเศษสำหรับเก็บข้อมูลใน GUI
E1 = ttk.Entry(F1,textvariable=v_list,font=FONT1)
E1.pack()
#-------------------

B2 = ttk.Button(F1,text=f'{"Save":>{5}}',command=Save,compound='left')
B2.pack(ipadx=15,ipady=8,pady=5)


####################TAB2#######################

rs = []

def read_csv():
	with open('savedata.csv',newline='',encoding='utf-8') as f:
		fr = csv.reader(f)
		data = list(fr)
	return data
	

header = ['วัน-เวลา','To Do List']
resulttable = ttk.Treeview(F1,columns=header,show='headings',height=15)
resulttable.pack()

for i in range(len(header)):
	resulttable.heading(header[i],text=header[i])

for h in header:
	resulttable.heading(h,text=h)

headerwidth = [225,225]
for h,w in zip(header,headerwidth):
	resulttable.column(h,width=w)



def update_table():
	resulttable.delete(*resulttable.get_children())
	data = read_csv()
	for d in data:
		resulttable.insert('',0,value=d)


#update_record()
update_table()
print('GET CHILD:',resulttable.get_children())
GUI.bind('<Tab>',lambda x: E2.focus())
GUI.mainloop()
