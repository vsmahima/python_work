import tkinter as tk
from tkinter import ttk
import sqlite3
import csv
from tkinter import messagebox

root=tk.Tk()
root.title("Admin Login")
root.geometry("400x300")

def admin_dashboard():
    root.withdraw()
    ad_dashboard=tk.Tk()
    ad_dashboard.title("Admin Dashboard")
    #ad_dashboard.geometry("400x600")
    ad_dashboard.resizable(False,False)
    ad_frame=tk.Frame(ad_dashboard,
            border="3",
            bg="#DCE0E0"        
              )
    ad_frame.pack()
    head_label=tk.Label(ad_frame,
                text="Name Age Gender Course",
                font=("Arial",12),
                fg="#3414e4",
                bg="#DCE0E0")
    head_label.pack()
    try:
        conn=sqlite3.connect("scope.db")
        cu=conn.cursor()
        cu.execute(""" SELECT * FROM student_profile """)
        fe=cu.fetchall()
        # print(len(fe))
        length=len(fe)
        # for line in range(1,(len+1)):

        for row in fe:
                label=tk.Label(ad_frame,
                               text=row,
                               font=("Arial",10),
                               fg="#0f0f0f",
                               bg="#DCE0E0")
                label.pack()
        
        dwn_frame=tk.Frame(ad_dashboard,
                        border="3",
                        bg="#DCE0E0" )
        dwn_frame.pack(pady=250,padx=100)
        for i in range(4):
            frame.columnconfigure(i,weight=1,uniform="Button")

        frame.rowconfigure(0,weight=1,uniform="Button")

        bt_download=tk.Button(dwn_frame,
                              text="Download",
                              command=download_file)
        bt_download.grid(row=0,column=0)
        bt_close=tk.Button(dwn_frame,
                           text="close",
                           command=lambda:fn_exit(ad_dashboard))
        bt_close.grid(row=0,column=1)

    except Exception as ex:
        print(f"Error Message: {ex}")
    ad_dashboard.mainloop()

def fn_exit(ad_dashboard):
    ad_dashboard.withdraw()
    root.deiconify()
    root.lift()
    root.focus_force()
    entry_login.delete(0,"end")
    entry_pswd.delete(0,"end")
    

def download_file():
    conn=sqlite3.connect("scope.db")
    cu=conn.cursor()
    cu.execute(""" SELECT * FROM student_profile """)
    fe=cu.fetchall()
    values=("Name","Age","Gender","Course")
    with open("download_file.csv","w") as file:
        f=csv.writer(file)
        f.writerow(values)
        for row in fe:
            f.writerow(row)
    path="download_file.csv"
    messagebox.showinfo("Information",f"file successfully saved to {path}")
    
    print(f"file successfully saved to {path}")
    
def user_registration():
    root.withdraw()
    reg_form=tk.Tk()
    reg_form.geometry("400x400")
    reg_form.title("User Registration")
    reg_form.resizable(False,False)
    reg_frame=tk.Frame(
        reg_form,
        border="3",
        bg="#DCE0E0"
        )
    reg_frame.pack(padx=50,pady=50,expand="True",fill="both")
    
    for i in range(3):
        reg_frame.columnconfigure(i,weight=1,uniform="Label,Button,Entry,Combobox")
    for i in range(5):
        reg_frame.rowconfigure(i,weight=1,uniform="Label,Button,Entry,Combobox")

    label_name=tk.Label(reg_frame,
                text="Name:",
                font=("Arial",10),
                fg="#0f0f0f",
                bg="#DCE0E0"

                 )
    label_name.grid(row=0,column=0,pady=5)
    
    entry_name=tk.Entry(reg_frame,width=20)
    entry_name.grid(row=0,column=1,pady=5)

    label_age=tk.Label(reg_frame,
                    text="Age:",
                    font=("Arial",10),
                    fg="#0f0f0f",
                    bg="#DCE0E0"
    
                     )
    label_age.grid(row=1,column=0,pady=5)

    entry_age=tk.Entry(reg_frame,width=20)
    entry_age.grid(row=1,column=1,pady=5)
    
    label_gender=tk.Label(reg_frame,
                    text="Gender:",
                    font=("Arial",10),
                    fg="#0f0f0f",
                    bg="#DCE0E0"
    
                     )
    label_gender.grid(row=2,column=0,pady=5)

    combo_gender=ttk.Combobox(reg_frame,width=20,
                              values=["Male","Female","Trans Gender"])
    combo_gender.grid(row=2,column=1)

    label_course=tk.Label(reg_frame,
                        text="Course:",
                        font=("Arial",10),
                        fg="#0f0f0f",
                        bg="#DCE0E0"
        
                         )
    label_course.grid(row=3,column=0,pady=5)

    combo_course=ttk.Combobox(reg_frame,width=20,
                                  values=["Python","Java","AI","DB"])
    combo_course.grid(row=3,column=1)
    
    bt_save=tk.Button(reg_frame,
                      text="Save",
                      command= lambda:save_details(entry_name,entry_age,combo_gender,combo_course,reg_frame,reg_form))
    bt_save.grid(row=5,column=2,columnspan=2,pady=5)
    
    reg_form.mainloop()


def validation(name,age,gender,course,reg_frame):
    if(name==""):
        label_name_er=tk.Label(reg_frame,
                            text="Required field",
                            font=("Arial",10),
                            fg="#ee0a0a",
                            bg="#DCE0E0")
        label_name_er.grid(row=0,column=3)
    if(age==""):
        label_age_er=tk.Label(reg_frame,
                                    text="Required field",
                                    font=("Arial",10),
                                    fg="#ee0a0a",
                                    bg="#DCE0E0")
        label_age_er.grid(row=1,column=3)
    # if(age.isdigit()==False):
    #     label_age_er=tk.Label(reg_frame,
    #                                 text="Age should be a Number",
    #                                 font=("Arial",10),
    #                                 fg="#ee0a0a",
    #                                 bg="#DCE0E0")
    #     label_age_er.grid(row=0,column=3)
    if(gender==""):
        label_gender_er=tk.Label(reg_frame,
                                    text="Required field",
                                    font=("Arial",10),
                                    fg="#ee0a0a",
                                    bg="#DCE0E0")
        label_gender_er.grid(row=2,column=3)
    if(course==""):
        label_course_er=tk.Label(reg_frame,
                                    text="Required field",
                                    font=("Arial",10),
                                    fg="#ee0a0a",
                                    bg="#DCE0E0")
        label_course_er.grid(row=3,column=3)
  
def save_details(entry_name,entry_age,combo_gender,combo_course,reg_frame,reg_form):
    name=entry_name.get()
    age=int(entry_age.get())
    gender=combo_gender.get()
    course=combo_course.get()
    validation(name,age,gender,course,reg_frame)
    try:
        conn=sqlite3.connect("scope.db")
        cu=conn.cursor()
        cu.execute("""CREATE TABLE IF NOT EXISTS student_profile(sname VARCHAR(50),
                                    age INT,
                                    gender VARCHAR(30),
                                    course VARCHAR(30))
                    """)
        print(name,age,gender,course)
        cu.execute("""INSERT INTO student_profile (sname,age,gender,course) VALUES (?,?,?,?)
                """,(name,age,gender,course))

        conn.commit()
        child_reg_form=tk.Tk()
        child_reg_form.title("Message")
        child_reg_form.geometry("400x100")
        child_reg_form.resizable(False,False)
        label_reg_msg=tk.Label(child_reg_form,
                                            text="Registration completed successfully...",
                                            font=("Arial",10),
                                            fg="#190aee",
                                            bg="#DCE0E0")
        label_reg_msg.pack(padx=10,pady=10)
        bt_Ok=tk.Button(child_reg_form,command=lambda:fn_ok(reg_form,child_reg_form),
                        text="OK")
        bt_Ok.pack(padx=10,pady=20)
    except Exception as ex:
        print(f"Error Message: {ex}")
    conn.close()

def fn_ok(reg_form,child_reg_form):
    reg_form.withdraw()
    child_reg_form.withdraw()
    root.deiconify()
    root.lift()
    root.focus_force()


def admin_login():
    logid=entry_login.get()
    pswd=entry_pswd.get()
    if(logid=="admin" and pswd=="admin123"):
       admin_dashboard()
    else:
        label_msg=tk.Label(
            frame,
            text="Incorrect username/password",
            width=550,
            fg="#ee0a0a",
            font=("Arial",10),
            bg="#DCE0E0")
        label_msg.grid(row=3,column=0,columnspan=4)
########MAIN WINDOW
frame=tk.Frame(root,bg="#DCE0E0")
frame.pack(padx=50,pady=50,expand="True",fill="both")
for i in range(4):
    frame.columnconfigure(i,weight=1,uniform="Label,Button")
for i in range(4):
    frame.rowconfigure(i,weight=1,uniform="Label,Button")

label_user=tk.Label(frame,
                    text="User Id:",
                    font=("Arial",10),
                    fg="#0f0f0f",
                    bg="#DCE0E0"
                    )
label_user.grid(row=0,column=0,padx=5,pady=5)

entry_login=tk.Entry(frame,width=30)
entry_login.grid(row=0,column=1,pady=5)

label_pswd=tk.Label(frame,
                    text="Password:",
                    font=("Arial",10),
                    fg="#0f0f0f",
                    bg="#DCE0E0"
                    )
label_pswd.grid(row=1,column=0,padx=5,pady=5)

entry_pswd=tk.Entry(frame,show="*",width=30)
entry_pswd.grid(row=1,column=1,pady=5)

bt_login=tk.Button(frame,text="Login",width=20,command=admin_login)
bt_login.grid(row=2,column=1,pady=5)

bt_reg=tk.Button(frame,text="User Registration",command=user_registration)
bt_reg.grid(row=4,column=2,columnspan=2,pady=5)
root.mainloop()