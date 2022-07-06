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

  global img1
  newWindow = tk.Toplevel(window)
  newWindow.title("New page")
  newWindow.geometry("700x400")
  label1 = tk.Label(newWindow, text = "Trial",fg = "black", bg = "beige", font = "bold",)
  label1.pack()
  if variable.get() == "Beagle" and variable1.get() == "Senior":
    label4 = tk.Label(newWindow, text = "Senior Beagle")
    label4.pack()
    canvas1 = tk.Canvas(newWindow,width = 300, height = 300)  
    canvas1.pack()  
    img1= ImageTk.PhotoImage(Image.open(r"c:\Users\navne\Desktop\Python\cute.jpg"))  
    canvas1.create_image(20, 20, anchor=tk.NW, image=img1) 



button = tk.Button(window, text="Click me", command=openNewWindow)
button.pack(side=tk.BOTTOM)


window.mainloop()
