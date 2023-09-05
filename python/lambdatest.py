# x = lambda a : a + 10
# print(x(4))

# x = lambda a, b, c: a*b+c #hàm ẩn
# print(x(5,1,5))


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)



print(mydoubler(11))



def test(n):
  return lambda a: a + n

doub = test(2)
print(doub(5))