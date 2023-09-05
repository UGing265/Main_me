
"""
Cho trước chuỗi s được nhập từ bàn phím, bạn hãy viết chương trình để đảo ngược thứ tự xuất hiện của các từ trong chuỗi s và sau đó hiển thị ra màn hình chuỗi đã được xử lý. 

Ví dụ

Nếu bạn nhập s = "Python Exercises" thì màn hình sẽ hiển thị ra "Exercises Python"
Nếu bạn nhập s = "This is an apple" thì màn hình sẽ hiển thị ra "apple an is This"
Gợi ý
Hoàn thành bài tập này bằng cách sử dụng hàm join() và split()
"""
s = str(input())
list= ' '

a = s.split(list)
print(a)
print(list)

result = a[::-1]
list2 = ' '
finished = list2.join(result)
print(finished)
print(len(finished))




text = "ez dota ricardo"
text = text.split(" ")
print(text)
text = text[::-1]

list = " "
text = list.join(text)
print(text)



