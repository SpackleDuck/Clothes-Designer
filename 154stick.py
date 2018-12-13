import tkinter
import os.path
import PIL.Image, PIL.ImageTk 
root= tkinter.Tk()
canvas = tkinter.Canvas(root,width=1080,height=720)
canvas.grid(row=0,rowspan=2,column=1)
directory = os.path.dirname(os.path.abspath(__file__)) 
filename = os.path.join(directory, 'stick.jpg')
img = PIL.Image.open(filename)
tkimg = PIL.ImageTk.PhotoImage(img)
image_item = canvas.create_image(540,360, image=tkimg)
root.mainloop() 