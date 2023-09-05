gay = [1,2,3,4,5]
print(*gay)

def hi(*n):
    for i in n:
        print(i,end=" ")
    return n 
hi("ngu",hi("stupid","brug"),1,2,3,4)

a = hi("LOL")
if "LOL" in a:
    print("goodjob")