import tkinter


root = tkinter.Tk()
shapes = []
canvas = tkinter.Canvas(root, width=600, height=600, background='#FFFFFF')
canvas.grid(row=0,rowspan=2, column=1)
def down(event):
    global startx, starty
    startx = event.x 
    starty = event.y

def up(event):
    r = (startx-event.x)**2 + (starty-event.y)**2 
    r = int(r**.5)                               
    new_shape = canvas.create_oval(startx-r, starty-r, startx+r, starty+r,
                                     outline='#000000')
    shapes.append(new_shape)
canvas.bind('<Button-1>', down)
canvas.bind('<ButtonRelease-1>', up)

root.mainloop()
