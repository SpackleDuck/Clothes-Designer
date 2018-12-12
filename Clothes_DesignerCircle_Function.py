import tkinter


root = tkinter.Tk()
root.wm_title('Clothes Designer')

shapes = []
canvas = tkinter.Canvas(root, width=1080, height=720, background='#FFFFFF')
canvas.grid(row=0,rowspan=2, column=1)
editor = tkinter.Text(root, width=10)
editor.grid(column=2, row=0, rowspan=3)

def down(event):
    global startx, starty
    startx = event.x 
    starty = event.y

def up(event):
    r = (startx-event.x)**2 + (starty-event.y)**2 
    r = int(r**.5)                               
    new_shape = canvas.create_oval(startx-r, starty-r, startx+r, starty+r,
                                     outline='#000000', width = 10)
    shapes.append(new_shape)
canvas.bind('<Button-1>', down)
canvas.bind('<ButtonRelease-1>', up)

root.mainloop()
