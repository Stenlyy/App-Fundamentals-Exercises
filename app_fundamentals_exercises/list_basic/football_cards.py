from tkinter import *


def football_cards():
    from list_basic import list_basic_task
    root = Tk()
    root.geometry("724x455")
    root.title("Football Cards")
    root.configure(bg="green")
    root.wm_maxsize(724, 455)

    def logic():
        result_box.config(state=NORMAL)
        result_box.delete("1.0", END)

        team_a = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
        team_b = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']

        cards = cards_entry.get().split()
        result = ""
        if not all(card in team_a or card in team_b for card in cards):
            result = "Please add correct card!"

        else:
            game_was_terminated = False

            for card in cards:
                if card in team_a:
                    team_a.remove(card)
                elif card in team_b:
                    team_b.remove(card)
                if len(team_a) < 7 or len(team_b) < 7:
                    game_was_terminated = True
                    break

            result = f'Team A - {len(team_a)}; Team B - {len(team_b)}'

            if game_was_terminated:
                result +='\nGame was terminated'

        result_box.insert(INSERT, result)

        cards_entry.delete("0", END)

    # task
    text_box = Text(root, height=21, wrap=WORD,bg="orange")
    text_box.insert(INSERT, list_basic_task.football_cards())
    text_box.place(x=0, y=0)
    text_box.config(state=DISABLED, fg="black", font="bold")

    # input
    cards_label = Label(root, text="Cards:", bg="green", fg="white", font="bold")
    cards_entry = Entry(root)
    cards_label.place(x=0, y=400)
    cards_entry.place(x=54, y=400)

    # Confirm button
    confirm_button = Button(root, text="Confirm", command=logic)
    confirm_button.place(x=184, y=400)

    # Result box
    result_box = Text(root, height=2, width=40, state=DISABLED)
    result_box.place(x=275, y=400)
    root.mainloop()

football_cards()