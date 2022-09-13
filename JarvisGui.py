from jarvisUI import Ui_JarvisUI_2
from PyQt5 import QtCore , QtWidgets , QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
import pyttsx3
from playsound import playsound
import speech_recognition as sr
import sys
import wikipedia

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices' , voices[0].id)
engine.setProperty('rate' , 210)

def speak(audio):
    print(f"{audio}")
    engine.say(audio)
    engine.runAndWait()


class MainThread(QThread):
    def __init__(self):
        super(MainThread , self).__init__()

    def run(self):
        self.Task_Exec()

    def takecommand(self):
        r=sr.Recognizer()
        with sr.Microphone() as source:
            speak("i listen your magic .. .. .. !!")
            print("Listening .. .. .. !!")
            r.pause_threshold= 1
            r.adjust_for_ambient_noise(source , duration=1)
            r.energy_threshold= 400
            audio=r.listen(source)

        try: 
            speak("Recognizing .. .. .!!")
            print("Recognizing .. .. .!!")
            speak("Getting information .. .. .. !!")
            print("Getting information .. .. .. !!")
            query = r.recognize_google(audio , language='en-in').lower()
            speak(f"You said :- {query}\n")
            print(f"You said :- {query}\n")

        except Exception : 
            speak('Sorry sir! I didn\'t get that! Try typing the command!')
            query = str(input('Command: '))
            return"None"
        return query.lower()    

    def Task_Exec(self):
            # music()
            speak(" Starting all system applications ...!!!!! ..            Installing all drivers...          !!!!!        Callibrating     and    examining     all    code          processes..!!!!!        all system have been started.....     Initialising databases.      !!!!!!!!!!Connecting to internet..!!!!!Now Iam online ..!!! ... Hello , iam zira.., a digital assistant..")
            # wishme()
            speak(" Now iam ready for your commands..!!!! Tell me how may i help you..!!")
            while True:
            # if 1:

                self.query=self.takecommand().lower()


                if 'hello' in self.query:
                    speak(f"hello mayank ..!!")
                
                elif 'tell me something about you' in query or 'Who are you' in self.query:
                    speak(f"hello !!iam zira..!!!!...... Iam a digital assistant.........!!...... my creator is mayank........!!!..... iam developed to make things easier!!....... Iam trained to chat with users and talk to them.......!!...... iam written in python and is currently under development .........!!!......iam sure very soon mayank develops me completely and will install  advance features in me...... .,!!...... Thank you..!!!..!!") 

                elif  'wikipedia' in query or 'Give me information about'  in self.query:
                    speak("Building connection .. !! connecting to wikipedia .. ..!! Gathering information from wikipedia..!!")
                    query=query.replace("wikipedia" , "")
                    results = wikipedia.summary(query , sentences=4)
                    speak("According to wikipedia .. ..!!")
                    print(results)
                    speak(results) 

                elif "what's up" in self.query :
                    speak(f"Iam fine..!! nothing special to tell ..!! how areee uh..!!" )
                    
                elif 'Can you help me ' in self.query or 'Can i ask you something' in self.query:
                    speak(f"yes Mayank..!! ofcousre ..!! iam here for helping uh only ..!! you can ask anything..!!")

                elif 'what is the time' in self.query:
                    strTime=datetime.datetime.now().strftime("%I:%M %p")
                    print(f"the current time is {strTime}")
                    speak(f"the current time is {strTime}")

                elif ' Exit ' in self.query :
                    speak(f"Thank you  for giving your valuable time...")
                    speak(f"Turning off all applications...")
                    speak(f"Quitting ... Have a good day MAYANK")
                    speak(f"Good Bye...")
                    sys.exit()





startFunctions = MainThread()

class Gui_Start(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui  = Ui_JarvisUI_2()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.startFunc)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startFunc(self):

        self.ui.movies = QtGui.QMovie("3.gif")
        self.ui.label.setMovie(self.ui.movies)
        self.ui.movies.start()

        self.ui.movies_2 = QtGui.QMovie("1.gif")
        self.ui.label_2.setMovie(self.ui.movies_2)
        self.ui.movies_2.start()

        self.ui.movies_3 = QtGui.QMovie("7.gif")
        self.ui.label_3.setMovie(self.ui.movies_3)
        self.ui.movies_3.start()

        self.ui.movies_4 = QtGui.QMovie("5.gif")
        self.ui.label_4.setMovie(self.ui.movies_4)
        self.ui.movies_4.start()

        self.ui.movies_5 = QtGui.QMovie("4.gif")
        self.ui.label_5.setMovie(self.ui.movies_5)
        self.ui.movies_5.start()

        self.ui.movies_6 = QtGui.QMovie("6.gif")
        self.ui.label_6.setMovie(self.ui.movies_6)
        self.ui.movies_6.start()

        self.ui.movies_7 = QtGui.QMovie("8.gif")
        self.ui.label_7.setMovie(self.ui.movies_7)
        self.ui.movies_7.start()

        self.ui.movies_8 = QtGui.QMovie("9.gif")
        self.ui.label_8.setMovie(self.ui.movies_8)
        self.ui.movies_8.start()

        startFunctions.start()


Gui_app = QApplication(sys.argv)
Gui_Jarvis = Gui_Start()
Gui_Jarvis.show()
exit(Gui_app.exec_())