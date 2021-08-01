import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile
from tkinter import filedialog

window = tk.Tk()
window.resizable(False, False)
window.title("Convertisseur d'image")
window.eval('tk::PlaceWindow . center')
window.geometry("650x560")

def show_frame(frame_name):
    frame_name.tkraise()

#==================Preview before converting===============#
def resize_image_gnb():                                                                    
    global resized_image_gnb
    global im_gnb
    global width_to_know_gnb
    im_gnb = Image.open (file)
    width, height = im_gnb.size
    if width > height:
        height = int(300/width*height)
        width = 300        
    elif height > width:
        width = int(300/height*width)
        height = 300
    else:
        width, height = 300, 300
    resized_image_gnb = im_gnb.resize((width, height))
    width_to_know_gnb = width

def image_render_gnb():
    global render_image_gnb
    global render_label_gnb
    resize_image_gnb()
    render_image_gnb = ImageTk.PhotoImage(resized_image_gnb)
    render_label_gnb = tk.Label(gnb_frame, image=render_image_gnb , bg="#292d3e")
    render_label_gnb.place(x=((650-width_to_know_gnb)/2), y=280)
#==========================================================#
#==================Preview before saving===================#
def resize_image_preview():                                                                    
    global resized_image_preview
    global width_to_know_preview
    im_preview = im2
    width, height = im2.size
    if width > height:
        height = int(300/width*height)
        width = 300
    elif height > width:
        width = int(300/height*width)
        height = 300
    else:
        width, height = 300, 300
    resized_image_preview = im_preview.resize((width, height))
    width_to_know_preview = width    

def image_render_preview():
    global render_image_preview
    global render_label_image_preview
    resize_image_preview()
    render_image_preview = ImageTk.PhotoImage(resized_image_preview)
    render_label_preview = tk.Label(save_frame, image=render_image_preview, bg="#292d3e") #================Add rounded corners to the render================#
    render_label_preview.place(x=((650-width_to_know_preview)/2), y=200)
#=========================================================#

def open_file():
    global file
    global im
    file = askopenfile(parent=home, mode='rb', title="Choose a file", filetypes=[("Fichiers image", "*.jpg *.jpeg *.png")])
    if file:
        im = Image.open (file)
        show_frame(gnb_frame) 
        image_render_gnb()                 

def save_file():
    im2_path = filedialog.asksaveasfile(initialdir="converted_images",
                                            defaultextension=".jpg",
                                            filetypes=[
                                                ("JPG",".jpg"),
                                                ("PNG",".png"),
                                                ("Tout fichier",""),

                                            ])
    im2.save(im2_path)
    show_frame(home) 

def greyscale():
    global im2
    global render_image
    global render_label
    im2 = Image.new('L', im.size)
    width, height = im.size
    for x in range(0,width):
        for y in range(0,height):
            r, g, b = im.getpixel((x,y))
            value = r + g + b / 3
            value = int(value)
            im2.putpixel((x, y), value)    
    show_frame(save_frame)          
    image_render_preview()  



def negative():
    width, height = im.size
    global im2
    im2 = Image.new(mode = "RGB", size = (width, height))
    for x in range(0,width):
        for y in range(0,height): 
            r, g, b = im.getpixel((x,y))
            rn = int(255 - r)
            gn = int(255 - g)
            bn = int(255 - b)
            im2.putpixel((x, y),(rn,gn,bn))
    show_frame(save_frame)  
    image_render_preview()

def black_white():
    global im2
    im2 = Image.new('1', im.size)
    width, height = im.size
    for x in range(0,width):
            for y in range(0,height):
                s = 127
                black = 255
                white = 0   
                r, g, b = im.getpixel((x,y))
                rn = int(r)
                gn = int(g)
                bn = int(b)
                if rn < s :
                    im2.putpixel( (x, y), white )
                else: 
                    im2.putpixel( (x, y), black )
                
                if gn < s :
                    im2.putpixel( (x, y), white )
                else: 
                    im2.putpixel( (x, y), black )

                if bn < s :
                    im2.putpixel( (x, y), white )
                else: 
                    im2.putpixel( (x, y), black )
    show_frame(save_frame)         
    image_render_preview()

home = tk.Frame(window,bg="#292d3e")
home.place(x=0,y=0,width=1920,height=1080)

gnb_frame = tk.Frame(window,bg="#292d3e")
gnb_frame.place(x=0,y=0,width=1920,height=1080)

save_frame = tk.Frame(window,bg="#292d3e")
save_frame.place(x=0,y=0,width=1920,height=1080)

instructions = tk.Label(home, text="Selectionnez une image sur votre ordinateur pour la convertir", font=("AtkinsonPolice", 13), fg="white", bg="#292d3e", border=0)
instructions.place(x=77.5,y=210)

instructions_save = tk.Label(save_frame, text="Aperçu de l'image convertie :", font=("AtkinsonPolice", 13), fg="white", bg="#292d3e", border=0)
instructions_save.place(x=206.5,y=170)



logo = Image.open("logo_i_like.png")
logo = logo.resize((198, 149))
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(home, image=logo, bg="#292d3e",)
logo_label.image = logo
logo_label.place(x=226, y=10)

logo_label2 = tk.Label(gnb_frame, image=logo, bg="#292d3e")
logo_label2.image = logo
logo_label2.place(x=226, y=10)

logo_label3 = tk.Label(save_frame, image=logo, bg="#292d3e")
logo_label3.image = logo
logo_label3.place(x=226, y=10)




#greyscale_btn = tk.Button(gnb_frame, text="Greyscale", command=lambda:greyscale(), font="AtkinsonPolice", bg="#0b8", fg="white")
#greyscale_btn.place(x=25,y=255,width=150,height=50)

#negative_btn = tk.Button(gnb_frame, text="Negative", command=lambda:negative(), font="AtkinsonPolice", bg="#0b8", fg="white") 
#negative_btn.place(x=225,y=255,width=150,height=60)

#black_white_btn = tk.Button(gnb_frame, text="Black & white", command=lambda:black_white(), font="AtkinsonPolice", bg="#0b8", fg="white")
#black_white_btn.place(x=425,y=255,width=150,height=50)

#save_btn = tk.Button(save_frame, text="Save", command=lambda:save_file(), font="AtkinsonPolice", bg="#0b8", fg="white") 
#save_btn.place(x=225,y=440,width=150,height=60)

#save_btn = tk.Button(save_frame, text="Save", command=lambda:save_file(), font="AtkinsonPolice", bg="#0b8", fg="white") 
#save_btn.place(x=225,y=440,width=150,height=60)

greyscale_btn = Image.open("nuances_de_gris_button.png")
greyscale_btn = ImageTk.PhotoImage(greyscale_btn)
greyscale_btn_label = tk.Button(gnb_frame, image=greyscale_btn, border=0, bg="#292d3e", activebackground="#292d3e", command=lambda:greyscale())
greyscale_btn_label.image = greyscale_btn
greyscale_btn_label.place(x=50,y=190)

negative_btn = Image.open("negatif_button.png")
negative_btn = ImageTk.PhotoImage(negative_btn)
negative_btn_label = tk.Button(gnb_frame, image=negative_btn, border=0, bg="#292d3e", activebackground="#292d3e", command=lambda:negative())
negative_btn_label.image = negative_btn
negative_btn_label.place(x=250,y=190)

black_white_btn = Image.open("noir&blanc_button.png")
black_white_btn = ImageTk.PhotoImage(black_white_btn)
black_white_btn_label = tk.Button(gnb_frame, image=black_white_btn, border=0, bg="#292d3e", activebackground="#292d3e", command=lambda:black_white())
black_white_btn_label.image = black_white_btn
black_white_btn_label.place(x=450,y=190)



save_btn = Image.open("save_button.png")
save_btn = save_btn.resize((500,87))
save_btn = ImageTk.PhotoImage(save_btn)
save_btn_label = tk.Button(save_frame, image=save_btn, width=500, height=87, border=0, bg="#292d3e", activebackground="#292d3e", command=lambda:save_file())
save_btn_label.image = save_btn
save_btn_label.place(x=75,y=440)


home_btn = Image.open("home_btn.png")
home_btn = ImageTk.PhotoImage(home_btn)
home_btn_label = tk.Button(gnb_frame, image=home_btn, width=50, height=50, border=0, bg="#292d3e", activebackground="#292d3e", command=lambda:show_frame(home))
home_btn_label.image = home_btn
home_btn_label.place(x=550,y=40)

home_btn = Image.open("home_btn.png")
home_btn = ImageTk.PhotoImage(home_btn)
home_btn_label = tk.Button(save_frame, image=home_btn, width=50, height=50, border=0, bg="#292d3e", activebackground="#292d3e", command=lambda:show_frame(home))
home_btn_label.image = home_btn
home_btn_label.place(x=550,y=40)



#=========================================#


browse_logo = Image.open("browse_logo.png")
browse_logo = ImageTk.PhotoImage(browse_logo)
browse_logo_label = tk.Button(home, image=browse_logo, border=0, bg="#292d3e", activebackground="#292d3e", command=lambda:open_file())
browse_logo_label.image = browse_logo
browse_logo_label.place(x=179.5, y=270)

#instructions_save.update()
#largeur_de_l_element = instructions_save.winfo_width()
#print(largeur_de_l_element)

show_frame(home)
 


#==============Tester image resize si pillow à trop de valeurs============#

window.mainloop()

