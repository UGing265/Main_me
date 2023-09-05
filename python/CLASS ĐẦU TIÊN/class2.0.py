"""
__________nhiệm vụ_________
tạo danh sách❌ (sử dụng class có lẽ sẽ tiện)
kn QR quét❌ (import QR)
tạo công cụ cần dò nhanh❌ (?)
setup tính năng để truy cập❌ (sử dụng lựa chọn input chẳng hạn ra yêu cầu)
có khả năng save khi tắt ❌ (tạo txt )
chỉnh sửa đc, list đc, thống kê,...❌ (tạo txt sau đó paste ra)
"""
import random

class lophoc:

    def __init__(self,cnumber,name="tên trống"):

        self.__cnumber=cnumber
        self.__name=name

    def __str__(self):
       
        return f"\n Trong danh sách có mã số và tên: {self.__cnumber}.{self.__name.upper()}\n"
        
    def get_stt(self):
        return print(f"{str(self.__cnumber)}")
    def get_name(self):
        return print(f"{str(self.__name)}")

test = lophoc(5,"Neko Ricardo")
gay = lophoc(24,"Gay_Dota")
Abe = lophoc(52,"Abedo")
d = lophoc(42)
#A12 = lophoc([1,2,3,4,5,6,7,8,9,10],["Khanh","Khoa","Khang","Kha","Kada","Korea","Kdiwi","Krack","Khung","Kim"])

print(test)
print(gay)
print(Abe)
print(d)