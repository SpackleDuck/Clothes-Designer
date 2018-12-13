import tkinter


root = tkinter.Tk()
shapes = []
canvas = tkinter.Canvas(root, width=300, height=300, background='#FFFFFF')
canvas.grid(row=0,rowspan=2, column=1)
option = tkinter.IntVar()

shape =tkinter.Radiobutton(root, variable=option,
                        text='click for circle', value=0)
shape.grid(row=2,column=2)
shape2 =tkinter.Radiobutton(root, variable=option,
                    text='click for rectangle', value=1) 
shape2.grid(row=1,column=2)
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
    shapes.append(new_shape)
canvas.bind('<Button-1>', down)
canvas.bind('<ButtonRelease-1>', up)

root.mainloop()
