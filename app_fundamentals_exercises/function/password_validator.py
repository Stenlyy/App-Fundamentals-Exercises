from tkinter import *

def password_validator():
    from app_fundamentals_exercises.function import function_task
    root = Tk()
    root.geometry("600x520")
    root.title("Password Validator")
    root.configure(bg="#26F286")
    root.wm_maxsize(600,520)

    def logic():
        result_box.config(state=NORMAL)
        result_box.delete("1.0", END)
        received_password = password_entry.get()
        result = []
        password_is_valid = True
        digit_counter = 0
        for character in received_password:
            if character.isdigit():
                digit_counter += 1

        if not 6 <= len(received_password) <= 10:
            result.append('Password must be between 6 and 10 characters')
            password_is_valid = False
        if not received_password.isalnum():
            result.append('Password must consist only of letters and digits')
            password_is_valid = False
        if not digit_counter >= 2:
            result.append('Password must have at least 2 digits')
            password_is_valid = False

        if password_is_valid:
            result_box.insert(INSERT,'Password is valid')
        else:
            result_box.insert(INSERT,'\n'.join(result))

        password_entry.delete("0", END)

    # task
    text_box = Text(root, height=23, wrap=WORD, bg="#889A90")
    text_box.insert(INSERT, function_task.password_validator())
    text_box.place(x=0, y=0)
    text_box.config(state=DISABLED, fg="#FDF973", font="bold")

    # input
    password_label = Label(root, text="Password:", bg="#26F286", fg="black", font="bold")
    password_entry = Entry(root)
    password_label.place(x=0, y=430)
    password_entry.place(x=80, y=433)

    # confirm button
    confirm_button = Button(root, text="Confirm", command=logic)
    confirm_button.place(x=210, y=431)

    # result box
    result_box = Text(root, height=4, width=37, state=DISABLED)
    result_box.place(x=290, y=433)

    root.mainloop()

password_validator()