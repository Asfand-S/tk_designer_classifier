with open("gui.py", "r") as f:
    string = f.read()

# --------------------PART 1 - MAKING CLASS STRUCTURE--------------------
# MAKING CLASS, CORRECTING INDENTATION, JOINING VARIABLES TO CLASS (self. thing) and other trivial things
step1 = string.replace("\n    ", " ")
step2 = step1.replace("\n)", ")")
step3 = step2.replace(".0", "")
step4 = step3.replace("window", "self.window")
step5 = step4.replace("canvas", "self.canvas")
step6 = step5.replace("\nentry", "\nself.entry")
step7 = step6.replace("\nimage_", "\nself.image_")
step8 = step7.replace("image=entry", "image=self.entry")
step9 = step8.replace("image=image", "image=self.image")
step10 = step9.replace("button_image", "self.button_image")
step11 = step10.replace("\nbutton_", "\nself.button_")
step12 = step11.replace("\nself", "\n        self")

step13 = step12.replace("        self.window", "class GUI:\n    def __init__(self):\n        self.window", 1)
step14 = step13.replace("mainloop()\n", "mainloop()\n\n\nobj = GUI()\n")
step15 = step14.replace("/home/asfand/Fiverr/WORK/build", ".") # This is my directory in kali, change it to suit your file location
step16 = step15.replace("bd=0", "bd=1")
step17 = step16.replace("( ", "(")

with open("gui_classed.py", "w") as a:
    a.write(step17)

# --------------------PART 2 - MAKING ARRAY OF BUTTONS--------------------
# # MAKING ARRAY OF BUTTONS (useful for Asfand)
with open("gui_classed.py", "r") as fp:
    string = fp.read()

# LOOP TO FIND NUMBER OF BUTTONS IN FILE
for i in range(1, 20):
    txt = "button_" + str(i)
    if txt not in string:
        x=i
        break

# LOOP TO CHANGE NAMES OF BUTTONS TO NEWLY DEFINED ARRAY buttons
for i in range(1, x):
    prev = "button_" + str(i)
    curr = "buttons[" + str(i) + "]"
    string = string.replace("button_" + str(i), "buttons[" + str(i) + "]")

# LOOP TO CHANGE NAMES OF IMAGE FILES BACK TO ORIGINAL WHICH WERE EDITED BY PREVIOUS LOOP 
# (Unwanted edits to image name, because by default, name of button and image is same)
for i in range(1, x): 
    prev = "buttons[" + str(i) + "].png"
    curr = "button_" + str(i) + ".png"    
    string = string.replace(prev, curr)

# LOOP TO CHANGE NAMES OF BUTTONS IMAGES TO NEWLY DEFINED ARRAY button_images
for i in range(1, x):
    prev = "button_image_" + str(i)
    curr = "button_images[" + str(i) + "]"
    string = string.replace(prev, curr)

for i in range(0, 10):
    prev = "[1]" + str(i)
    curr = "[1" + str(i) + "]"
    string = string.replace(prev, curr)

for i in range(10, x):
    prev = "buttons[" + str(i) + "]" + ".png"
    curr = "button_" + str(i) + ".png"
    string = string.replace(prev, curr)

# DECLARE ARRAYS buttons and button_images (same size as number of buttons)
step18 = string.replace("self.button", "self.buttons = [Button] * " + str(x) + "\n        self.button_images = [PhotoImage] * " + str(x) + "\n\n        self.button", 1)

with open("gui_classed.py", "w") as a:
    a.write(step18)

# --------------------PART 3 - REMOVING ENTRY IMAGES--------------------
# REMOVING ENTRY IMAGES
with open("gui_classed.py", "r") as fp:
    lines = fp.readlines()

with open("gui_classed.py", "w") as fp:
    for line in lines:
        if "entry_image" not in line.strip("\n"):
            fp.write(line)

# --------------------PART 3 - MAKING ENTRY VARIABLES--------------------
# READING FILE
with open("gui_classed.py", "r") as fp:
    string = fp.read()

# LOOP TO FIND NUMBER OF ENTRIES IN FILE AND THEIR NAMES
var_names = []
for i in range(1, 20):
    txt = "entry_" + str(i)
    if txt not in string:
        x=i
        break
    a = string.find(txt)
    string2 = string[a:]

    b = string2.find('text="') + 6
    string3 = string2[b:]
    c = string3.find('"')

    var_name = string3[0:c]
    var_name = var_name.replace(' ', '_')
    var_name = var_name.lower()
    var_names.append(var_name)

# LOOP TO MAKE ENTRY VARIABLES FOR ALL ENTRIES
for i in range(1, x):
    prev = "self.entry_" + str(i) + " = Entry("
    var_name = "self." + var_names[i-1]
    curr = var_name + " = StringVar()\n        " + prev + "textvariable=" + var_name + ", "
    string = string.replace(prev, curr, 1)

string = string.replace("from tkinter import ", "from tkinter import StringVar, ")
string = string.replace("Text, ", "", 1)

# WRITING CHANGES TO FILE
with open("gui_classed.py", "w") as fp:
    fp.write(string)



