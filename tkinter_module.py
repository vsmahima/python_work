import tkinter as tk
root =tk.Tk()
#to change the title
root.title("My first App")
#to change the size of the window
root.geometry("500x600")
l1=tk.Label(root,text="Scope Class",font=("Arial",20),fg="blue",bg="#f0bbbb",padx=50,pady=50)

l1.pack()
root.mainloop()