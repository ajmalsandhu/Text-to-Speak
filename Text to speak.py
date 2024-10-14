import os
import gtts
import playsound


while True:
    text = input("Enter what you want to speak (type 'quit' to exit) :  ")

    if text.lower() == 'quit':
        print("\nThanks for using...")
        break   # Exit the loop if the user types 'quit'

    sound = gtts.gTTS(text, lang="en")
    filename = "a.mp3"
    sound.save(filename)
    playsound.playsound(filename)

    # Remove the file after playing it
    os.remove(filename)
