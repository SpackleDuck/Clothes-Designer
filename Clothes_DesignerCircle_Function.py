
import tkinter
import os.path
import PIL.Image, PIL.ImageTk
root = tkinter.Tk()
shapes = []
canvas = tkinter.Canvas(root, width=1080, height=720, background='#FFFFFF')
canvas.grid(row=0,rowspan=2, column=1)
option = tkinter.IntVar()
directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(directory, 'shirt.png')
img = PIL.Image.open(filename) # create a PIL.Image from the jpg file
tkimg = PIL.ImageTk.PhotoImage(img) 
filename2 = os.path.join(directory, 'stick.jpg')
img2 = PIL.Image.open(filename2)
tkimg2 = PIL.ImageTk.PhotoImage(img2)
image_item = canvas.create_image(540,375, image=tkimg2)




shape =tkinter.Radiobutton(root, variable=option,
                        text='click for circle', value=0)
shape.grid(row=1,column=2)
shape2 =tkinter.Radiobutton(root, variable=option,
                    text='click for rectangle', value=1) 
shape2.grid(row=0,column=2)
shape3 =tkinter.Radiobutton(root, variable=option,
                    text='click for shirt', value=2) 
shape3.grid(row=0,columnspan=2,column=3)
option.set(0)

def down(event):
    global startx, starty
    startx = event.x 
    starty = event.y

def up(event):
    r = (startx-event.x)**2 + (starty-event.y)**2 
    r = int(r**.5)
    if option.get() == 0: 
        new_shape = canvas.create_oval(startx-r, starty-r, startx+r, starty+r,
                                     outline='#000000')
    elif option.get() == 1:
        new_shape = canvas.create_rectangle(startx-r, starty-r, startx+r, starty+r,
                                     outline='#000000')
    elif option.get() ==2:
        new_shape = canvas.create_image(540,360,image=tkimg)
    shapes.append(new_shape)
canvas.bind('<Button-1>', down)
canvas.bind('<ButtonRelease-1>', up)

root.mainloop()


