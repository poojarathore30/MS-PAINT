from tkinter import *
import tkinter.ttk as ttk
from tkinter import colorchooser
from tkinter import filedialog
import PIL
from PIL import Image,ImageDraw,ImageGrab,ImageTk
from tkinter import messagebox
root=Tk()
root.title('Paint Peogram using Tkinter and Python')
root.geometry('800x800')
brush_color="black"
def paint(e):
	# change canvas background
	# my_canvas.config(bg='black')
	#Brush parameters
	#brush_color='green'
	brush_width='%0.0f' % float(my_slider.get())
	#brush types : BUTT <ROUND <PROJECTING
	brush_type2=brush_type.get()
	#startng position
	x1=e.x-1
	y1=e.y-1
	
	#ending Position
	x2=e.x+1
	y2=e.y+1
	#create line
	my_canvas.create_line(x1,y1,x2,y2,fill=brush_color,width=brush_width,capstyle=brush_type2,smooth=True)
	
#change the brush size
def change_brush_size(thing):
	slider_label.config(text='%0.0f' % float(my_slider.get()))
#change brush color
def change_brush_color():
	global brush_color
	brush_color="black"
	brush_color=colorchooser.askcolor(color=brush_color)[1]
	# color=Label(root,text=brush_color)
	# color.pack(pady=20)

#change canvas color
def change_canvas_color():
	global bg_color
	bg_color="black"
	bg_color=colorchooser.askcolor(color=bg_color)[1]
	my_canvas.config(bg=bg_color)

def clear_screen():
	my_canvas.delete(ALL)
	my_canvas.config(bg='white')

	#save image
def save_as_png():
	result=filedialog.asksaveasfilename(initialdir='C:/Users/Dell/Desktop/Python_learning/',filetypes=(("png files","*.png"),("all files","*.*")))
	if result.endswith('.png'):
		pass
	else:
		result+='.png'
	result_label=Label(root,text=result)
	result_label.pack(pady=20)
	if result:
		x=root.winfo_rooty()+my_canvas.winfo_x()
		y=root.winfo_rooty()+my_canvas.winfo_y()
		x1=x+my_canvas.winfo_width()
		y1=y+my_canvas.winfo_height()
		ImageGrab.grab().crop((x,y,x1,y1)).save(result)
		#popup success msg
		messagebox.showinfo("Image Saved","Boom !Your Image has been saved successfully !")
#create canvas	
w=600
h=400
bgcolor='black'
my_canvas=Canvas(root,width=w,height=h,bg='white')
my_canvas.pack(pady=20)
my_canvas.bind('<B1-Motion>',paint)
#Brush options frame

brush_options_frame=Frame(root)
brush_options_frame.pack(pady=20)

#brush width
brush_size_frame=LabelFrame(brush_options_frame,text='Brush Size')
brush_size_frame.grid(row=0,column=0,padx=50)
#Brush Slider

my_slider=ttk.Scale(brush_size_frame,from_=1,to=100,command=change_brush_size,orient=VERTICAL,value=10)
my_slider.pack(padx=10,pady=10)
#brush slider label
slider_label=Label(brush_size_frame,text=my_slider.get())
slider_label.pack(pady=5)

#brush types
brush_type_frame=LabelFrame(brush_options_frame,text='Brush Type',height=400)
brush_type_frame.grid(row=0,column=1,padx=50)
brush_type=StringVar()
brush_type.set('round')
#radio buttons for brush type
brush_type_radio1=Radiobutton(brush_type_frame,text='round ',variable=brush_type,value='round')
brush_type_radio2=Radiobutton(brush_type_frame,text='slash ',variable=brush_type,value='butt')
brush_type_radio3=Radiobutton(brush_type_frame,text='diamond ',variable=brush_type,value='projecting')
brush_type_radio1.pack(anchor=W)
brush_type_radio2.pack(anchor=W)
brush_type_radio3.pack(anchor=W)

#cahnge color
change_colors_frame=LabelFrame(brush_options_frame,text="Change Colors")
change_colors_frame.grid(row=0,column=2)

#change Brush Color Button
brush_color_button=Button(change_colors_frame,text="Brush Color",command=change_brush_color)
brush_color_button.pack(pady=10,padx=10)

#change canvas background color
canvas_color_button=Button(change_colors_frame,text="Canvas Color",command=change_canvas_color)
canvas_color_button.pack(pady=10,padx=10)

#program options Frame
options_frame=LabelFrame(brush_options_frame,text="program options")
options_frame.grid(row=0,column=3,padx=50)
#claer screen button
clear_button=Button(options_frame,text="Clear Screen",command=clear_screen)
clear_button.pack(padx=10,pady=10)
#save image

sav_image_button=Button(options_frame,text="Save to PNG",command=save_as_png)
sav_image_button.pack(padx=10,pady=10)





root.mainloop()