from tkinter import *
import pyttsx3
from google.cloud import translate
# from translation import google

languages = {
    'English': 'en',
    'Urdu': 'ur',
    'Gujarati': 'gu',
    'Tamil': 'ta',
    'Bengali': 'bn',
    'Hindi': 'hi',
    'Telugu': 'tu',
    'Kannada': 'kn',
}

translate_client = translate.Client()


def convert(*args):
    try:
        text = str(val.get())               # source

        target = str(value.get())           # lang selection

        t = languages[target]

        translation = translate_client.translate(
            text,
            target_language=t)

        t1.insert(END, translation['translatedText'])
    except KeyError:
        print('No such key found')
    return translation


def audio(*args):
    engine = pyttsx3.init()
    engine.say('Hello')
    engine.runAndWait()


lang_keys = list(languages.keys())

lang_values = list(languages.values())

window = Tk()

window.geometry('500x500')

window.title('Translator')

Label(text='Enter your text: ').grid(row=0, column=0)


# source input
val = StringVar()
e1 = Entry(window, textvariable=val, width=40)

e1.grid(row=0, column=1)

# Drop down list for output

value = StringVar()

# value.set("auto")     # sets auto as default value

# For getting support of all languages

# l1 = OptionMenu(window, value, *lang_values, command=convert)

l1 = OptionMenu(window, value, 'Hindi', 'English', 'Bengali', 'Kannada', 'Tamil', 'Gujarati', 'Urdu', command=convert)
# print(value.get)
l1.grid(row=0, column=2)

# Drop down list for input language
v = StringVar()
Label(text='Translated text: ').grid(row=1, column=0)

# desired output textfield
t1 = Text(window, height=1, width=30)
t1.grid(row=1, column=1)

photo = PhotoImage(file='audio.png')

b2 = Button(window, command=audio, image=photo)
b2.grid(row=1, column=2)

# conversion button
b1 = Button(window, text="Convert", command=convert)
b1.grid(row=2, column=1)

window.mainloop()
