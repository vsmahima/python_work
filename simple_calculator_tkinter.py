#create a simple calculator using tkinter
import tkinter as tk

root=tk.Tk()
root.title("Calculator")
root.geometry("250x250")
root.resizable(False,False)

def click():
   
    pass
e1=tk.Entry(root,width=30,font=("Arial",20),bg="#353333",fg="#f1efef",justify="right")
e1.pack(padx=2,pady=2)
e1.insert(0,"0")

frame=tk.Frame(root,width=30)
frame.pack(fill="both",expand="True",padx=2)
for i in range(4):
    frame.columnconfigure(i,weight=1,uniform="button")
for i in range(5):
    frame.rowconfigure(i,weight=1,uniform="button")

bt1=tk.Button(frame,text="AC",fg="#eeeaea",bg="#333333",font=("Arial",12))
bt1.grid(row=0,column=0,sticky="nsew")
bt2=tk.Button(frame,text="+/-",fg="#eeeaea",bg="#333333",font=("Arial",12))
bt2.grid(row=0,column=1,sticky="nsew")
bt3=tk.Button(frame,text="%",fg="#eeeaea",bg="#333333",font=("Arial",12))
bt3.grid(row=0,column=2,sticky="nsew")
bt4=tk.Button(frame,text="\u00f7",fg="#eeeaea",bg="#f1a33c",font=("Arial",12))
bt4.grid(row=0,column=3,sticky="nsew")

bt5=tk.Button(frame,text="7",fg="#eeeaea",bg="#a5a5a5",font=("Arial",12))
bt5.grid(row=1,column=0,sticky="nsew")
bt6=tk.Button(frame,text="8",fg="#eeeaea",bg="#a5a5a5",font=("Arial",12))
bt6.grid(row=1,column=1,sticky="nsew")
bt7=tk.Button(frame,text="9",fg="#eeeaea",bg="#a5a5a5",font=("Arial",12))
bt7.grid(row=1,column=2,sticky="nsew")
bt8=tk.Button(frame,text="\u00d7",fg="#eeeaea",bg="#f1a33c",font=("Arial",12))
bt8.grid(row=1,column=3,sticky="nsew")

bt9=tk.Button(frame,text="4",fg="#eeeaea",bg="#a5a5a5",font=("Arial",12))
bt9.grid(row=2,column=0,sticky="nsew")
bt10=tk.Button(frame,text="5",fg="#eeeaea",bg="#a5a5a5",font=("Arial",12))
bt10.grid(row=2,column=1,sticky="nsew")
bt11=tk.Button(frame,text="6",fg="#eeeaea",bg="#a5a5a5",font=("Arial",12))
bt11.grid(row=2,column=2,sticky="nsew")
bt12=tk.Button(frame,text="-",fg="#eeeaea",bg="#f1a33c",font=("Arial",12))
bt12.grid(row=2,column=3,sticky="nsew")

bt13=tk.Button(frame,text="1",fg="#eeeaea",bg="#a5a5a5",font=("Arial",12))
bt13.grid(row=3,column=0,sticky="nsew")
bt14=tk.Button(frame,text="2",fg="#eeeaea",bg="#a5a5a5",font=("Arial",12))
bt14.grid(row=3,column=1,sticky="nsew")
bt15=tk.Button(frame,text="3",fg="#eeeaea",bg="#a5a5a5",font=("Arial",12))
bt15.grid(row=3,column=2,sticky="nsew")
bt16=tk.Button(frame,text="+",fg="#eeeaea",bg="#f1a33c",font=("Arial",12))
bt16.grid(row=3,column=3,sticky="nsew")

bt17=tk.Button(frame,text="0",fg="#eeeaea",bg="#a5a5a5",font=("Arial",12))
bt17.grid(row=4,column=0,sticky="nsew",columnspan=2)
bt18=tk.Button(frame,text=".",fg="#eeeaea",bg="#a5a5a5",font=("Arial",12))
bt18.grid(row=4,column=2,sticky="nsew")
bt19=tk.Button(frame,text="=",fg="#eeeaea",bg="#f1a33c",font=("Arial",12))
bt19.grid(row=4,column=3,sticky="nsew")

root.mainloop()