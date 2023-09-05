import pyttsx3
import speech_recognition as sp

engine = pyttsx3.init("sapi5") #SAPI5 (Speech Application Programming Interface 5) là một giao diện lập trình 
                               #ứng dụng được cung cấp bởi Microsoft để hỗ trợ các tính năng liên quan đến giọng nói trong các ứng dụng Windows. 
                               # Thông qua SAPI5, pyttsx3 có thể sử dụng các giọng đọc có sẵn trên hệ thống Windows để chuyển đổi văn bản thành giọng nói.

voices = engine.getProperty("voices")
engine.setProperty("voices",voices[0].id)

engine.setProperty('rate', 80)  # Tốc độ đọc là 150 (giá trị mặc định là 200)
engine.setProperty('volume', 2)  # Âm lượng là 0.8 (giá trị mặc định là 1.0)

def speak(text):
    engine.say(text)
    print(text)
    engine.runAndWait()

def command():
    r = sp.Recognizer()
    with sp.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=1,phrase_time_limit=5)
    
    try:
        print("reconizing...")
        querry = r.recognize_google(audio,language='en-US')
        print(f"user said:{querry}")
    except Exception as e:
        speak("Say that again please...")
    return querry



command()
speak("hello what are you doing")




