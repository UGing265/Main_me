import numpy as np

# tạo một mảng các điểm dữ liệu
x = np.array([0, 1, 2, 3, 4])
y = np.array([0, 2, 4, 6, 8])

# tìm giá trị y tại x = 1.5
val = np.interp(1.5, x, y)
print("Giá trị y tại x = 1.5 là:", val)

# Kết quả sẽ in ra:
# Giá trị y tại x = 1.5 là: 3.0