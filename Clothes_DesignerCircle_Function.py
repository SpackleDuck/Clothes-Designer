import tkinter


root = tkinter.Tk()
root.wm_title('Clothes Designer')

shapes = []
canvas = tkinter.Canvas(root, width=1080, height=720, background='#FFFFFF')
canvas.grid(row=0,rowspan=2, column=1)
editor = tkinter.Text(root, width=10)
editor.grid(column=2, row=0, rowspan=3)

rotation_slider = tkinter.IntVar()
rotation_slider.set(0)
#class RotationSlider(tkinter.Scale):
 #       def __init__(self, parent, myLabel, model_intvar, editor, canvas):
  #          def slider_changed(newval):
    #                tk_rotation = rotation_slider
   #                 editor.insert(tkinter.END, tk_rotation+'\n')
     #               editor.see(tkinter.END)
      #              canvas.itemconfig(shapes[-1],fill=tk_rotation)
       #             tkinter.Scale.__init__(self, parent, orient=tkinter.HORIZONTAL, from_=0, to=255,
        #                        variable=model_intvar, label=myLabel, command=slider_changed)
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
