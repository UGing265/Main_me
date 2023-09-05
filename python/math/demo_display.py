import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Đường dẫn đến hình ảnh
image_path = 'ricardo1.png'

# Đọc hình ảnh
image = mpimg.imread(image_path)

# Hiển thị hình ảnh
plt.imshow(image)
plt.axis('off')  # Tắt hiển thị trục
plt.show()
