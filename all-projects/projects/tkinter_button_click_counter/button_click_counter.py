from tkinter import *

root = Tk()
root.geometry("300x46")
root.resizable(1, 0)

numberOfClicks = 0

myLabel = Label(root, text=numberOfClicks, width=50)
myLabel.pack()

def addOne():
    global numberOfClicks
    numberOfClicks += 1
    myLabel.config(text=numberOfClicks)

myButton = Button(root, text="Click Me!",width=50, command=addOne)
myButton.pack()

root.mainloop()