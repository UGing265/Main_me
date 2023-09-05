a = [1,2,3,4,5]
b = a.insert(7,"a")
print(a)
def move_zeros(lst):
    for a,i in enumerate(lst):
        if i == 0:
            lst.remove(i)
            lst.insert(999,0)
            
    return print(lst)
move_zeros([1,2,0,3,4,0])