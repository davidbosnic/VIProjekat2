# This is a sample Python script.
import speech_recognition as sr
from tkinter import *
from gtts import gTTS
from playsound import playsound
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def Text_to_speech():
    label1.configure(text="")
    label1.update()
    Message = entry_field.get()
    if not Message:
        label1.configure(text="No entered text for transforming !")
        label1.update()
        return
    speech = gTTS(text = Message, lang=Msg3.get())

    reader = open('counter.txt', 'r')
    counter = int(reader.readline())
    speech.save('Soundtrack'+str(counter)+'.mp3')
    playsound('Soundtrack'+str(counter)+'.mp3')
    counter += 1
    reader.close()

    writer = open('counter.txt', 'w')
    writer.write(str(counter))
    writer.close()

def Exit():
    root.destroy()

def Reset():
    Msg.set("")
    Msg2.set("")
    Msg4.set("")
    label1.configure(text="")
    label1.update()

def STT():
    label1.configure(text="")
    label1.update()
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        if not Msg4.get():
            label1.configure(text="Duration of listening mic is empty !")
            label1.update()
            return
        if not RepresentsInt(Msg4.get()):
            label1.configure(text="Duration must be entered as integer !")
            label1.update()
            return
        if int(Msg4.get()) < 1:
            Msg4.set(1)
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        label1.configure(text="Speek now !")
        label1.update()
        recorded_audio = recognizer.listen(source, timeout=int(Msg4.get()))

    try:
        label1.configure(text="Working !")
        label1.update()
        text = recognizer.recognize_google(
            recorded_audio,
            language=Msg3.get()
        )
        entry_field2.delete(0, END)
        entry_field2.insert(0, format(text))
        print("Decoded Text : {}".format(text))
        label1.configure(text="")
        label1.update()

    except Exception as ex:
        print(ex)
# Press the green button in the gutter to run the script.

def RepresentsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

root = Tk()
root.geometry("700x400")
root.configure(bg='ghost white')
root.title("TTS and STT")

Label(root, text="Terminator converter", font="arial 20 bold", bg='white smoke').pack()

Msg = StringVar()
Label(root, text="Enter Text", font='arial 15 bold', bg='white smoke').place(x=20, y=60)

entry_field = Entry(root, textvariable=Msg, width='50')
entry_field.place(x=20, y=100)

Label(root, text="Recognized text:", font='arial 15 bold', bg='white smoke').place(x=20, y=140)

Msg2 = StringVar()
entry_field2 = Entry(root, textvariable=Msg2, width='50')
entry_field2.place(x=20, y=180)


label1 = Label(root, text='', font='arial 15 bold', bg='white smoke', fg='red' )
label1.place(x=300, y=140)


Msg4 = StringVar()
entry_field4 = Entry(root, textvariable=Msg4, width='20')
entry_field4.place(x=150, y=300)

Button(root, text="TTS", font='arial 15 bold', command=Text_to_speech, width='4', bg='Blue').place(x=25, y=220)

Button(root, font='arial 15 bold', text='EXIT', width='4', command=Exit, bg='OrangeRed1').place(x=175, y=220)

Button(root, font='arial 15 bold', text='STT', width='4', command=STT, bg='Yellow').place(x=100, y=220)

Button(root, font='arial 15 bold', text='RESET', width='6', command=Reset).place(x=250, y=220)

Label(root, text="Language:", font='arial 10 bold', bg='white smoke').place(x=50, y=270)
Label(root, text="Duration of listening mic:", font='arial 10 bold', bg='white smoke').place(x=150, y=270)

Msg3 = StringVar()
OptionMenu(root, Msg3, "en-US", "sr").place(x=50, y=300)
Msg3.set("en-US")

root.mainloop()




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
