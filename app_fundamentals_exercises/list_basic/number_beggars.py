from tkinter import *


def number_beggars():
    import list_basic.list_basic_task

    root = Tk()
    root.geometry("645x285")
    root.title("Number beggars")
    root.configure(bg="purple")
    root.wm_maxsize(645, 285)

    def logic():
        import re

        result_box.config(state=NORMAL)
        result_box.delete("1.0", END)

        all_are_numbers = True
        money_in_string = numbers_entry.get().split(', ')
        beggars = count_of_beggars_entry.get()
        counter_beggars = 0

        the_result = []
        money_in_int = []

        for index in range(len(money_in_string)):
            if money_in_string[index].isdigit():
                money_in_int.append(int(money_in_string[index]))
            else:
                all_are_numbers = False

        if not beggars.isdigit():
            all_are_numbers = False

        if all_are_numbers:
            beggars = int(beggars)

            while counter_beggars < beggars:
                sum_for_beggar = 0
                for money in range(counter_beggars, len(money_in_int), beggars):
                    sum_for_beggar += money_in_int[money]
                the_result.append(sum_for_beggar)
                counter_beggars += 1

        else:
            the_result = "Please add just numbers"

        result_box.insert(INSERT, str(the_result))

        numbers_entry.delete("0", END)
        count_of_beggars_entry.delete("0", END)

    # Task
    text_box = Text(root, height=13, wrap=WORD)
    text_box.insert(INSERT, list_basic.list_basic_task.number_beggars())
    text_box.place(x=0, y=0)
    text_box.config(state=DISABLED)

    # input
    numbers_label = Label(root, text="Numbers:", bg="purple", fg="white", font="bold")
    numbers_entry = Entry(root)
    numbers_label.place(x=0, y=220)
    numbers_entry.place(x=77, y=223)

    count_of_beggars_label = Label(root, text="Count of beggars:", bg="purple", fg="white", font="bold")
    count_of_beggars_entry = Entry(root)
    count_of_beggars_label.place(x=0, y=240)
    count_of_beggars_entry.place(x=130, y=243)

    # confirm button

    confirm_button = Button(root, text="Confirm", command=logic)
    confirm_button.place(x=261, y=242)

    # Result box
    result_box = Text(root, height=1, width=30, state=DISABLED)
    result_box.place(x=370, y=242)

    root.mainloop()


number_beggars()
