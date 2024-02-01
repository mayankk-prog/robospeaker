
import os

while True:
    print("welcome to RoboSpeaker")
    x= input("Enter what you want oto speak")
    command=    "  PowerShell -Command \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{}');\" ".format(x)
    os.system(command)

'''
import os

while True:
    text = input("Type something to speak aloud (or 'quit' to exit): ")
    if text.lower() == "quit":
        break

    # Use PowerShell to invoke text-to-speech
    os.system("PowerShell -Command \"Add-Type –AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{}');\"".format(text))
'''