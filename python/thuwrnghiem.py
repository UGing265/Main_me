"""
from tkinter import *
from tkinter import messagebox

ws = Tk()
ws.title('Python Guides')
ws.geometry('300x100')

def askMe():
    res = messagebox.askquestion('askquestion', 'Do you like cats?')
    if res == 'yes':
        messagebox.showinfo('Response', 'You like Cats')
    elif res == 'no':
        messagebox.showinfo('Response', 'You must be a dog fan.')
    else:
        messagebox.showwarning('error', 'Something went wrong!')


Button(ws, text='Click here', padx=10, pady=5, command=askMe).pack(pady=20)

ws.mainloop()
"""
"""
from tkinter import *
from tkinter import messagebox
import time

ws = Tk()
ws.title('Python Guides')
ws.geometry('400x200')
ws.config(bg='#345')

def quitWin():
    res = messagebox.askyesno('prompt', 'Do you want to kill this window?') 
    if res == True:
        messagebox.showinfo('countdown', 'killing window in 5 seconds')
        time.sleep(5)
        ws.quit()

    elif res == False:
        pass
    else:
        messagebox.showerror('error', 'something went wrong!')

Button(ws, text='Kill the Window', padx=10, pady=5, command=quitWin).pack(pady=50)

ws.mainloop()
"""
"""
from tkinter import *
from tkinter import messagebox

ws = Tk()
ws.title('PythonGuides')
ws.geometry('400x300')
ws.config(bg='#4a7a8c')

def askQuestion():
    reply = messagebox.askyesno('confirmation', 'Are you sure you want to donate $10000 ?')
    if reply == True:
        messagebox.showinfo('successful','You are the Best!')
    else:
        messagebox.showinfo('', 'Maybe next time!')
       

def askYesNo():
    reply = messagebox.askyesno('confirmation', 'Do you want to quit this application?')
    if reply == True:
        messagebox.showinfo('exiting..', 'exiting application')
        ws.destroy()
    else:
        messagebox.showinfo('', 'Thanks for Staying')
       

btn1 = Button(
    ws,
    text='Transfer',
    command=askQuestion,
    padx=15,
    pady=5
)
btn1.pack(expand=True, side=LEFT)

btn2 = Button(
    ws,
    text='Exit',
    command=askYesNo,
    padx=20,
    pady=5
)
btn2.pack(expand=True, side=RIGHT)

ws.mainloop()
"""
"""
from tkinter import *
from tkinter import simpledialog

ws = Tk()
ws.title("Python Guides")

answer1 = simpledialog.askstring("Input", "What is your first name?",
                                parent=ws)
if answer1 is not None:
    print("Your first name is ", answer1)
else:
    print("You don't have a first name?")

answer1 = simpledialog.askinteger("Input", "What is your age?",
                                 parent=ws,
                                 minvalue=0, maxvalue=100)
if answer1 is not None:
    print("Your age is ", answer1)
else:
    print("You don't have an age?")

answer1 = simpledialog.askfloat("Input", "What is your salary?",
                               parent=ws,
                               minvalue=0.0, maxvalue=100000.0)
if answer1 is not None:
    print("Your salary is ", answer1)
else:
    print("You don't have a salary?")
ws.mainloop()
""" # nhập tên tuổi tiền

"""
from tkinter import *
from tkinter import filedialog as fd 
ws = Tk()
ws.title("Python Guides")
ws.geometry("100x100")
def callback():
    name= fd.askopenfilename() 
    print(name)
    
error_msg = 'Error!'
Button(text='File Open', 
       command=callback).pack(fill=X)
ws.mainloop()
"""
"""
from tkinter import *


class customdialog(Toplevel):
    def __init__(self, parent, prompt):
        Toplevel.__init__(self, parent)

        self.var = StringVar()

        self.label = Label(self, text=prompt)
        self.entry = Entry(self, textvariable=self.var)
        self.ok_button = Button(self, text="OK", command=self.on_Ok)

        self.label.pack(side="top", fill="x")
        self.entry.pack(side="top", fill="x")
        self.ok_button.pack(side="right")

        self.entry.bind("<Return>", self.on_Ok)

    def on_Ok(self, event=None):
        self.destroy()

    def show(self):
        self.wm_deiconify()
        self.entry.focus_force()
        self.wait_window()
        return self.var.get()

class example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.button = Button(self, text="Get Input", command=self.on_Button)
        self.label = Label(self, text="", width=20)
        self.button.pack(padx=8, pady=8)
        self.label.pack(side="bottom", fill="both", expand=True)

    def on_Button(self):
        string = customdialog(self, "Enter something:").show()
        self.label.configure(text="You entered:\n" + string)


if __name__ == "__main__":
    ws = Tk()
    ws.title("Python Guides")
    ws.geometry("200x200")
    example(ws).pack(fill="both", expand=True)
    ws.mainloop()
"""

import tkinter as tk
from tkinter import ttk
# for python 2 imports:
# import Tkinter as tk
# import ttk

root = tk.Tk()
root.withdraw()

for i in range(0,5):
    x = tk.Toplevel(root)
    x.title("Error Box!")
    x.geometry("150x75+0+0")
    x.resizable(False, False)
    ttk.Label(x, text = "oops").pack()
    ttk.Button(x, text = " OK ", command = x.destroy).pack(side=tk.BOTTOM)

root.mainloop()