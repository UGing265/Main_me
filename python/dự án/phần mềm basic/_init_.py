import tkinter as tk
import customtkinter
from PIL import ImageTk, Image
import res as aa


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("green")

# def button_Dota():
#     app.destroy()
#     app1= customtkinter.CTk()
#     app1.geometry("1500x1000")
#     app1.title("Homepage")
#     text = customtkinter.CTkLabel(master=app1,text="WELCOME TO GAY")
#     text.place(x=100,y=100)
#     app1.mainloop()
def button5():
    test = entry1.get()
    test2 = entry2.get()#input field
    print("user:",test)
    print("pass:",test2)
    app.destroy()

#set up vị trí 
width=900
height=500
app = customtkinter.CTk()
app.geometry("700x500")
app.title("HELLO")
x= (app.winfo_screenwidth()//2)-(width//2)
y= (app.winfo_screenheight()//3)-(height//3)
app.geometry(f"{width}x{height}+{x}+{y}")
app.resizable(False,False)
#set ico 
#app.iconbitmap("./icon.ico")


bg= ImageTk.PhotoImage(Image.open("bg1.png")) #từ khóa parrten
l1=customtkinter.CTkLabel(master=app, image=bg)
l1.pack()

frame = customtkinter.CTkFrame(master=l1,width=320,height=360, corner_radius=20)#corner_radius  laf ber gocso vuoong
frame.place(relx=0.5,rely=0.5, anchor=tk.CENTER)

l2 = customtkinter.CTkLabel(master=frame, text="log into your account",font=("Century Gothic", 20))
l2.place(x=40,y=50)

entry1= customtkinter.CTkEntry(master=frame, width=220, placeholder_text="Username")
entry1.place(x=50, y= 100)

entry2= customtkinter.CTkEntry(master=frame, width=220, placeholder_text="Password")
entry2.place(x=50, y= 150)

l3 = customtkinter.CTkLabel(master=frame, text="Forgot passwork ?", font=("Century Gothic",15))
l3.place(x=150,y=180)

button1= customtkinter.CTkButton(master=frame,width=220, text="Login", corner_radius=20,command=button5)
button1.place(x=45,y= 240)

button2= customtkinter.CTkButton(master=frame,width=220, text="Resgiter", corner_radius=20)
button2.place(x=45,y= 280)










app.mainloop()






"""
ghi chú
pack(side=LEFT) là xài nhanh kiểu tự động sắp xếp điểm place
place(x=1,y=1) set vị trí x,y
grid(row=0,column=0) xet lưới là hàng hay cột
"""




