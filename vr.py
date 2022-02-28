import wikipedia
from tkinter import *
import speech_recognition as sr


def check_exit(text):
    if text == "stop":
        return True
    if text == "रुको":
        return True
    if text == "थांबा":
        return True


def virtual_assistant(il, wl):
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening.....")
            audio = r.listen(source)
            try:
                print("Recognizing....")
                text = r.recognize_google(audio, language=il)
                print('You said: ' + text)
                if check_exit(text):
                    print("The program will exit...")
                    exit()
                else:
                    window = Tk()
                    window.geometry("700x600")
                    wikipedia.set_lang(wl)
                    answer = wikipedia.summary(text, sentences=5)
                    label1 = Label(window, justify=LEFT, wraplength=650, compound=CENTER, padx=10, text=answer,
                                   fg='#1a1b1c',
                                   bg='#f4dbb0', font='times 15 bold')
                    label1.pack()
                    window.after(500000, lambda: window.destroy())
                    mainloop()

            except Exception as e:
                print(e)
                answer = "Sorry we can't hear you"
                print(answer)
