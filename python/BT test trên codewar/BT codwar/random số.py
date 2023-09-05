import random

# Chọn số thứ nhất khác 0
a = random.randint(1, 999999)

# Chọn số thứ hai khác số thứ nhất
b = random.randint(0, 999999)
while b == a:
    b = random.randint(0, 999999)

# Chọn số thứ ba, c, d, e
bcd_sum = a * 100000 + b
bcd_sum_diff = 786040 - bcd_sum
c = random.randint(0, 999999)
while c == b or c == bcd_sum_diff // 100000:
    c = random.randint(0, 999999)

bcd_sum += c * 10000
bcd_sum_diff = 786040 - bcd_sum
d = random.randint(0, 999999)
while d == b or d == c or d == bcd_sum_diff // 10000:
    d = random.randint(0, 999999)

bcd_sum += d * 1000
bcd_sum_diff = 786040 - bcd_sum
e = random.randint(0, 999999)
while e == b or e == c or e == d or e == bcd_sum_diff // 1000:
    e = random.randint(0, 999999)

# In kết quả
print(f"a = {a}")
print(f"b = {b:05d}")
print(f"c = {c:05d}")
print(f"d = {d:05d}")
print(f"e = {e:05d}")
total = a + b + c + d + e
print(total)