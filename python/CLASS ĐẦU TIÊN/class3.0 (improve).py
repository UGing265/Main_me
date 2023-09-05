class asus:
    def __init__(self,cpu):
        self.LOL = cpu #self là add thuộc tính (attribute) vào để lưu trữ (self.cpu=cpu k cần trùng có thể add thuộc tính khác)
        print(self.LOL)             #chính vì đó là __init__ nên sẽ khởi động trc mọi thứ đây



a = asus("gay")



i = 0
a = int(input())
for b in range(i,a):
    s = input("giá trị ?:")