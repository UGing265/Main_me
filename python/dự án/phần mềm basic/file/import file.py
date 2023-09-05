#2 pp
####################################
f  = open("E:\\CC+\\python\\dự án\\phần mềm basic\\file\\gay.txt","r")

print(f.mode)

f.close()

###################################
with open("E:\\CC+\\python\\dự án\\phần mềm basic\\file\\gay.txt","r") as f:
    print(f.name)
    pass
##################################
with open("E:\\CC+\\python\\dự án\\phần mềm basic\\file\\gay.txt","r") as f:
    dota = f.read(50)#50 kí tự
   
    print(dota)
    pass
##################################
print()
with open("E:\\CC+\\python\\dự án\\phần mềm basic\\file\\gay.txt","r") as f:
  
    dota2 = f.readlines() #readline() là read từng dòng nếu gọi nó
    print(dota2)
    pass
##################################
print()
with open("E:\\CC+\\python\\dự án\\phần mềm basic\\file\\gay.txt","r") as f: #"r" là đọc
  
    for dota in f:
        print(dota,end="") #ctrl + K + C
    f.seek(0) # yêu cầu đọc lại
    pass
#################################
print()
with open("E:\\CC+\\python\\dự án\\phần mềm basic\\file\\writeme.txt","r+") as wf:
    
        wf.write("how are you my name is gay")
        wf.seek(0)
        a= wf.read()
        print(a)
print()
########################

with open("E:\\CC+\\python\\dự án\\phần mềm basic\\file\\bg1.png","rb") as rf:
     with open("E:\\CC+\\python\\dự án\\phần mềm basic\\file\\bg1dota.png","wb") as wf:
          for line in rf:
               wf.write(line)


