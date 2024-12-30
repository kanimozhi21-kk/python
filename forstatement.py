from tkinter import *
from tkinter import messagebox
from tkinter import font
from tkinter import filedialog
from PIL import ImageTk,Image
from tkinter import ttk
from tkcalendar import DateEntry
import sqlite3
import webbrowser

conn=sqlite3.connect("students mgt.db")
conn_ma=sqlite3.connect("books.db")
cursor=conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS students(id INTEGER PRIMARY KEY
                AUTOINCREMENT,name TEXT,dob TEXT,age TEXT,gender TEXT,contact TEXT,email TEXT,
                address TEXT,degree TEXT,course TEXT,joning TEXT,fees TEXT)""")
conn.commit()
try:
    cursor.execute("ALTER TABLE students ADD COLUMN fees INTEGER DEFAULT 0")
    conn.commit()
except sqlite3.OperationalError:
    pass
cursor_ma=conn_ma.cursor()
cursor_ma.execute("""CREATE TABLE IF NOT EXISTS materials(id INTEGER PRIMARY KEY AUTOINCREMENT,
                    subject TEXT,material TEXT)""")
conn.commit()
conn_ma.commit()

############books
def add_material():
    subject=mater_entry.get()
    path=material_entry.get()
    if subject and path:
        cursor_ma.execute("INSERT INTO materials(subject,material)VALUES(?,?)",(subject,path))
        conn_ma.commit()
        messagebox.showinfo("DONE","SUCCESSFULLY FILE ADDED")
        clear_field()
    else:
        messagebox.showerror("FAILED","ADD FILE")

def browser_file():
    file_path=filedialog.askopenfilename(filetypes=[("PDF Files","*.pdf"),("All Files","*.*")])
    material_entry.delete(0, END)
    material_entry.insert(0,file_path)

def open_material(tree):
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror("FAILED","SOMETHING WRONG")
        return
    material=tree.item(selected_item)["values"]
    file_path=material[2]
    try:
        webbrowser.open(file_path)
    except Exception as e:
        messagebox.showerror("FAILED","SOMETHING WRONG")

def show_all_materials():
    cursor_ma.execute("SELECT * FROM materials")
    materials=cursor_ma.fetchall()
    if not materials:
        messagebox.showinfo("DONE","MATERIAL UPDATE SUCCESSFULLY")
        return
    material_win=Toplevel(app)
    material_win.title("ALL MATERIALS")
    material_win.geometry("600x400")

    font_but22=font.Font(weight="bold",family="Trebuchet MS",size=20)
    Label(material_win,text="Registered",font=font_but22).pack(pady=10)

    tree=ttk.Treeview(material_win,columns=("Number","Subject","Material"),show="headings")
    tree.heading("Number",text="Number")
    tree.heading("Subject",text="Subject")
    tree.heading("Material",text="Material")

    for mat in materials:
        tree.insert("","end",values=mat)
    tree.pack(fill="both",expand=True,pady=10)

    Button(material_win,text="DELETE",command=lambda:delet(tree)).place(relx=0.05,rely=0.05)
    Button(material_win,text="OPEN",command=lambda:open_material(tree)).place(relx=0.10,rely=0.05)
    Button(material_win,text="BACK",command=material_win.destroy).place(relx=0.15,rely=0.05)

def delet(tree):
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror("ERROR","SELECT ID NUMBER")
        return
    mat=tree.item(selected_item)["values"]
    cursor_st.execute("DELETE * FROM materials WHERE number=?",(mat[0],))
    conn_ma.commit()
    tree.delete(selected_item)

def clear_field():
    mater_entry.delete(0,END)
    material_entry.delete(0,END)
##########START
def login():
    username=usernam_entry.get()
    password=passwo_entry.get()
    if username =="admin" and password =="admin":
        usernam_entry.delete(0,END)
        passwo_entry.delete(0,END)
        show_registration_page()
    else:
        messagebox.showerror("FAILED","USERNAME AND PASSWORD INCORRET")

#####STUDENT REGISTER
def show_registration_page():
    login_frame.pack_forget()
    registration_frame.pack(fill="both",expand=True)
def register_student():
    name=entry_name.get()
    dob=entry_dob.get()
    age=entry_ag.get()
    gender=entry_cc.get()
    contact=entry_non.get()
    email=entry_no.get()
    address=entry_addre.get()
    degree=entry_deg.get()
    course=entry_co.get()
    joning=entry_rn.get()

    if name and dob and age and gender and contact and email and address and degree and course and joning:
        cursor.execute("""INSERT INTO students(name,dob,age,gender,contact,email,address,degree,
                             course,joning,fees)VALUES(?,?,?,?,?,?,?,?,?,?,0)""",(
                                 name,dob,age,gender,contact,email,address,degree,course,joning))
        conn.commit()
        messagebox.showinfo("DONE","SUCCESSFULLY REGISTER")
        reset_fields()
    else:
         messagebox.showerror("FAILED","SOMETHING WRONG")

#####STORE THE VALUE IN DATABASE         
def records():
    cursor.execute("SELECT * FROM students")
    students=cursor.fetchall()
    if not students:
        messagebox.showinfo("DONE","STUDENT RECORDS REGISTER SUCCESSFULLY")
        return
    student_win=Toplevel()
    student_win.title("all")
    student_win.geometry("500x500")

    font_but22=font.Font(weight="bold",family="Trebuchet MS",size=20)
    Label(student_win,text="STUDENT RECORDS",font=font_but22).pack(pady=10)

    myframe=Frame(student_win)
    myframe.pack(fill="both",expand=True)

    font_but23=font.Font(family="Trebuchet MS",size=12)
    Label(student_win,text="FEES:",font=font_but23).place(relx=0.43,rely=0.06)
    fees_entry=Entry(student_win)
    fees_entry.place(relx=0.48,rely=0.07)

    tree=ttk.Treeview(student_win,columns=("ID","NAME","DOB","AGE","GENDER","CONTACT","EMAIL_ID","ADDRESS","DEGREE","COURSE","JONING DATE","FEES"),show="headings",height=30)
    tree.heading("ID",text="ID")
    tree.heading("NAME",text="NAME")
    tree.heading("DOB",text="DOB")
    tree.heading("AGE",text="AGE")
    tree.heading("GENDER",text="GENDER")
    tree.heading("CONTACT",text="CONTACT")
    tree.heading("EMAIL_ID",text="EMAIL_ID")
    tree.heading("ADDRESS",text="ADDRESS")
    tree.heading("DEGREE",text="DEGREE")
    tree.heading("COURSE",text="COURSE")
    tree.heading("JONING DATE",text="JONING DATE")
    tree.heading("FEES",text="FEES")


    tree.column("ID",width=50)
    tree.column("NAME",width=50)
    tree.column("DOB",width=50)
    tree.column("AGE",width=50)
    tree.column("GENDER",width=50)
    tree.column("CONTACT",width=50)
    tree.column("EMAIL_ID",width=50)
    tree.column("ADDRESS",width=50)
    tree.column("DEGREE",width=50)
    tree.column("COURSE",width=50)
    tree.column("JONING DATE",width=50)
    tree.column("FEES",width=50)
    for students in students:
        tree.insert("","end",values=students)
    tree.pack(fill="both",expand=True)

    Button(student_win,text="UPDATE",command=lambda:update(tree,student_win)).place(relx=0.05,rely=0.10)
    Button(student_win,text="DELETE",command=lambda:delet(tree)).place(relx=0.10,rely=0.10)
    Button(student_win,text="BACK",command=student_win.destroy).place(relx=0.15,rely=0.10)
    Button(student_win,text="FEES UPDATE",command=lambda:update_fees(tree,fees_entry)).place(relx=0.48,rely=0.11)
#######UPDATE FEES
def update_fees(tree,fees_entry):
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror("FAILED","FEES UPDATE WRONG")
        return
    student=tree.item(selected_item)["values"]
    new_fees=fees_entry.get()
    if not new_fees.isdigit():
        messagebox.showerror("FAILED","FEES UPDATE WRONG")
        return
    try:
        cursor.execute("UPDATE students SET fees=? WHERE id=?",(int(new_fees),student[0]))
        conn.commit()
        updated_student=list(student)
        updated_student[4]=int(new_fees)
        tree.item(selected_item,values=updated_student)
        messagebox.showinfo("DONE","FEES UPDATE SUCCESSFULLY")
    except sqlite3.Error as e:
            messagebox.showerror("FAILED","FEES UPDATE WRONG")
#######UPDATE STUDENT
def update(tree,win):
    selected_item=tree.selection()
    if not selected_item:
        messagebox.showerror("ERROR","SOMETHING ERROR")
        return
    student=tree.item(selected_item)["values"]
    win.destroy()
    entry_name.insert(0,student[1])
    entry_dob.insert(0,student[2])
    entry_ag.insert(0,student[3])
    entry_cc.insert(0,student[4])
    entry_non.insert(0,student[5])
    entry_no.insert(0,student[6])
    entry_addre.insert(0,student[7])
    entry_deg.insert(0,student[8])
    entry_co.insert(0,student[9])
    entry_rn.insert(0,student[10])
    
    register_button.config(text="UPDATE",command=lambda:exect_updat(student[0]))
######EXECUTE UPDATE CONCEPT
def exect_updat(student_id):
    name=entry_name.get()
    dob=entry_dob.get()
    age=entry_ag.get()
    gender=entry_cc.get()
    contact=entry_non.get()
    email=entry_no.get()
    address=entry_addre.get()
    degree=entry_deg.get()
    course=entry_co.get()
    joning=entry_rn.get()

    if name and dob and age and gender and contact and email and address and degree and course and joning:
        cursor.execute("""UPDATE students SET name=?,dob=?,age=?,gender=?,contact=?,
                          email=?,address=?,degree=?,course=?,joning=? WHERE id=?""",
                            (name,dob,age,gender,contact,email,address,degree,course,joning,student_id))
        conn.commit()
        messagebox.showinfo("DONE","UPDATE STUDENT DETAILS SUCCESSFULLY")
        reset_fields()
        register_button.config(text="register",command=register_student)
    else:
         messagebox.showerror("FAILED","UPDATE FAILED")

######DELETE IN STUDENT DETAILS
def delet(tree):
    selected_item=tree.selection()
    if not selected_item:
         messagebox.showerror("ERROR","SELECT ID NUMBER")
         return
    student=tree.item(selected_item)["values"]
    cursor.execute("DELETE FROM students WHERE id=?",(student[0],))
    conn.commit()
    tree.delete(selected_item)

#####AUTOMETIC ERASED STUDENT DETAILS
def reset_fields():
    entry_name.delete(0,END)
    entry_dob.delete(0,END)
    entry_ag.delete(0,END)
    entry_cc.delete(0,END)
    entry_non.delete(0,END)
    entry_no.delete(0,END)
    entry_addre.delete(0,END)
    entry_deg.delete(0,END)
    entry_co.delete(0,END)
    entry_rn.delete(0,END)
######STUDENT LOGIN PAGE
def main1():
    registration_frame.pack_forget()
    student_page.pack(fill="both",expand=True)
def last_page():
    userna=usernamee_entry.get()
    passwo=passwordd_entry.get()
    datee=entry_rn.get()
    with open("student.txt","w")as file:
        file.write(f"NAME:{userna}\n")
        file.write(f"COURSE:{passwo}\n")
        file.write(f"DATE:{datee}\n")
        file.write(f"_______________________________________________\n")
    if userna and passwo:
        messagebox.showinfo("LOGIN","LOGIN SUCCESSFULLY")
    else:
        messagebox.showerror("FAILED","LOGIN FAILED")

#######MAIN 
def main():
    registration_frame.pack_forget()
    student_page.pack(fill="both",expand=True)
def exit_app():
    registration_frame.pack_forget()
    login_frame.pack(fill="both",expand=True)
def exit_a():
    student_page.pack_forget()
    registration_frame.pack(fill="both",expand=True)

app=Tk()
app.title("STUDENT MANAGEMENT SYSTEM")
app.geometry("800x400")

#####ADMIN LOGIN
login_frame=Frame(app)
login_frame.pack(fill="both",expand=True)

# imga=Image.open("compp5.jpg")
# imga=imga.resize((1500,350))
# phot=ImageTk.PhotoImage(imga)
# Label(login_frame,image=phot).pack()

font_but2=font.Font(weight="bold",family="Trebuchet MS",size=15)
x=Label(text="K2 Computer Institute",font=font_but2)
x.config(bg="dark goldenrod",fg="black")
x.place(relx=0.42,rely=0.48)

font_but22=font.Font(weight="bold",family="Trebuchet MS",size=20)
Label(login_frame,text="ADMIN LOGIN",font=font_but22).place(relx=0.43,rely=0.56)

font_11=font.Font(weight="bold",family="Trebuchet MS",size=15)
Label(login_frame,text="USER ID:",fg="black",font=font_11).place(relx=0.36,rely=0.67)
usernam_entry=Entry(login_frame,width=20,font='arial 15')
usernam_entry.place(relx=0.46,rely=0.67)
    
font_12=font.Font(weight="bold",family="Trebuchet MS",size=15)
Label(login_frame,text="PASSWORD:",fg="black",font=font_12).place(relx=0.36,rely=0.75)
passwo_entry=Entry(login_frame,show="*",width=20,font='arial 15')
passwo_entry.place(relx=0.46,rely=0.75)

font_but=font.Font(weight="bold",family="Trebuchet MS",size=10)       
login_button=Button(login_frame,text="LOGIN",bg='black',fg="white",activebackground="rosybrown2",command=login,font=font_but)
login_button.place(relx=0.5,rely=0.83)
showw=Button(login_frame,text="SHOW ALL REGISTRATION",command=records,font=font_but)
showw.place(relx=0.36,rely=0.90)
mate=Button(login_frame,text="SHOW ALL MATERIAL",command=lambda:[login_frame.pack_forget(),material_frame.pack(fill="both",expand=True)],font=font_but)
mate.place(relx=0.55,rely=0.90)

frame=Frame(login_frame,width=1500,height=40,bg='dark goldenrod').place(relx=.00,rely=.48)
frame=Frame(login_frame,width=20,height=1500,bg='black').place(relx=.0,rely=.0)
frame=Frame(login_frame,width=20,height=1500,bg='black').place(relx=.99,rely=.0)
frame=Frame(login_frame,width=1500,height=20,bg='black').place(relx=.00,rely=.0)
frame=Frame(login_frame,width=1500,height=30,bg='black').place(relx=.99,rely=.0)
###STUDENT REGISTRATION
registration_frame=Frame(app)

# img=Image.open("compp5.jpg")
# img=img.resize((1500,350))
# photo=ImageTk.PhotoImage(img)
# Label(registration_frame,image=photo).place(relx=0.00,rely=0.00)

font_but2=font.Font(weight="bold",family="Trebuchet MS",size=18)
x=Label(text="K2 Computer Institute",font=font_but2)
x.config(bg="dark goldenrod",fg="black")
x.place(relx=0.42,rely=0.48)

font_but22=font.Font(weight="bold",family="Trebuchet MS",size=20)
Label(registration_frame,text="STUDENT REGISTRATION",font=font_but22).place(relx=0.36,rely=0.54)

frame=Frame(registration_frame,width=1500,height=40,bg='dark goldenrod').place(relx=.00,rely=.48)
frame=Frame(registration_frame,width=20,height=1500,bg='black').place(relx=.0,rely=.0)
frame=Frame(registration_frame,width=20,height=1500,bg='black').place(relx=.99,rely=.0)
frame=Frame(registration_frame,width=1500,height=20,bg='black').place(relx=.00,rely=.0)
frame=Frame(registration_frame,width=1500,height=30,bg='black').place(relx=.99,rely=0.00)

font_11=font.Font(weight="bold",family="Trebuchet MS",size=15)
Label(registration_frame,text="NAME:",fg="black",font=font_11).place(relx=0.20,rely=0.60)
entry_name=Entry(registration_frame,width=20,font='arial 10')
entry_name.place(relx=0.28,rely=0.60)

font_12=font.Font(weight="bold",family="Trebuchet MS",size=15)
Label(registration_frame,text="DOB:",fg="black",font=font_12).place(relx=0.20,rely=0.65)
entry_dob=Entry(registration_frame,width=20,font='arial 10')
entry_dob.place(relx=0.28,rely=0.65)

Label(registration_frame,text="AGE:",fg="black",font=font_11).place(relx=0.20,rely=0.70)
entry_ag=Entry(registration_frame,width=20,font='arial 10')
entry_ag.place(relx=0.28,rely=0.70)

font_13=font.Font(weight="bold",family="Trebuchet MS",size=15)
Label(registration_frame,text='GENDER',fg="black",font=font_13).place(relx=0.20,rely=0.75)
entry_cc=ttk.Combobox(registration_frame,values=['MALE','FEMALE'])
entry_cc.place(relx=0.28,rely=0.75)

font_14=font.Font(weight="bold",family="Trebuchet MS",size=15)
Label(registration_frame,text="CONTACT:",fg="black",font=font_14).place(relx=0.20,rely=0.80)
entry_non=Entry(registration_frame,width=20,font='arial 10')
entry_non.place(relx=0.28,rely=0.80)

font_e=font.Font(weight="bold",family="Trebuchet MS",size=15)
c=Label(registration_frame,text="EMAIL ID:",fg="black",font=font_e)
c.place(relx=0.55,rely=0.80)
entry_no=Entry(registration_frame,width=20,font='arial 10')
entry_no.place(relx=0.66,rely=0.80)

font_13=font.Font(weight="bold",family="Trebuchet MS",size=15)
Label(registration_frame,text="ADDRESS:",fg="black",font=font_13).place(relx=0.55,rely=0.65)
entry_addre=Entry(registration_frame,width=20,font='arial 10')
entry_addre.place(relx=0.66,rely=0.65)

Label(registration_frame,text="DEGREE:",fg="black",font=font_13).place(relx=0.55,rely=0.70)
entry_deg=Entry(registration_frame,width=20,font='arial 10')
entry_deg.place(relx=0.66,rely=0.70)

Label(registration_frame,text="COURSE:",fg="black",font=font_13).place(relx=0.55,rely=0.75)
entry_co=Entry(registration_frame,width=20,font='arial 10')
entry_co.place(relx=0.66,rely=0.75)

Label(registration_frame,text="JOINING DATE:",fg="black",font=font_13).place(relx=0.55,rely=0.60)
entry_rn=DateEntry(registration_frame,date_pattern='y-mm-dd',width=20,font='arial 10')
entry_rn.place(relx=0.66,rely=0.60)


font_but2=font.Font(weight="bold",family="Trebuchet MS",size=10)
register_button=Button(registration_frame,text="REGISTER",bg="black",fg="white",command=register_student,activebackground="rosybrown2",font=font_but2)
register_button.place(relx=0.45,rely=0.87)
Button(registration_frame,text="EXIT",command=exit_app,font=font_but2).place(relx=0.43,rely=0.94)
Button(registration_frame,text="GO TO THE STUDENT LOGIN",command=main1,font=font_but2).place(relx=0.50,rely=0.94)


###STUDENT LOGIN
student_page=Frame(app)

# imgekl=Image.open("compp5.jpg")
# imgekl=imgekl.resize((1500,350))
# photool=ImageTk.PhotoImage(imgekl)
# Label(material_frame,image=photool).place(relx=0.00,rely=0.00)

font_but2=font.Font(weight="bold",family="Trebuchet MS",size=18)
x=Label(text="K2 Computer Institute",font=font_but2)
x.config(bg="dark goldenrod",fg="black")
x.place(relx=0.42,rely=0.48)

font_but22=font.Font(weight="bold",family="Trebuchet MS",size=20)
Label(student_page,text="STUDENT LOGIN",font=font_but22).place(relx=0.43,rely=0.56)

frame=Frame(student_page,width=1500,height=40,bg='dark goldenrod').place(relx=.00,rely=.48)
frame=Frame(student_page,width=20,height=1500,bg='black').place(relx=.0,rely=.0)
frame=Frame(student_page,width=20,height=1500,bg='black').place(relx=.99,rely=.0)
frame=Frame(student_page,width=1500,height=20,bg='black').place(relx=.00,rely=.0)
frame=Frame(student_page,width=1500,height=20,bg='black').place(relx=.98,rely=.0)

font_11=font.Font(weight="bold",family="Trebuchet MS",size=15)
Label(student_page,text="NAME:",fg="black",font=font_11).place(relx=0.39,rely=0.75)
usernamee_entry=Entry(student_page,width=20,font='arial 15')
usernamee_entry.place(relx=0.46,rely=0.75)
    
font_12=font.Font(weight="bold",family="Trebuchet MS",size=15)
Label(student_page,text="COURSE:",fg="black",font=font_12).place(relx=0.39,rely=0.83)
passwordd_entry=Entry(student_page,width=20,font='arial 15')
passwordd_entry.place(relx=0.46,rely=0.83)

Label(student_page,text="DATE:",fg="black",font=font_12).place(relx=0.39,rely=0.67)
entry_rn=DateEntry(student_page,date_pattern='y-mm-dd',width=20,font='arial 15')
entry_rn.place(relx=0.46,rely=0.67)

font_but=font.Font(weight="bold",family="Trebuchet MS",size=10)       
login_button=Button(student_page,text="LOGIN",bg='black',fg="white",activebackground="rosybrown2",command=main,font=font_but)
login_button.place(relx=0.50,rely=0.90)
Button(student_page,text="EXIT",command=exit_a,font=font_but).place(relx=0.43,rely=0.94)
Button(student_page,text="SHOW ALL MATERIALS",command=show_all_materials,font=font_but).place(relx=0.55,rely=0.94)
#######OPTIONAL
material_frame=Frame(app)

# imgekk=Image.open("compp5.jpg")
# imgekk=imgekk.resize((1500,350))
# photook=ImageTk.PhotoImage(imgekk)
# Label(syl_frame,image=photook).place(relx=0.00,rely=0.00)

font_but2=font.Font(weight="bold",family="Trebuchet MS",size=18)
x=Label(text="K2 Computer Institute",font=font_but2)
x.config(bg="dark goldenrod",fg="black")
x.place(relx=0.42,rely=0.48)

font_but22=font.Font(weight="bold",family="Trebuchet MS",size=20)
Label(material_frame,text="STUDENT LOGIN",font=font_but22).place(relx=0.35,rely=0.56)

font_11=font.Font(weight="bold",family="Trebuchet MS",size=15)
Label(material_frame,text="SUBJECT:",fg="black",font=font_11).place(relx=0.37,rely=0.67)
mater_entry=Entry(material_frame,width=20,font='arial 15')
mater_entry.place(relx=0.46,rely=0.67)
    
font_12=font.Font(weight="bold",family="Trebuchet MS",size=15)
Label(material_frame,text="MATERIAL:",fg="black",font=font_12).place(relx=0.37,rely=0.75)
material_entry=Entry(material_frame,width=20,font='arial 15')
material_entry.place(relx=0.46,rely=0.75)

font_but=font.Font(weight="bold",family="Trebuchet MS",size=10)
Button(material_frame,text="BROWSER",command=browser_file,font=font_but).place(relx=0.37,rely=0.86)
Button(material_frame,text="ADD MATERIAL",command=add_material,font=font_but).place(relx=0.45,rely=0.86)
Button(material_frame,text="SHOW ALL MATERIAL",command=show_all_materials,font=font_but).place(relx=0.55,rely=0.86)
Button(material_frame,text="BACK",command=lambda:[material_frame.pack_forget(),login_frame.pack(fill="both",expand=True)],font=font_but).place(relx=0.50,rely=0.93)

frame=Frame(material_frame,width=1500,height=40,bg='dark goldenrod').place(relx=.00,rely=.48)
frame=Frame(material_frame,width=20,height=1500,bg='black').place(relx=.0,rely=.0)
frame=Frame(material_frame,width=20,height=1500,bg='black').place(relx=.99,rely=.0)
frame=Frame(material_frame,width=1500,height=20,bg='black').place(relx=.00,rely=.0)
frame=Frame(material_frame,width=1500,height=20,bg='black').place(relx=.98,rely=.0)
#date_pattern='y-mm-dd',

app.mainloop()

