from tkinter import *
def invert_values():

    from app_fundamentals_exercises.list_basic import list_basic_task

    root = Tk()
    root.geometry("645x200")
    root.title("Invert Values")
    root.configure(bg="#E4CD5B")
    root.wm_maxsize(645, 200)

    def get_input_value():

        result_box.config(state=NORMAL)
        result_box.delete("1.0", END)

        import re
        number_in_string = input_entry.get().split()
        the_opposite_number = []

        for index in range(len(number_in_string)):
            if re.match(r'^-?\d+(?:\d+)?$', number_in_string[index]):
                opposite_number = -int(number_in_string[index])
                the_opposite_number.append(opposite_number)
            else:
                the_opposite_number = "Please add just numbers"
                break

        result_box.insert(END, str(the_opposite_number))

        input_entry.delete("0",END)

    # task

    text_box = Text(root,  height=9, wrap=WORD)

    text_box.insert(INSERT, list_basic_task.invert_values())
    text_box.place(x=0, y=0)
    text_box.config(state=DISABLED)

    # input
    input_label = Label(root, text="Add your Input:", bg="#E4CD5B")
    input_entry = Entry(root)
    input_label.place(x=0, y= 160)
    input_entry.place(x=90, y= 160)

    # Confirm button
    confirm_button = Button(root, text="Confirm", command=get_input_value)
    confirm_button.place(x=220, y= 160)


    result_box = Text(root, height=1, width=30, state=DISABLED)
    result_box.place(x= 300, y=160)




    root.mainloop()

invert_values()