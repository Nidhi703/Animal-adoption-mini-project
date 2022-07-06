import tkinter as tk
from PIL import ImageTk,Image 
window = tk.Tk()
window.title("Animal Adoption") 

canvas = tk.Canvas(window, width = 300, height = 300)  
canvas.pack()  
img = ImageTk.PhotoImage(Image.open(r"c:\Users\navne\Desktop\Python\cute.jpg"))  

canvas.create_image(20, 20, anchor=tk.NW, image=img) 

label = tk.Label(window, text = "Welcome! Please pick what kind of animal you are looking for:",fg = "black", bg = "beige", font = "bold",)
label.pack()
label2 = tk.Label(window, text = "breed")
label2.pack()
OptionList = [
"Beagle",
"Pug",
"German Shepherd",
"Labrador"
] 
variable = tk.StringVar(window)
variable.set(OptionList[0])

opt = tk.OptionMenu(window, variable, *OptionList)
opt.config(width=90, font=('Helvetica', 12))
opt.pack()
    

label3 =tk.Label(window, text = "Age")
label3.pack()
OptionList1 = [
"1-5",
"5-10",
"Senior",
] 

variable1 = tk.StringVar(window)
variable1.set(OptionList1[0])

opt1 = tk.OptionMenu(window, variable1, *OptionList1)
opt1.config(width=90, font=('Helvetica', 12))
opt1.pack()

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
