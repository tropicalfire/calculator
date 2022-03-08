from tkinter import *

from click import command

root = Tk()  #Tk object

'''
newFrame = Frame(root)
newFrame.pack()

otherFrame= Frame(root) #container which hold up the widgets. Window contains frame which contains widgets
otherFrame.pack(side = BOTTOM)

button1= Button(newFrame, text="Click here", fg="Red")
button2= Button(otherFrame, text="Click here 2", fg="Blue")

button1.pack()
button2.pack()

'''
'''

#textfield, entry, arranging items in grid

label1 = Label(root, text = "Firstname")
label2 = Label(root, text = "Lastname")

entry1 = Entry(root)
entry2 = Entry(root)

label1.grid(row = 0, column = 0) #arrange values in a grid
label2.grid(row = 1, column = 0)

entry1.grid(row = 0, column = 1)
entry2.grid(row=1, column = 1)
'''
'''
#self-adjusting widgets

label1 = Label(root, text = "First", bg = "Red", fg = "White")
label1.pack(fill = X) #adjust the label to the width, parameter x

label2 = Label(root, text = "Second", bg = "Blue", fg = "White")
label2.pack(side=LEFT, fill=Y)
'''
'''
#button functions

def dosomething():
    print("Something")

button1 = Button(root, text = "click here", command = dosomething)
button1.pack()
'''
'''
#use classes

class MyButtons:

    def __init__(self, root1):
        frame = Frame(root1)
        frame.pack()

        self.printButton = Button(frame, text = "Click here", command = self.printMessage)
        self.printButton.pack()

        self.quitButton = Button(frame, text = "Exit", command = frame.quit)
        self.quitButton.pack(side = LEFT)

    def printMessage(self):
        print("Button Clicked")

b = MyButtons(root) #this line creates a myButton object which will create a frame and 2 buttons immediately.
'''

#drowdown menues

def function1():
    print('Menu item clicked')

mymenu = Menu(root)
root.config(menu = mymenu)

submenu = Menu(mymenu)

mymenu.add_cascade(label = "File", menu = submenu)
submenu.add_command(label = "Project", command = function1)
submenu.add_command(label = "Save", command = function1)

submenu.add_separator()
submenu.add_command(label = "Exit", command= function1)

root.mainloop() #window in a loop, doesnt immediately close




