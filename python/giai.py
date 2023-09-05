#a = int(input())
#b = int(input())
##i=0
#for x in range(a, b):
# print(x)
"""
n = int(input())  #giải bài toán tìm số nhỏ trong list
lst = []
for i in range(n):
    lst.append(int(input())) #làm hàm mảng kinh điển
min_value = lst[0]
print("min",min_value)
for i in lst:  #i và lst luôn thay đổi theo giá trị trong list (i sẽ liệt kê trong list nên dễ nhớ hơn "chạy dữ liệu TRONG danh sách")
    print("i:",i)
    print("list:", lst)
    if i < min_value:
        print(i, "<", min_value)
        min_value = i
        print("true")
    else:
        print("false")
        print(i, "<", min_value)
        
    print()
print(min_value)
"""
n = int(input())
lst = []
for i in range(n):
  lst.append(int(input()))

ls = []
for i in lst:
  if i % 5 == 0:
     ls.append(int(i))
     