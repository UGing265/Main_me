import speech_recognition
import pyttsx3

robot_mouth = pyttsx3.init()
robot_ear = speech_recognition.Recognizer()


with speech_recognition.Microphone() as mic:
    print("Robot : I'm listening")
    audio = robot_ear.listen(mic)
try:
    you = robot_ear.recognize_google(audio)
except:
    you = ""
print("You: " + you)


if you == "hello" or you == "hi":
    robot_brain = "Hello Bitch"
elif you == "today":
    robot_brain = "thu 4" 
   
elif you =="":
    robot_brain  = " I can't hear you please say again "
else :
    robot_brain = "Bye Bitch"
print(robot_brain)




robot_mouth.say(robot_brain)
robot_mouth.runAndWait()