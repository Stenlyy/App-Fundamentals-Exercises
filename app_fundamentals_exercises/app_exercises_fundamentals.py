from tkinter import *

def invert_values():
    import invert_values
    invert_values.invert_values()


root = Tk()

# Background

root.geometry("610x315")
root.title("SoftUni Fundamentals")
root.wm_maxsize(610, 315)
canvas = Canvas(root, width=600, height=800)
background_img = PhotoImage(file="background.png")
canvas.create_image(0, 0, anchor=NW, image=background_img)
canvas.pack()

# Menu
menu = Menu(root)
menu.config(font=17)
root.config(menu=menu)


# List Basic Menu
list_basic_menu = Menu(menu, tearoff=False)
list_basic_menu.config()
menu.add_cascade(label="List Basic", menu=list_basic_menu)

list_basic_exercises = Menu(list_basic_menu, tearoff=False)
list_basic_more_exercises = Menu(list_basic_menu, tearoff=False)
list_basic_menu.add_cascade(label="List Basic - Exercises", menu=list_basic_exercises)
list_basic_menu.add_cascade(label="List basic - More Exercises", menu=list_basic_more_exercises)
list_basic_exercises.add_command(label="Invert Values", command=invert_values)

# Function Menu
function = Menu(menu, tearoff=False)
function.config()
menu.add_cascade(label="Function", menu=function)
function_exercises = Menu(function, tearoff=False)
function_more_exercises = Menu(function, tearoff=False)
function.add_cascade(label="Function - Exercises", menu=function_exercises)
function.add_cascade(label="Function - More Exercises", menu=function_more_exercises)

#List Advanced Menu
list_advanced = Menu(menu, tearoff=False)
list_advanced.config()
menu.add_cascade(label="List Advanced", menu=list_advanced)
list_advanced_exercises = Menu(list_advanced, tearoff=False)
list_advanced_more_exercises = Menu(list_advanced, tearoff=False)
list_advanced.add_cascade(label="List Advanced - Exercises", menu=list_advanced_exercises)
list_advanced.add_cascade(label="List Advanced - More Exercises", menu=list_advanced_more_exercises)

#Objects and classes Menu
objects_and_classes = Menu(menu, tearoff=False)
objects_and_classes.config()
menu.add_cascade(label="Objects and Classes", menu=objects_and_classes)
objects_and_classes_lab = Menu(objects_and_classes, tearoff=False)
objects_and_classes_exercises = Menu(objects_and_classes, tearoff=False)
objects_and_classes.add_cascade(label="Object and Classes - Lab", menu=objects_and_classes_lab)
objects_and_classes.add_cascade(label="LObject and Classes - Exercises", menu=objects_and_classes_exercises)

#Dictionaries Menu
dictionaries = Menu(menu, tearoff=False)
dictionaries.config()
menu.add_cascade(label="Function", menu=dictionaries)
dictionaries_exercises = Menu(dictionaries, tearoff=False)
dictionaries_more_exercises = Menu(dictionaries, tearoff=False)
dictionaries.add_cascade(label="Dictionaries - Exercises", menu=dictionaries_exercises)
dictionaries.add_cascade(label="Dictionaries - More Exercises", menu=dictionaries_more_exercises)

# Text Processing Menu
text_processing = Menu(menu, tearoff=False)
text_processing.config()
menu.add_cascade(label="Text processing", menu=text_processing)
text_processing_exercises = Menu(text_processing, tearoff=False)
text_processing_more_exercises = Menu(text_processing, tearoff=False)
text_processing.add_cascade(label="Text Processing - Exercises", menu=text_processing_exercises)
text_processing.add_cascade(label="Text Processing - More Exercises", menu=text_processing_more_exercises)

# Regular Expressions Menu
regular_expressions = Menu(menu, tearoff=False)
regular_expressions.config()
menu.add_cascade(label="Regular Expressions", menu=regular_expressions)
regular_expressions_exercises = Menu(regular_expressions, tearoff=False)
regular_expressions_more_exercises = Menu(regular_expressions, tearoff=False)
regular_expressions.add_cascade(label="Regular Expressions - Exercises", menu=regular_expressions_exercises)
regular_expressions.add_cascade(label="Regular Expressions - More Exercises", menu=regular_expressions_more_exercises)


root.mainloop()