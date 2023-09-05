import customtkinter as ctk
from PIL import Image,ImageTk
import tkinter as tk



def user():
        a1 =entry1.get()
        with open("E:\\CC+\\python\\dự án\\phần mềm basic\\hi.txt","w") as f:
         f.write(a1)#ý tưởng tiếp theo là dupe file txt từng tài khoản (tk1.txt,tk2.txt,tk3.txt,... điển hình)
                    #tạo if để xác minh hợp lệ không ?
                    #tạo pass
                    #tạo homepage đầu tiên
                    #lưu tất cả dữ liệu từ bài học (color.py,helloworld.py) 
                    #màu sắc trang trí
                    #mở được phần mềm = exe mà vẫn không làm hỏng file khác
tv = ctk.CTk()

tv.geometry("700x500")
ctk.set_appearance_mode("Dark")


bg = ImageTk.PhotoImage(Image.open("bg1.png"))
gay = ctk.CTkLabel(master=tv,image=bg)
gay.pack()


shape = ctk.CTkFrame(master=gay,width=320,height=320)
shape.place(relx=0.5,rely=0.5, anchor=tk.CENTER)

text = ctk.CTkLabel(master=shape,text="resgiter",font=("Century Gothic", 60))
text.place(x=30,y=5)


l2 = ctk.CTkLabel(master=shape, text="log into your account",font=("Century Gothic", 20))
l2.place(x=40,y=50)

entry1= ctk.CTkEntry(master=shape, width=220, placeholder_text="Username")
entry1.place(x=50, y= 100)

entry2= ctk.CTkEntry(master=shape, width=220, placeholder_text="Password")
entry2.place(x=50, y= 150)

l3 = ctk.CTkLabel(master=shape, text="Forgot passwork ?", font=("Century Gothic",15))
l3.place(x=150,y=180)

button1= ctk.CTkButton(master=shape,width=220, text="Login", corner_radius=20,command=user)
button1.place(x=45,y= 240)









tv.mainloop()

