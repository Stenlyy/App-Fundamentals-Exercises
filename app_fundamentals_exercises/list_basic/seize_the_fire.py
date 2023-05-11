from tkinter import *


def seize_the_fire():
    from list_basic import list_basic_task

    root = Tk()
    root.geometry("900x700")
    root.title("Seize the fire")
    root.configure(bg="#F9EE40")
    root.wm_maxsize(900, 700)

    def logic():
        result_box.config(state=NORMAL)
        result_box.delete("1.0", END)
        result = ""
        LOW, MEDIUM, HIGH = range(1, 51), range(51, 81), range(81, 126)

        type_of_fire = fire_entry.get().split("#")
        water = water_entry.get()
        if not water.isdigit():
            result = "Water should a number to be"
        else:
            effort = 0
            total = 0
            water = int(water)
            result = 'Cells:'
            flag = True
            for fire in range(len(type_of_fire)):
                the_fire = type_of_fire[fire].split(' = ')
                if len(the_fire) != 2:
                    result = "Your fire is invalid, please add a valid fire. \nExample:\nHigh = 89"
                    flag = False
                    break
                type_fire = the_fire[0]
                the_water = the_fire[1]
                if not the_water.isdigit():
                    result = "Your fire is invalid, please add a valid fire. \nExample:\nHigh = 89"
                    flag = False
                    break

                the_water = int(the_water)

                if water < the_water:
                    continue
                if type_fire == 'Low' and the_water in LOW:
                    water -= the_water
                    effort += the_water * 0.25
                elif type_fire == 'Medium' and the_water in MEDIUM:
                    water -= the_water
                    effort += the_water * 0.25
                elif type_fire == 'High' and the_water in HIGH:
                    water -= the_water
                    effort += the_water * 0.25
                else:
                    continue
                total += the_water

                result += f'\n - {the_water}'
            if flag:
                result += f'\nEffort: {effort:.2f}\nTotal Fire: {total}'

        result_box.insert(INSERT, result)
        water_entry.delete("0", END)
        fire_entry.delete("0", END)

    # task
    text_box = Text(root, height=25, width=100, wrap=WORD, font="bold", bg="#F00F0F", fg="#F9D140")
    text_box.insert(INSERT, list_basic_task.seize_the_fire())
    text_box.place(x=0, y=0)
    text_box.config(state=DISABLED)

    # Input
    fire_label = Label(root, text="Fire:", bg="#F9EE40", fg="#F00F0F", font="bold")
    fire_entry = Entry(root, width=50)
    water_label = Label(root, text="Water:", fg="#F00F0F", bg="#F9EE40", font="bold")
    water_entry = Entry(root)
    fire_label.place(x=0, y=470)
    fire_entry.place(x=50, y=470)
    water_label.place(x=0, y=500)
    water_entry.place(x=60, y=500)

    # button

    button = Button(root, text="Confirm", command=logic)
    button.place(x=200, y=497)

    # result box

    result_box = Text(root, height=12, width=20, state=DISABLED)
    result_box.place(x=600, y=470)

    root.mainloop()


seize_the_fire()
