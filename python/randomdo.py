import random

def dota():
 a = 'end'
 #random.seed(100)
 print(random.random())
 x = random.randint(1,10)
 print("random số nguyên:",x)
 print("random số thực:",random.uniform(1,10))
 a = 'end'
 print()
 return a

def sisi():
 #prints a random value from the list
 list1 = [1, 2, 3, 4, 5, 6]
 print("random số:", random.choice(list1))
 
 # prints a random item from the string
 string = "striver"
 print("random chữ:", random.choice(string)) 
 return 

dota() #k có trả giá trị
print(dota()) #trả giá trị
print("----------------------------------------------------------")
sisi()

