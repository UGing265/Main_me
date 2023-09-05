import pyttsx3

# Khởi tạo đối tượng "engine"
engine = pyttsx3.init()

# Lấy danh sách các giọng đọc có sẵn
voices = engine.getProperty('voices')


# Đặt giọng đọc mong muốn
engine.setProperty('voice', voices[0].id)  # Chọn giọng đọc đầu tiên trong danh sách

# Đặt tốc độ đọc và âm lượng
engine.setProperty('rate', 150)  # Tốc độ đọc là 150 (giá trị mặc định là 200)
engine.setProperty('volume', 0.8)  # Âm lượng là 0.8 (giá trị mặc định là 1.0)

# Chuyển đổi văn bản thành giọng nói
text = "hello, you suck suck suck suck suck ."
engine.say(text)
engine.runAndWait()
