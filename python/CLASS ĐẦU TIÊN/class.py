class family:
    member=0
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
        self.member+=1
    def get_name(self):
        return print(str(self.member)+"."+str(self.__name))
    def get_age(self):
        return print(str(self.member)+"."+str(self.__age))
    
    def set_name(self,name):
        self.__name = name
    def set_age(self,age):
        self.__age = age

    Main_name=property(get_name,set_name) #add này để gọi gọn hơn nếu muốn khai báo tên trong ds thì sẽ trả get_name nếu muốn đổi tên hay truyền thì sẽ tự qua set_name
    Main_age=property(get_age,set_age)


DOTA = family("yo",30)

#DOTA.get_name()       #gọi cổ điển
#DOTA.set_name("SCAM")
#DOTA.get_name()

DOTA.Main_name


DOTA.name_get_hack = "Hacker01"
print(DOTA.name_get_hack)

def name_hacked(self,name_get_hack): #chèn thêm def vào class 
    self.name_get_hack = name_get_hack
    return self.name_get_hack
family.name_hacked = name_hacked
print(DOTA.name_hacked("SÍIS"))


