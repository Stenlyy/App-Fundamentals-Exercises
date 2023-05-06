from tkinter import *


def multiples_list():
    from app_fundamentals_exercises.list_basic import list_basic_task

    root = Tk()
    root.geometry("645x310")
    root.title("Multiples List")
    root.configure(bg="green")
    root.wm_maxsize(645, 310)

    def logic():
        import re

        result_box.config(state=NORMAL)
        result_box.delete("1.0", END)

        the_result = []
        if not number_entry.get():
            the_result = "Please add a number"

        elif not count_entry.get():
            the_result = "Please add a count"

        elif re.match(r'^-?\d+(?:\d+)?$', number_entry.get()) and re.match(r'^-?\d+(?:\d+)?$', count_entry.get()):

            number = int(number_entry.get())
            count = int(count_entry.get())
            for index in range(1, count + 1):
                the_result.append(number * index)
        else:
            the_result = "Please add just numbers"

        result_box.insert(END, str(the_result))

        number_entry.delete("0", END)
        count_entry.delete("0", END)

    # task
    text_box = Text(root, height=13, wrap=WORD)
    text_box.insert(INSERT, list_basic_task.multiples_list())
    text_box.place(x=0, y=0)
    text_box.config(state=DISABLED)

    # Input
    number_label = Label(root, text="Factor:", bg="green", fg="yellow")
    number_entry = Entry(root)
    number_label.place(x=0, y=220)
    number_entry.place(x=60, y=220)

    count_label = Label(root, text="Count:", bg="green", fg="yellow")
    count_entry = Entry(root)
    count_label.place(x=0, y=250)
    count_entry.place(x=60, y=250)

    # Confirm button
    confirm_button = Button(root, text="Confirm", command=logic)
    confirm_button.place(x=100, y=275)

    # Result box
    result_box = Text(root, height=1, width=40, state=DISABLED)
    result_box.place(x=300, y=250)

    root.mainloop()


multiples_list()
