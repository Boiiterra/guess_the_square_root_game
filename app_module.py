from tkinter import Tk, Frame, Label, Button, Entry
from tkinter.constants import ACTIVE, TOP, BOTH, CENTER, DISABLED, NORMAL, END, BOTTOM
from random import randint


class MainAppBody(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.title("Guess the square root of random number")
        self.iconbitmap("icon.ico")
        self.geometry(f"{(self.winfo_screenwidth() // 2) + 500}x{(self.winfo_screenheight() // 2) + 200}")
        self.resizable(0, 0)

        container = Frame(self)
        container.pack(side=TOP, fill=BOTH, expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame_collection = (GreetingsPage, MainPage)

        for current_frame in frame_collection:
            frame = current_frame(container, self)
            self.frames[current_frame] = frame

            frame.grid(column=0, row=0, sticky="nsew")

        self.show_frame(GreetingsPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class GreetingsPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg="black")

        text = "Welcome to 'guess the square root\n" \
               "of random number' game. Range of\n" \
               "numbers starts at 11 and ends at 99.\n" \
               "\nPress start to continue."

        welcome_text = Label(self, text=text, font=("Verdana", 45), bg="#000000", fg="#00ff00")
        welcome_text.pack(fill=BOTH)

        start_button = Button(self, text="\nStart\n", bg="#0a0c0a", fg="#00ff00", font=("Arial", 60),
                              activeforeground="green", activebackground="black", bd=0,
                              disabledforeground="black", command=lambda: controller.show_frame(MainPage))
        start_button.pack(fill=BOTH)


class MainPage(Frame):
    integer = None

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg="black")

        MainPage.integer = randint(11, 99)

        text = f"Square root of {MainPage.integer ** 2} is"

        number_display = Label(self, text=text, font=("Verdana", 75), bg="#000000", fg="#00ff00")
        number_display.pack()

        answer_input = Entry(self, justify=CENTER, font=("Times New Roman", 55), bg="black", fg="#00ff00",
                             selectbackground="white", selectforeground="#ff00ff", insertbackground="white",
                             state=DISABLED, disabledbackground="black", width=2, bd=1, disabledforeground="#00ff00",
                             cursor="arrow")
        answer_input.pack()

        def insert_number(number):
            answer_input.config(state=NORMAL)
            answer_input.insert(END, str(number))
            answer_input.config(state=DISABLED)
            confirm_button.config(state=ACTIVE)

        def clear():
            answer_input.config(state=NORMAL)
            answer_input.delete(0, END)
            answer_input.config(state=DISABLED)
            confirm_button.config(state=DISABLED)

        def home():
            controller.show_frame(GreetingsPage)
            MainPage.integer = randint(11, 99)
            new_text = f"Square root of {MainPage.integer ** 2} is"
            number_display.config(text=new_text)
            answer_input.config(bd=1)
            buttons_on()
            clear_button.config(text="Clear", command=clear)
            confirm_button.config(state=DISABLED)
            answer_input.config(state=DISABLED)

        def buttons_on():
            one.config(state=ACTIVE)
            two.config(state=ACTIVE)
            three.config(state=ACTIVE)
            four.config(state=ACTIVE)
            five.config(state=ACTIVE)
            six.config(state=ACTIVE)
            seven.config(state=ACTIVE)
            eight.config(state=ACTIVE)
            nine.config(state=ACTIVE)
            zero.config(state=ACTIVE)

        def buttons_off():
            one.config(state=DISABLED)
            two.config(state=DISABLED)
            three.config(state=DISABLED)
            four.config(state=DISABLED)
            five.config(state=DISABLED)
            six.config(state=DISABLED)
            seven.config(state=DISABLED)
            eight.config(state=DISABLED)
            nine.config(state=DISABLED)
            zero.config(state=DISABLED)

        def confirm():
            answer_input.config(state=NORMAL)
            if len(answer_input.get()) != 0:
                answer = int(answer_input.get())
                if answer == MainPage.integer:
                    new_text = f"Your answer is correct."
                    number_display.config(text=new_text)
                    answer_input.config(bd=0)
                    buttons_off()
                    clear_button.config(text="Home", command=home, fg=colours[9], activeforeground=colours[8])
                else:
                    new_text = f"Correct answer was {MainPage.integer}"
                    number_display.config(text=new_text)
                    answer_input.config(bd=0)
                    buttons_off()
                    clear_button.config(text="Home", command=home, fg=colours[9], activeforeground=colours[8])
            else:
                MainPage.integer = randint(11, 99)
                new_text = f"Square root of {MainPage.integer ** 2} is"
                number_display.config(text=new_text)
                answer_input.config(bd=1)
                buttons_on()
                clear_button.config(text="Clear", command=clear, fg=colours[1], activeforeground=colours[2])
                confirm_button.config(state=DISABLED)
            answer_input.delete(0, END)
            answer_input.config(state=DISABLED)

        button_font = ("Arial", 50)
        colours = ["black", '#00ff00', "green", "#0a0a0a", "#0a0a0c", "#0a0c0a", "#0c0a0a", "#ff001f", "dark blue",
                   "blue"]

        buttons_container = Label(self, bg="black")
        buttons_container.pack(side=BOTTOM)

        one = Button(buttons_container, text="1", font=button_font, command=lambda: insert_number(1),
                     activeforeground=colours[2], activebackground=colours[4], disabledforeground=colours[4],
                     bg=colours[4], fg=colours[1])
        one.grid(column=0, row=2)

        two = Button(buttons_container, text="2", font=button_font, command=lambda: insert_number(2),
                     activeforeground=colours[2], activebackground=colours[5], disabledforeground=colours[5],
                     bg=colours[5], fg=colours[1])
        two.grid(column=1, row=2)

        three = Button(buttons_container, text="3", font=button_font, command=lambda: insert_number(3),
                       activeforeground=colours[2], activebackground=colours[6], disabledforeground=colours[6],
                       bg=colours[6], fg=colours[1])
        three.grid(column=2, row=2)

        four = Button(buttons_container, text="4", font=button_font, command=lambda: insert_number(4),
                      activeforeground=colours[2], activebackground=colours[6], disabledforeground=colours[6],
                      bg=colours[6], fg=colours[1])
        four.grid(column=0, row=1)

        five = Button(buttons_container, text="5", font=button_font, command=lambda: insert_number(5),
                      activeforeground=colours[2], activebackground=colours[3], disabledforeground=colours[3],
                      bg=colours[3], fg=colours[1])
        five.grid(column=1, row=1)

        six = Button(buttons_container, text="6", font=button_font, command=lambda: insert_number(6),
                     activeforeground=colours[2], activebackground=colours[4], disabledforeground=colours[4],
                     bg=colours[4], fg=colours[1])
        six.grid(column=2, row=1)

        seven = Button(buttons_container, text="7", font=button_font, command=lambda: insert_number(7),
                       activeforeground=colours[2], activebackground=colours[4], disabledforeground=colours[4],
                       bg=colours[4], fg=colours[1])
        seven.grid(column=0, row=0)

        eight = Button(buttons_container, text="8", font=button_font, command=lambda: insert_number(8),
                       activeforeground=colours[2], activebackground=colours[5], disabledforeground=colours[5],
                       bg=colours[5], fg=colours[1])
        eight.grid(column=1, row=0)

        nine = Button(buttons_container, text="9", font=button_font, command=lambda: insert_number(9),
                      activeforeground=colours[2], activebackground=colours[6], disabledforeground=colours[6],
                      bg=colours[6], fg=colours[1])
        nine.grid(column=2, row=0)

        zero = Button(buttons_container, text="0", font=button_font, command=lambda: insert_number(0),
                      activeforeground=colours[2], activebackground=colours[3], disabledforeground=colours[3],
                      bg=colours[3], fg=colours[1])
        zero.grid(column=3, row=0, sticky="nsew")

        clear_button = Button(buttons_container, text="Clear", font=button_font, command=clear,
                              activeforeground=colours[2], activebackground=colours[0], disabledforeground=colours[0],
                              bg=colours[0], fg=colours[1])
        clear_button.grid(column=3, row=1, sticky="nsew")

        confirm_button = Button(buttons_container, text="Confirm", font=button_font, command=confirm, state=DISABLED,
                                activeforeground=colours[2], activebackground=colours[0], disabledforeground=colours[0],
                                bg=colours[0], fg=colours[1])
        confirm_button.grid(column=3, row=2)
