from tkinter import *
import tkinter.messagebox as msgbox
import random

root = Tk()

root.title("Password Generator")

characters = '''a b c d e f g h i j  k l m n o p q r s t u v w x Y z 
A B C  D E F G H I J K L M N O P Q R S T U V W X Y Z 
@ # $ % &'''

arr = characters.split(" ")


def Button_clear():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)


def Button_password():
    length = int(entry2.get())
    entry3.delete(0, END)
    global arr
    password = ""
    for i in range(0, length):
        password = password+random.choice(arr)
    entry3.insert(0, password)


def Button_accept():
    name = entry1.get()
    password = entry3.get()
    content = name+"\n"+password
    root.clipboard_clear()  # Clear the clipboard
    root.clipboard_append(content)
    msgbox.showinfo("Copied", "Content copied to clipboard!")


label0 = Label(root, text="Password Generated", width=30, fg="blue")

label1 = Label(root, text="Enter User name", width=30)
label2 = Label(root, text="Enter Password Length", width=30)
label3 = Label(root, text="Generated Password", width=30)

entry1 = Entry(root, width=40)
entry2 = Entry(root, width=40)
entry3 = Entry(root, width=40)

button_1 = Button(root, text="Generate Password",
                  bg="blue", fg="white", borderwidth=5, command=Button_password)
button_2 = Button(root, text="Accept", fg="blue", bg="white",
                  borderwidth=5, command=Button_accept)
button_3 = Button(root, text="Reset", fg="blue", bg="white",
                  borderwidth=5, command=Button_clear)

label0.grid(row=0, column=0, columnspan=2)
label1.grid(row=1, column=0, padx=20, pady=20)
label2.grid(row=2, column=0, padx=20, pady=20)
label3.grid(row=3, column=0, padx=20, pady=20)


entry1.grid(row=1, column=1, padx=20, pady=20)
entry2.grid(row=2, column=1, padx=20, pady=20)
entry3.grid(row=3, column=1, padx=20, pady=20)

button_1.grid(row=4, column=1, padx=20, pady=10)
button_2.grid(row=5, column=1, padx=20, pady=10)
button_3.grid(row=6, column=1, padx=20, pady=10)


root.mainloop()
