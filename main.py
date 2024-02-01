
import os

while True:
    print("welcome to RoboSpeaker")
    x= input("Enter what you want oto speak")
    command=    "  PowerShell -Command \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{}');\" ".format(x)
    os.system(command)
