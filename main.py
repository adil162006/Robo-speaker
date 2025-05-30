import os
import pyttsx3


if __name__ == '__main__':
    engine = pyttsx3.init()
    print("welcome to RoboSpeaker 1.1. Created by Adil ")
    while True:
        x=input("Enter What you want me to speak ")
        if x.lower()=="exit" :
            break
        engine.say(x)
        engine.runAndWait()
