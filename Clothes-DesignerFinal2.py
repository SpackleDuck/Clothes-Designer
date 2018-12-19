
import tkinter
import os.path
import PIL.Image, PIL.ImageTk
root = tkinter.Tk()
root.wm_title('Clothes Designer')
shapes = []
canvas = tkinter.Canvas(root, width=180, height=350, background='#FFFFFF')
canvas.grid(row=0,rowspan=2, column=1)
option = tkinter.IntVar()
directory = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(directory, 'stick.jpg')
img = PIL.Image.open(filename) # create a PIL.Image from the jpg file
tkimg = PIL.ImageTk.PhotoImage(img) 
editor = tkinter.Text(root, width=10)
editor.grid(column=3, row=0, rowspan=3)
red_intvar = tkinter.IntVar()
green_intvar = tkinter.IntVar()
blue_intvar = tkinter.IntVar()
image_item = canvas.create_image(540,375, image=tkimg)

class ColorSlider(tkinter.Scale): # ColorSlider is a subclass of tkinter.Scale
    '''A Scale that reports to editor and stores in IntVar
    '''
    def __init__(self, parent, myLabel, model_intvar, editor, canvas):
        '''Creates a new ColorSlider'''
        # Define the event handler for the slider moving 
        def slider_changed(new_val):
            # Handler passes data from this controller to two views 
            
            
            
            # Create a hex string from the model data
            tk_color_string = color(red_intvar, green_intvar, blue_intvar)# the sliders' data
            # Tell the text window view about it
            editor.insert(tkinter.END, tk_color_string+'\n')
            editor.see(tkinter.END)
            # Tell the canvas view about it
            # The canvas view holds the model data in its internal canvas items
            # The viewer exposes the data through itemconfig() and itemcoords()
            canvas.itemconfig(shapes[-1],fill=tk_color_string, outline = tk_color_string)

        # To finish creating a ColorSlider, call the constructor for a regular
        # tkinter.Scale, associated with the model data and the event handler
        tkinter.Scale.__init__(self, parent, orient=tkinter.HORIZONTAL, from_=0, to=255,
                                variable=model_intvar, label=myLabel, command=slider_changed)
                
######
# Instantiate three sliders
#####

# Create and place the controllers
red_slider = ColorSlider(root, 'Red:', red_intvar, editor, canvas)
red_slider.grid(row=0, column=0, sticky=tkinter.W)

green_slider = ColorSlider(root, 'Green:', green_intvar, editor, canvas)
green_slider.grid(row=1, column=0, sticky=tkinter.W)

blue_slider = ColorSlider(root, 'Blue:', blue_intvar, editor, canvas)
blue_slider.grid(row=2, column=0, sticky=tkinter.W)    



#this creates the buttons to change what shape you wish to create
shape =tkinter.Radiobutton(root, variable=option,
                        text='click for circle', value=0)
shape.grid(rowspan=3,columnspan=2)
shape2 =tkinter.Radiobutton(root, variable=option,
                    text='click for square', value=1) 
shape2.grid(rowspan=3,columnspan=2)
shape3 =tkinter.Radiobutton(root, variable=option,
                    text='click for shirt', value=2) 
shape3.grid(rowspan=3,columnspan=2)

shape4 =tkinter.Radiobutton(root, variable=option,
                    text='click for pants', value=3) 
shape4.grid(rowspan=3,columnspan=2)
shape6 =tkinter.Radiobutton(root, variable=option, 
                    text = 'click to draw', value =4) 
shape6.grid(rowspan=3,columnspan =2)

shape5 =tkinter.Radiobutton(root, variable=option, 
                    text = 'click to clear', value =5) 
shape5.grid(rowspan=3,columnspan =2)
option.set(0)
option.set(0)

def down(event):
    global startx, starty
    startx = event.x 
    starty = event.y

def up(event):
    global tk_color_string
    tk_color_string = color(red_intvar, green_intvar, blue_intvar)
    r = (startx-event.x)**2 + (starty-event.y)**2 
    r = int(r**.5)
    #these option elifs determine which shape will be put down, and where, for instance the shirt and pants will go on the stick figure, while the circle and square will go where the user chooses
    if option.get() == 0: 
        new_shape = canvas.create_oval(startx-r, starty-r, startx+r, starty+r,
                                     outline='#000000')
        canvas.itemconfig(new_shape, tag="one")
    elif option.get() == 1:
        new_shape = canvas.create_rectangle(startx-r, starty-r, startx+r, starty+r,
                                     outline='#000000')
        canvas.itemconfig(new_shape, tag="two")
    elif option.get() ==2:
        new_shape = canvas.create_polygon(510,490,570,490,570,300,620,400,650,350,580,265,505,265,440,350,470,400,510,300,outline='#000000',width=5)
        canvas.itemconfig(new_shape, tag="three")
    elif option.get() ==3:
        new_shape= canvas.create_polygon(510,490,420,645,445,655,540,530,630,655,655,645,570,490)
        canvas.itemconfig(new_shape, tag="four")
    elif option.get() ==5:
        canvas.delete('one', 'two', 'three', 'four')   
    shapes.append(new_shape)
#binds the button for placing shapes to M1
canvas.bind('<Button-1>', down)
canvas.bind('<ButtonRelease-1>', up)

def hexstring(slider_intvar):
    '''A function to prepare data from controller's widget for view's consumption
    
    slider_intvar is an IntVar between 0 and 255, inclusive
    hexstring() returns a string representing two hexadecimal digits
    '''
    # Get an integer from an IntVar
    slider_int = slider_intvar.get()
    # Convert to hex
    slider_hex = hex(slider_int)
    # Drop the 0x at the beginning of the hex string
    slider_hex_digits = slider_hex[2:] 
    # Ensure two digits of hexadecimal:
    if len(slider_hex_digits)==1:
        slider_hex_digits = '0' + slider_hex_digits 
    return slider_hex_digits

def color(r,g,b):
    '''Takes three IntVar and returns a color tkinter string like #FFFFFF.        
    '''
    rx=hexstring(r)
    gx=hexstring(g)
    bx=hexstring(b)
    return '#'+rx+gx+bx

def paint (event):
    x1, y1 = (event.x -1), (event.y-1)
    x2, y2 = (event.x +1), (event.y +1)
    if option.get()==4:
        canvas.create_rectangle(x1,y1,x2,y2)
canvas.bind( '<B1-Motion>', paint)
root.mainloop()

