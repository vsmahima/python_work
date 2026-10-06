import tkinter as tk

root=tk.Tk()
root.title("Calculator")
root.geometry("250x250")
root.resizable(False,False)

frame=tk.Frame(root,width=30)
frame.pack(fill="both",expand="True",padx=2)

for i in range(4):
    frame.columnconfigure(i,weight=1,uniform="button")
for i in range(6):
    frame.rowconfigure(i,weight=1,uniform="button")

####ADDING WIDGET
e1=tk.Entry(frame,
            width=30,
            font=("Arial",20),
            bg="#353333",
            fg="#f1efef",
            justify="right")
e1.grid(row=0,column=0,columnspan=4)
e1.insert(0,"0")

button_values=[ ("AC","+/-","%","\u00f7"),
                ("7","8","9","\u00f7"),
                ("4","5","6","-"),
                ("1","2","3","+"),
                ("0",".","=")
]
j=1
for btn in button_values:
    i=0
    for txt in btn:
        if (txt=="0"):
            bt=tk.Button(frame,
                    text=txt
                    )
            bt.grid(row=j,column=i,sticky="nsew")
            i+=2 

        else:    
            bt=tk.Button(frame,
                 text=txt
                 )
            bt.grid(row=j,column=i,sticky="nsew")
            i+=1
    j+=1
root.mainloop()
