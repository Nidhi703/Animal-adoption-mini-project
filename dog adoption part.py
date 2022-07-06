import tkinter as tk
from PIL import ImageTk,Image 
window = tk.Tk()
window.configure(bg = "light blue")
window.title("Animal Adoption") 

canvas = tk.Canvas(window, width = 301, height = 167)  
canvas.pack()  
img = ImageTk.PhotoImage(Image.open(r"adoptme.jpg"))  

canvas.create_image(1, 1, anchor=tk.NW, image=img) 

canvas1 = tk.Canvas(window, width = 225, height = 224)  
canvas1.pack()  
img1 = ImageTk.PhotoImage(Image.open(r"animals.jpg"))  

canvas1.create_image(1,1, anchor=tk.NW,image=img1) 

label = tk.Label(window, text = "Welcome! Please pick what kind of animal you are looking for:",fg = "Red", bg = "light pink", font = "bold",)
label.pack()

OptionList2 = [
"Dog",
"Cat",
"Rabbit",
"Bird"
] 
variable2 = tk.StringVar(window)
variable2.set(OptionList2[0])

opt = tk.OptionMenu(window, variable2, *OptionList2)
opt.config(width=90, font=('Helvetica', 12))
opt.pack()

def openNewWindow():
  global img2, img2, img3, img4, img5, img6
  global variable 
  global variable1
  global newWindow

  newWindow = tk.Toplevel(window)
  newWindow.title("Next")
  newWindow.configure(bg = "light yellow")
  newWindow.geometry("700x400")
  
  tk.Button(newWindow,text="CLICK ME", command=openNewWindow2).pack(side=tk.BOTTOM)



  if variable2.get() == "Dog":
    label2 = tk.Label(newWindow, text = "Breed",font = 15)
    label2.pack()
    OptionList = [
    "Beagle",
    "Pug",
    "German Shepherd",
    "Labrador"
    ] 
    variable = tk.StringVar(window)
    variable.set(OptionList[0])

    opt = tk.OptionMenu(newWindow, variable, *OptionList)
    opt.config(width=90, font=('Helvetica', 12))
    opt.pack()

    label3 =tk.Label(newWindow, text = "Age", font = 15)
    label3.pack()
    OptionList1 = [
    "1-5",
    "5-10",
    "Senior",
    ] 

    variable1 = tk.StringVar(newWindow)
    variable1.set(OptionList1[0])

    opt1 = tk.OptionMenu(newWindow, variable1, *OptionList1)
    opt1.config(width=90, font=('Helvetica', 12))
    opt1.pack()

    canvas2 = tk.Canvas(newWindow, width = 221, height = 228)  
    canvas2.pack()  
    img2 = ImageTk.PhotoImage(Image.open(r"download (2).jpg"))  

    canvas2.create_image(1,1, anchor=tk.NW,image=img2) 



  if variable2.get() == "Cat":
    label4 = tk.Label(newWindow, text = "Breed",font = 15)
    label4.pack()
    OptionList2 = [
    "Persian",
    "Siamese",
    "Maine Coon",
    "Siberian"
    ] 
    variable = tk.StringVar(window)
    variable.set(OptionList2[0])

    opt = tk.OptionMenu(newWindow, variable, *OptionList2)
    opt.config(width=90, font=('Helvetica', 12))
    opt.pack()

    label5 =tk.Label(newWindow, text = "Age", font = 15)
    label5.pack()
    OptionList3 = [
    "1-5",
    "5-10",
    "Senior",
    ] 

    variable1 = tk.StringVar(newWindow)
    variable1.set(OptionList3[0])

    opt1 = tk.OptionMenu(newWindow, variable1, *OptionList3)
    opt1.config(width=90, font=('Helvetica', 12))
    opt1.pack()

    canvas3 = tk.Canvas(newWindow, width = 275, height = 183)  
    canvas3.pack()  
    img3 = ImageTk.PhotoImage(Image.open(r"cat.jpg")) 
    canvas3.create_image(1,1, anchor=tk.NW,image=img3)
  

  if variable2.get() == "Rabbit":
    label6 = tk.Label(newWindow, text = "Color",font = 15)
    label6.pack()
    OptionList4 = [
    "White",
    "Black",
    "Brown"
    ] 
    variable = tk.StringVar(window)
    variable.set(OptionList4[0])

    opt = tk.OptionMenu(newWindow, variable, *OptionList4)
    opt.config(width=90, font=('Helvetica', 12))
    opt.pack()


    canvas4 = tk.Canvas(newWindow, width = 225, height = 225)  
    canvas4.pack()  
    img4 = ImageTk.PhotoImage(Image.open(r"rabbit.jpg"))  

    canvas4.create_image(1,1, anchor=tk.NW,image=img4) 


  if variable2.get() == "Bird":
    label7 = tk.Label(newWindow, text = "Which bird?",font = 15)
    label7.pack()
    OptionList5 = [
    "Parrot",
    "Love birds"
    ] 
    variable = tk.StringVar(window)
    variable.set(OptionList5[0])

    opt = tk.OptionMenu(newWindow, variable, *OptionList5)
    opt.config(width=90, font=('Helvetica', 12))
    opt.pack()

    canvas5 = tk.Canvas(newWindow, width = 300, height = 168)  
    canvas5.pack()  
    img5 = ImageTk.PhotoImage(Image.open(r"parrot.jpg"))  

    canvas5.create_image(1,1, anchor=tk.NW,image=img5) 

    canvas6 = tk.Canvas(newWindow, width = 300, height = 168)  
    canvas6.pack()  
    img6 = ImageTk.PhotoImage(Image.open(r"lovebirds.jpg"))  

    canvas6.create_image(1,1, anchor=tk.NW,image=img6) 


    

    
button = tk.Button(window, text="Next", command=openNewWindow)
button.pack(side=tk.BOTTOM)



window.mainloop()
