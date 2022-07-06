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
  newWindow.title("Animal Adoption Page 2")
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

def openNewWindow2():

    global img7, img8, img9, img10, img11, img12, img13, img14, img15, img16, img17, img18, img19

    newWindow = tk.Toplevel(window)
    newWindow.title("Animal Adoption Page 3")
    newWindow.geometry("800x400")
    label1 = tk.Label(newWindow, text = "You selected:",fg = "black", bg = "beige", font = "bold",)
    label1.pack()

    if variable.get() == "Beagle":  
        
        canvas7 = tk.Canvas(newWindow, width = 216, height = 234)  
        canvas7.pack()  
        img7 = ImageTk.PhotoImage(Image.open(r"beagle.jpg")) 
        canvas7.create_image(20, 20, anchor=tk.NW, image=img7)

        labelbeagle1 = tk.Label(newWindow, text = """Beagles are active, curious dogs. 
        They are also hound dogs, so it's in their nature to roam. 
        Care must be taken to prevent them from wandering off into harm's way by 
        keeping them contained in a fenced-in yard or on a leash when outside of the house. 
        Beagles also are friendly little dogs. 
        Availability: 5""")
          
        labelbeagle1.pack() 

       
        if variable1.get() == "1-5":
            label4 = tk.Label(newWindow, text = "1-5 Beagle")
            label4.pack()
        
        elif variable1.get() == "5-10":
            label5 = tk.Label(newWindow, text = "5-10 Beagle")
            label5.pack()

        elif variable1.get() == "Senior":
            label6 = tk.Label(newWindow, text = "Senior Beagle")
            label6.pack()

    if variable.get() == "Pug":  
        
        canvas8 = tk.Canvas(newWindow, width = 290, height = 174)  
        canvas8.pack()  
        img8 = ImageTk.PhotoImage(Image.open(r"pug.jpg"))  
        canvas8.create_image(20, 20, anchor=tk.NW, image=img8)

        labelpug1 =tk.Label(newWindow, text = """The pug is an extremely popular breed with 
        a devoted fan base. That's because they're friendly, funny, 
        loyal, adorable, and relatively easy to care for — qualities 
        that also make the breed ideal for first-time dog owners. 
        Pugs, like all dogs, need to be walked regularly, 
        but apart from that they are not athletes. 
        Availability: 1""")
        labelpug1.pack()

        
        if variable1.get() == "1-5":
            label7 = tk.Label(newWindow, text = "1-5 Pug")
            label7.pack()
        
        elif variable1.get() == "5-10":
            label8 = tk.Label(newWindow, text = "5-10 Pug")
            label8.pack()

        elif variable1.get() == "Senior":
            label9 = tk.Label(newWindow, text = "Senior Pug")
            label9.pack()

    if variable.get() == "German Shepherd":  
        
        canvas9 = tk.Canvas(newWindow, width = 246, height = 205)  
        canvas9.pack()  
        img9 = ImageTk.PhotoImage(Image.open(r"german_shepherd.jpg"))  
        canvas9.create_image(20, 20, anchor=tk.NW, image=img9)

        labelgerman = tk.Label(newWindow, text = """The German shepherd dog is a herding breed 
        known for its courage, loyalty and guarding instincts. 
        This breed makes an excellent guard dog, police dog, military dog, 
        guide dog for the blind and search and rescue dog. For many families, 
        the German shepherd is also a treasured family pet. 
        Availability: 2""")        
        labelgerman.pack()

        
        if variable1.get() == "1-5":
            label10 = tk.Label(newWindow, text = "1-5 German Shepherd")
            label10.pack()
        
        elif variable1.get() == "5-10":
            label11 = tk.Label(newWindow, text = "5-10 German Shepherd")
            label11.pack()

        elif variable1.get() == "Senior":
            label12 = tk.Label(newWindow, text = "Senior German Shepherd")
            label12.pack()


    if variable.get() == "Labrador":  
        
        canvas10 = tk.Canvas(newWindow, width = 275, height = 183)  
        canvas10.pack()  
        img10 = ImageTk.PhotoImage(Image.open(r"labrodor.jpg"))  
        canvas10.create_image(20, 20, anchor=tk.NW, image=img10)

        labellabrador = tk.Label(newWindow, text = """The Labrador Retriever breed is outgoing, 
        friendly and enthusiastic. Labradors have a medium sized physique, 
        short coat, floppy ears and soulful eyes. They are a gentle clever 
        breed that need attention, training and love. They make great pets, show dogs, 
        and working, hunting, therapy and service partners. 
        Availability: 4""")
        labellabrador.pack()

        
        if variable1.get() == "1-5":
            label13 = tk.Label(newWindow, text = "1-5 Labrador")
            label13.pack()
        
        elif variable1.get() == "5-10":
            label14 = tk.Label(newWindow, text = "5-10 Labrador")
            label14.pack()

        elif variable1.get() == "Senior":
            label15 = tk.Label(newWindow, text = "Senior Labrador")
            label15.pack()
    

    if variable.get() == "Persian":  
        
        canvas11 = tk.Canvas(newWindow, width = 225, height = 225)  
        canvas11.pack()  
        img11 = ImageTk.PhotoImage(Image.open(r"persian.jpg"))
        canvas11.create_image(20, 20, anchor=tk.NW, image=img11) 

        labelpersian = tk.Label(newWindow, text = """The dignified and docile Persian cat is known 
        for being quiet and sweet. 
        Availability: 2""")
        labelpersian.pack() 

        
        if variable1.get() == "1-5":
            label16 = tk.Label(newWindow, text = "1-5 Persian")
            label16.pack()
        
        elif variable1.get() == "5-10":
            label17 = tk.Label(newWindow, text = "5-10 Persian")
            label17.pack()

        elif variable1.get() == "Senior":
            label8 = tk.Label(newWindow, text = "Senior Persian")
            label8.pack()

    if variable.get() == "Siamese":  
        
        canvas12 = tk.Canvas(newWindow, width = 183, height = 275)  
        canvas12.pack()  
        img12 = ImageTk.PhotoImage(Image.open(r"siamese.jpg"))
        canvas12.create_image(20, 20, anchor=tk.NW, image=img12)  

        labelsiamese = tk.Label(newWindow, text = """Siamese cats are almost as famous for their personality 
        as they are for their looks. They are among the most vocal of cats, 
        enjoying long 'conversations' with their human friends. 
        They are loving, loyal and crave human companionship, 
        making them excellent family pets. 
        Availability: 1""")
        labelsiamese.pack()

        
        if variable1.get() == "1-5":
            label9 = tk.Label(newWindow, text = "1-5 Siamese")
            label9.pack()
        
        elif variable1.get() == "5-10":
            label20 = tk.Label(newWindow, text = "5-10 Siamese")
            label20.pack()

        elif variable1.get() == "Senior":
            label21 = tk.Label(newWindow, text = "Senior Siamese")
            label21.pack()

    if variable.get() == "Maine Coon":  
        
        canvas13 = tk.Canvas(newWindow, width = 225, height = 225)  
        canvas13.pack()  
        img13 = ImageTk.PhotoImage(Image.open(r"maine coon.jpg")) 
        canvas13.create_image(20, 20, anchor=tk.NW, image=img13)

        labelmaine = tk.Label(newWindow, text = """Sometimes weighing up to 25 pounds, the Maine Coon 
        is considered one of the largest domestic cat breeds. 
        Nevertheless, they are good natured and gentle. They thrive in 
        families with children and other pets, even dogs. Additionally, they are 
        known to be very tolerant and can easily adapt to the needs of children. 
        Availability: 2""")
        labelmaine.pack()  

        
        if variable1.get() == "1-5":
            label22 = tk.Label(newWindow, text = "1-5 Maine Coon")
            label22.pack()
        
        elif variable1.get() == "5-10":
            label23 = tk.Label(newWindow, text = "5-10 Maine Coon")
            label23.pack()

        elif variable1.get() == "Senior":
            label24 = tk.Label(newWindow, text = "Senior Maine Coon")
            label24.pack()


    if variable.get() == "Siberian":  
        
        canvas14 = tk.Canvas(newWindow, width = 300, height = 168)  
        canvas14.pack()  
        img14 = ImageTk.PhotoImage(Image.open(r"siberian.jpg"))  
        canvas14.create_image(20, 20, anchor=tk.NW, image=img14)

        labelsiberian = tk.Label(newWindow, text = """ Affection-wise, they are devoted but not clingy. 
        Siberians will follow you from room to room but patiently wait until you have time for cuddles. 
        They don't mind noises or strangers as much as most cats, and if introduced properly, 
        they are happy to cohabitate with kids, dogs, and whoever else may live in your home. 
        Availability: 1""")
        labelsiberian.pack()

        if variable1.get() == "1-5":
            label25 = tk.Label(newWindow, text = "1-5 Siberian")
            label25.pack()
        
        elif variable1.get() == "5-10":
            label26 = tk.Label(newWindow, text = "5-10 Siberian")
            label26.pack()

        elif variable1.get() == "Senior":
            label27 = tk.Label(newWindow, text = "Senior Siberian")
            label27.pack()

    if variable.get() == "White":  
        
        canvas15 = tk.Canvas(newWindow, width = 238, height = 212)  
        canvas15.pack()  
        img15 = ImageTk.PhotoImage(Image.open(r"white.jpg"))  
        canvas15.create_image(20, 20, anchor=tk.NW, image=img15)

        labelwhite = tk.Label(newWindow, text =""" Rabbits make great pets. In general rabbits 
        need appropriate housing, exercise, socialisation 
        and a specific diet for good welfare. Some breeds of rabbits, 
        particularly the longer haired rabbits, may require daily grooming. 
        Availability: 3""")
        labelwhite.pack()

    if variable.get() == "Black":  
        
        canvas16 = tk.Canvas(newWindow, width = 280, height = 180)  
        canvas16.pack()  
        img16 = ImageTk.PhotoImage(Image.open(r"black.jpg"))  
        canvas16.create_image(20, 20, anchor=tk.NW, image=img16)

        labelblack = tk.Label(newWindow, text ="""The black rabbits are merely a rare 'freak' of nature. 
        Black wild rabbits are completely natural and are what's 
        described as being melanistic. This occurs when there is an over 
        development of the melanin gene which leads to the dark colour. 
        Availability: 0""")
        labelblack.pack()

    if variable.get() == "Brown":  
        
        canvas17 = tk.Canvas(newWindow, width = 264, height = 191)  
        canvas17.pack()  
        img17 = ImageTk.PhotoImage(Image.open(r"brown.jpg"))  
        canvas17.create_image(20, 20, anchor=tk.NW, image=img17)

        labelbrown = tk.Label(newWindow, text ="""Rabbits require safe, gentle handling 
        and a quiet environment. As prey animals, rabbits can be easily 
        startled and stressed by the loud noises and fast. 
        Availability: 2""")
        labelbrown.pack()
    
    if variable.get() == "Parrot":  
        
        canvas18 = tk.Canvas(newWindow)  
        canvas18.pack()  
        img18 = ImageTk.PhotoImage(Image.open(r"parrot1.jpg"))  
        canvas18.create_image(20, 20, anchor=tk.NW, image=img18)

        labelparrot = tk.Label(newWindow, text ="""They are colorful, quite intelligent, highly 
        sociable, and long-lived creatures. Different parrot species vary 
        largely in characteristics such as color, weight, and habits. 
        There are close to 400 parrot species around the globe, but sadly, many of 
        them have become endangered. 
        Availability: 5""")
        labelparrot.pack()
        
    if variable.get() == "Love birds":  
        
        canvas19 = tk.Canvas(newWindow)  
        canvas19.pack()  
        img19 = ImageTk.PhotoImage(Image.open(r"lovebords1.jpg"))  
        canvas19.create_image(20, 20, anchor=tk.NW, image=img19)

        labellovebird = tk.Label(newWindow, text ="""Lovebirds need a safe, securely locked habitat, 
        a nutritionally complete pelleted diet, fresh water daily, 
        toys and other stimulation in their habitat, and daily interaction 
        and handling. They also need a bowl to bathe in or a mister to be sprayed with, as well 
        as regular veterinary checkups to help them stay healthy. 
        Availability: 3""")
        labellovebird.pack()


window.mainloop()
