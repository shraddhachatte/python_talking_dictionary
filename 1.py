
import tkinter as tk
from tkinter import PhotoImage, Label, Text, Entry, Button, messagebox
import json
import pyttsx3
from difflib import get_close_matches

engine = pyttsx3.init()

def wordaudio():
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(enterwordentry.get())
    engine.runAndWait()

def meaningaudio():
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(textarea.get(1.0, tk.END))
    engine.runAndWait()

def iexit():
    res = messagebox.askyesno('Confirm', 'Do you want to exit?')
    if res == True:
        root.destroy()
    else:
        pass

def clear():
    textarea.config(state=tk.NORMAL)
    enterwordentry.delete(0, tk.END)
    textarea.delete(1.0, tk.END)
    textarea.config(state=tk.DISABLED)

def search():
    data = json.load(open('C:/Users/Hp/Desktop/talking dic/Talking Dictionary/data.json'))

    # data = json.load(open('data.json'))
    word = enterwordentry.get().lower()

    if word in data:
        
        meaning = data[word]
        
        textarea.config(state=tk.NORMAL)
        
        textarea.delete(1.0, tk.END)
       
        for item in meaning:
            
            textarea.insert(tk.END, u'\u2022' + item + '\n\n')
        
        textarea.config(state=tk.DISABLED)
    
    elif len(get_close_matches(word, data.keys())) > 0:
        
        close_match = get_close_matches(word, data.keys())[0]
        
        res = messagebox.askyesno('Confirm', 'Did you mean ' + close_match + ' instead?')
        
        if res == True:
            
            meaning = data[close_match]
            
            textarea.delete(1.0, tk.END)
            
            textarea.config(state=tk.NORMAL)
            
            for item in meaning:
                
                textarea.insert(tk.END, u'\u2022' + item + '\n\n')
           
            textarea.config(state=tk.DISABLED)
        else:
           
            textarea.delete(1.0, tk.END)
            
            messagebox.showinfo('Information', 'Please type a correct word')
            
            enterwordentry.delete(0, tk.END)
    else:
       
        messagebox.showerror('Error', 'The word doesn\'t exist. Please double-check it.')
        
        enterwordentry.delete(0, tk.END)

root = tk.Tk()

root.geometry('1000x626+100+50')

root.title('Talking Dictionary ')

root.resizable(0, 0)

bgimage = PhotoImage(file='C:/Users/Hp/Desktop/talking dic/Talking Dictionary/bg.png')

bgLabel = Label(root, image=bgimage)

bgLabel.place(x=0, y=0)

enterwordLabel = Label(root, text='Enter Word', font=('castellar', 29, 'bold'), fg='red3', bg='whitesmoke')

enterwordLabel.place(x=530, y=20)

enterwordentry = Entry(root, font=('arial', 23, 'bold'), bd=8, relief=tk.GROOVE, justify=tk.CENTER)

enterwordentry.place(x=510, y=80)

enterwordentry.focus_set()

searchimage = PhotoImage(file='C:/Users/Hp/Desktop/talking dic/Talking Dictionary/search.png')

searchButton = Button(root, image=searchimage, bd=0, bg='whitesmoke', activebackground='whitesmoke', cursor='hand2',
                      command=search)

searchButton.place(x=620, y=150)

micimage = PhotoImage(file='C:/Users/Hp/Desktop/talking dic/Talking Dictionary/mic.png')

micButton = Button(root, image=micimage, bd=0, bg='whitesmoke', activebackground='whitesmoke',
                   cursor='hand2', command=wordaudio)

micButton.place(x=710, y=153)

meaninglabel = Label(root, text='Meaning', font=('castellar', 29, 'bold'), fg='red3', bg='whitesmoke')

meaninglabel.place(x=580, y=240)

textarea = Text(root, font=('arial', 18, 'bold'), height=8, width=34, bd=8, relief=tk.GROOVE, wrap='word')

textarea.place(x=460, y=300)


audioimage = PhotoImage(file='C:/Users/Hp/Desktop/talking dic/Talking Dictionary/microphone.png')

audioButton = Button(root, image=audioimage, bd=0, bg='whitesmoke', activebackground='whitesmoke',
                     cursor='hand2', command=meaningaudio)

audioButton.place(x=530, y=555)

clearimage = PhotoImage(file='C:/Users/Hp/Desktop/talking dic/Talking Dictionary/clear.png')

clearButton = Button(root, image=clearimage, bd=0, bg='whitesmoke', activebackground='whitesmoke', cursor='hand2',
                     command=clear)

clearButton.place(x=660, y=555)

exitimage = PhotoImage(file='C:/Users/Hp/Desktop/talking dic/Talking Dictionary/exit.png')


exitButton = Button(root, image=exitimage, bd=0, bg='whitesmoke', activebackground='whitesmoke', cursor='hand2',
                    command=iexit)

exitButton.place(x=790, y=555)

root.mainloop()
