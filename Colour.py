from tkinter import *
from random import *
from tkinter import messagebox
import time

COLOUR_WORD = ['DRE', 'OELLYW', 'LBEU', 'ERGNE', 'OREAGN', 'RPEULP', 'EMIL', 'ORWBN', 'NYAV', 'PNIK', 'LDGO', 'VRLSEI',
               'BLKAC', 'HTWIE', ]

COLOUR_ANSWER = ['RED', 'YELLOW', 'BLUE', 'GREEN', 'ORANGE', 'PURPLE', 'LIME', 'BROWN', 'NAVY', 'PINK', 'GOLD',
                 'SILVER', 'BLACK', 'WHITE', ]


ran_num = randrange(0, (len(COLOUR_WORD)))
jumbled_rand_word = COLOUR_WORD[ran_num]

points = 0


def main():
    def back():
        my_window.destroy()
        from Project import start_main_page
        start_main_page()

    def change():
        global ran_num
        ran_num = randrange(0, (len(COLOUR_WORD)))
        word.configure(text=COLOUR_WORD[ran_num])
        get_input.delete(0, END)
        ans_lab.configure(text="")

    def check_submit():
        global points, ran_num
        user_word = get_input.get().upper()
        if user_word == COLOUR_ANSWER[ran_num]:
            points += 5
            score.configure(text="Score:- " + str(points))
            messagebox.showinfo('correct', "Correct Answer.. Wooohhooo!")
            ran_num = randrange(0, (len(COLOUR_WORD)))
            word.configure(text=COLOUR_WORD[ran_num])
            get_input.delete(0, END)
            ans_lab.configure(text="")
        else:
            messagebox.showerror("Error", "Inorrect Answer..Try your best!")
            get_input.delete(0, END)

    def show_answer():
        global points
        if points > 4:
            points -= 5
            score.configure(text="Score:- " + str(points))
            time.sleep(0.5)
            ans_lab.configure(text=COLOUR_ANSWER[ran_num])
        else:
            ans_lab.configure(text='Not enough points')

    my_window = Tk()
    my_window.geometry("500x500+500+150")
    my_window.resizable(0, 0)
    my_window.title("Jumbled Words Quiz Game -->> Colours")
    my_window.configure(background="gold")
    img1 = PhotoImage(file="back.png")

    lab_img1 = Button(
        my_window,
        image=img1,
        bg='gold',
        border=0,
        justify='center',
        command=back,
    )
    lab_img1.pack(anchor='nw', pady=10, padx=10)

    score = Label(
        text="Score:- 0",
        pady=10,
        bg="gold",
        fg="#000000",
        font="Titillium  14 bold"
    )
    score.pack(anchor="n")

    word = Label(
        text=jumbled_rand_word,
        pady=10,
        bg="gold",
        fg="#000000",
        font="Titillium  30 bold"
    )
    word.pack()

    get_input = Entry(
        font="none 26 bold",
        borderwidth=10,
        justify='center',
    )
    get_input.pack()

    submit = Button(
        text="Submit",
        width=18,
        borderwidth=8,
        font=("", 13),
        fg="#000000",
        bg="silver",
        command=check_submit,
    )
    submit.pack(pady=(10, 20))

    change = Button(
        text="Change Word",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="silver",
        font=("", 13),
        command=change,
    )
    change.pack()

    ans = Button(
        text="Answer",
        width=18,
        borderwidth=8,
        fg="#000000",
        bg="silver",
        font=("", 13),
        command=show_answer,
    )
    ans.pack(pady=(20, 10))

    ans_lab = Label(
        text="",
        bg="gold",
        fg="#000000",
        font="Courier 15 bold",
    )
    ans_lab.pack()

    my_window.mainloop()
