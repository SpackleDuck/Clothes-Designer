import tkinter


root = tkinter.Tk()
root.wm_title('Clothes Designer')

shapes = []
canvas = tkinter.Canvas(root, width=800, height=600, background='#FFFFFF')
canvas.grid(row=1,rowspan=3, column=2)
editor = tkinter.Text(root, width=10)
editor.grid(column=3, row=0, rowspan=3)

red_intvar = tkinter.IntVar()
green_intvar = tkinter.IntVar()
blue_intvar = tkinter.IntVar()
# Create a list of circles on the canvas
shapes = []

#######
# Define a new class, an abstraction of the sliders
#######
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
red_slider.grid(row=1, column=0, sticky=tkinter.W)

green_slider = ColorSlider(root, 'Green:', green_intvar, editor, canvas)
green_slider.grid(row=2, column=0, sticky=tkinter.W)

blue_slider = ColorSlider(root, 'Blue:', blue_intvar, editor, canvas)
blue_slider.grid(row=3, column=0, sticky=tkinter.W)    

#rotation_slider = tkinter.IntVar()
#rotation_slider.set(1)
#def whatever(__self__):
 #   r = rotation_slider.get()
    
#radius_slider = tkinter.Scale(root, from_=1, to=180, variable=rotation_slider,    
 #                             label='y-position', command=whatever)
#radius_slider.grid(row=1, column=0, sticky=tkinter.W)

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
    global tk_color_string
    tk_color_string = color(red_intvar, green_intvar, blue_intvar)
    r = (startx-event.x)**2 + (starty-event.y)**2 
    r = int(r**.5)                               
    new_shape = canvas.create_oval(startx-r, starty-r, startx+r, starty+r,
                                    fill = tk_color_string, outline=tk_color_string, width = 10)
    shapes.append(new_shape)
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

root.mainloop()
