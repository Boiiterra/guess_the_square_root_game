from tkinter import Tk, Frame, Label, Button, Entry, Grid
from tkinter.constants import NORMAL, TOP, BOTH, CENTER, DISABLED, END, BOTTOM
from random import randint
from configparser import ConfigParser


def colors_reset():
    parser = ConfigParser()
    parser.read("colors.txt")
    parser.get("colors", "background", "#000000")
    parser.get("colors", "foreground", "#00ff00")
    parser.get("colors", "active_foreground", "#008000")
    parser.get("colors", "home_btn_fore", "#0000FF")
    parser.get("colors", "home_bts_active_fore", "#00008B")
    parser.get("colors", "main_btn_fore", "#00ff00")
    parser.get("colors", "main_btn_back", "#000000")
    parser.get("colors", "main_btn_active_fore", "#008000")
    parser.get("colors", "num_btn_back", "#0a0a0a")
    parser.get("colors", "num_btn_fore", "#00ff00")
    parser.get("colors", "num_btn_active_fore", "#008000")
    with open("colors.txt", 'w') as configfile:
        parser.write(configfile)
    # Reset the colors 
    # parser.read("colors.txt")
    global bg, fg, active_fg, home_btn_fg, home_btn_active_fg, main_btn_fg, main_btn_bg, main_btn_active_fg, num_bg, num_fg, num_active_fg
    bg = parser.get("colors", "background")
    fg = parser.get("colors", "foreground")
    active_fg = parser.get("colors", "active_foreground")
    home_btn_fg = parser.get("colors", "home_btn_fore")
    home_btn_active_fg = parser.get("colors", "home_bts_active_fore")
    main_btn_fg = parser.get("colors", "main_btn_fore")
    main_btn_bg = parser.get("colors", "main_btn_back")
    main_btn_active_fg = parser.get("colors", "main_btn_active_fore")
    num_bg = parser.get("colors", "num_btn_back")
    num_fg = parser.get("colors", "num_btn_fore")
    num_active_fg = parser.get("colors", "num_btn_active_fore")


# Color section
parser = ConfigParser()
parser.read("colors.txt")
bg = parser.get("colors", "background")
fg = parser.get("colors", "foreground")
active_fg = parser.get("colors", "active_foreground")
home_btn_fg = parser.get("colors", "home_btn_fore")
home_btn_active_fg = parser.get("colors", "home_bts_active_fore")
main_btn_fg = parser.get("colors", "main_btn_fore")
main_btn_bg = parser.get("colors", "main_btn_back")
main_btn_active_fg = parser.get("colors", "main_btn_active_fore")
num_bg = parser.get("colors", "num_btn_back")
num_fg = parser.get("colors", "num_btn_fore")
num_active_fg = parser.get("colors", "num_btn_active_fore")


class MainAppBody(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.title("Guess the square root of random number")
        self.iconbitmap("icon.ico")
        self.geometry(f"{(self.winfo_screenwidth() // 2) + 500}x{(self.winfo_screenheight() // 2) + 200}")
        self.minsize(800, 600)
        self.maxsize(self.winfo_screenwidth(), self.winfo_screenheight())

        container = Frame(self)
        container.pack(side=TOP, fill=BOTH, expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame_collection = (GreetingsPage, MainPage, Settings_page)

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
        Frame.__init__(self, parent, bg=bg)

        text = "Welcome to 'guess the square root\n" \
               "of random number' game. Range of\n" \
               "numbers starts at 11 and ends at 99.\n" \
               "\nPress start to continue."

        welcome_text = Label(self, text=text, font=("Verdana", 45), bg="#000000", fg=fg)
        welcome_text.pack(fill=BOTH, expand=True)

        start_button = Button(self, text="Start", bg=num_bg, fg=fg, font=("Arial", 45),
                              activeforeground=active_fg, activebackground=bg, bd=0,
                              disabledforeground=bg, command=lambda: controller.show_frame(MainPage))
        start_button.pack(fill=BOTH, pady=2, expand=True)

        settings_button = Button(self, text="Settings", bg=num_bg, fg=home_btn_fg, font=("Arial", 45),
                                activeforeground=home_btn_active_fg, activebackground=bg, bd=0,
                                disabledforeground=bg, command=lambda: controller.show_frame(Settings_page))
        settings_button.pack(fill=BOTH, side=BOTTOM, expand=True)

        def font_resize(e): 
            """Resizes font based on window height and width"""
            # based on width
            if e.width <= 912:
                welcome_text.config(font=('Verdana', 30))
                settings_button.config(font=('Arial', 45))
                start_button.config(font=('Arial', 45))
            elif e.width > 912 and e.width <= 1004:
                welcome_text.config(font=("Verdana", 36))
                settings_button.config(font=('Arial', 45))
                start_button.config(font=('Arial', 45))
            elif e.width > 1004 and e.width < 1160:
                welcome_text.config(font=("Verdana", 40))
                settings_button.config(font=('Arial', 45))
                start_button.config(font=('Arial', 45))
            elif e.width > 1160:
                welcome_text.config(font=('Verdana', 45))
                settings_button.config(font=('Arial', 45))
                start_button.config(font=('Arial', 45))
            if e.width == 1160:
                welcome_text.config(font=("Verdana", 40))
                settings_button.config(font=('Arial', 45))
                start_button.config(font=('Arial', 45))
            elif e.height <= 610 and e.width > 1160:
                start_button.config(font=('Arial', 35))
                settings_button.config(font=('Arial', 35))
            elif e.height > 610 and e.height <= 645 and e.width > 1160:
                start_button.config(font=('Arial', 45))
                settings_button.config(font=('Arial', 45))
            elif e.height > 645 and e.height <= 700 and e.width > 1160:
                start_button.config(font=('Arial', 55))
                settings_button.config(font=('Arial', 55))
            elif e.height > 700 and e.height <= 715 and e.width > 1160:
                start_button.config(font=('Arial', 65))
                settings_button.config(font=('Arial', 65))
            elif e.height > 740 and e.height <= 795 and e.width > 1160:
                start_button.config(font=('Arial', 75))
                settings_button.config(font=('Arial', 75))
            elif e.height > 795 and e.height <= 807 and e.width > 1160:
                start_button.config(font=('Arial', 85))
                settings_button.config(font=('Arial', 85))
            elif e.height > 807 and e.width > 1160:
                start_button.config(font=('Arial', 95))
                settings_button.config(font=('Arial', 95))

        self.bind("<Configure>", font_resize)


class Settings_page(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=bg)

        

class MainPage(Frame):
    integer = None

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=bg)
        self.controller = controller

        # print(self.winfo_screenheight())

        MainPage.integer = randint(11, 99)

        text = f"Square root of {MainPage.integer ** 2} is"

        number_display = Label(self, text=text, font=("Verdana", 75), bg="#000000", fg=fg)
        number_display.pack(expand=True)

        answer_input = Entry(self, justify=CENTER, font=("Times New Roman", 55), bg=bg, fg=fg,
                             state=DISABLED, disabledbackground=bg, width=2, bd=1, disabledforeground=fg,
                             cursor="arrow")
        answer_input.pack(expand=True)

        def insert_number(number):
            answer_input.config(state=NORMAL)
            answer_input.insert(END, str(number))
            answer_input.config(state=DISABLED)
            confirm_button.config(state=NORMAL)

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
            clear_button.config(text="Clear", command=clear, fg=fg, activeforeground=active_fg)
            confirm_button.config(state=DISABLED)
            answer_input.config(state=DISABLED)

        def buttons_on():
            one.config(state=NORMAL)
            two.config(state=NORMAL)
            three.config(state=NORMAL)
            four.config(state=NORMAL)
            five.config(state=NORMAL)
            six.config(state=NORMAL)
            seven.config(state=NORMAL)
            eight.config(state=NORMAL)
            nine.config(state=NORMAL)
            zero.config(state=NORMAL)

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
                    clear_button.config(text="Home", command=home, fg=home_btn_fg, activeforeground=home_btn_active_fg)
                else:
                    new_text = f"Correct answer was {MainPage.integer}"
                    number_display.config(text=new_text)
                    answer_input.config(bd=0)
                    buttons_off()
                    clear_button.config(text="Home", command=home, fg=home_btn_fg, activeforeground=home_btn_active_fg)
            else:
                MainPage.integer = randint(11, 99)
                new_text = f"Square root of {MainPage.integer ** 2} is"
                number_display.config(text=new_text)
                answer_input.config(bd=1)
                buttons_on()
                clear_button.config(text="Clear", command=clear, fg=fg, activeforeground=active_fg)
                confirm_button.config(state=DISABLED)
            answer_input.delete(0, END)
            answer_input.config(state=DISABLED)

        buttons_container = Label(self, bg=bg)
        buttons_container.pack(expand=True, side=BOTTOM, anchor='s')

        Grid.rowconfigure(buttons_container, 0, weight=1)
        Grid.rowconfigure(buttons_container, 1, weight=1)
        Grid.rowconfigure(buttons_container, 2, weight=1)
        Grid.columnconfigure(buttons_container, 0, weight=1)
        Grid.columnconfigure(buttons_container, 1, weight=1)
        Grid.columnconfigure(buttons_container, 2, weight=1)

        btn_d = 50

        one = Button(buttons_container, text="1", font=("Arial", btn_d), command=lambda: insert_number(1),
                     activeforeground=active_fg, activebackground=num_bg, disabledforeground=num_bg,
                     bg=num_bg, fg=fg)
        one.grid(column=0, row=2, sticky="nsew")

        two = Button(buttons_container, text="2", font=("Arial", btn_d), command=lambda: insert_number(2),
                     activeforeground=active_fg, activebackground=num_bg, disabledforeground=num_bg,
                     bg=num_bg, fg=fg)
        two.grid(column=1, row=2, sticky="nsew")

        three = Button(buttons_container, text="3", font=("Arial", btn_d), command=lambda: insert_number(3),
                       activeforeground=active_fg, activebackground=num_bg, disabledforeground=num_bg,
                       bg=num_bg, fg=fg)
        three.grid(column=2, row=2, sticky="nsew")

        four = Button(buttons_container, text="4", font=("Arial", btn_d), command=lambda: insert_number(4),
                      activeforeground=active_fg, activebackground=num_bg, disabledforeground=num_bg,
                      bg=num_bg, fg=fg)
        four.grid(column=0, row=1, sticky="nsew")

        five = Button(buttons_container, text="5", font=("Arial", btn_d), command=lambda: insert_number(5),
                      activeforeground=active_fg, activebackground=num_bg, disabledforeground=num_bg,
                      bg=num_bg, fg=fg)
        five.grid(column=1, row=1, sticky="nsew")

        six = Button(buttons_container, text="6", font=("Arial", btn_d), command=lambda: insert_number(6),
                     activeforeground=active_fg, activebackground=num_bg, disabledforeground=num_bg,
                     bg=num_bg, fg=fg)
        six.grid(column=2, row=1, sticky="nsew")

        seven = Button(buttons_container, text="7", font=("Arial", btn_d), command=lambda: insert_number(7),
                       activeforeground=active_fg, activebackground=num_bg, disabledforeground=num_bg,
                       bg=num_bg, fg=fg)
        seven.grid(column=0, row=0, sticky="nsew")

        eight = Button(buttons_container, text="8", font=("Arial", btn_d), command=lambda: insert_number(8),
                       activeforeground=active_fg, activebackground=num_bg, disabledforeground=num_bg,
                       bg=num_bg, fg=fg)
        eight.grid(column=1, row=0, sticky="nsew")

        nine = Button(buttons_container, text="9", font=("Arial", btn_d), command=lambda: insert_number(9),
                      activeforeground=active_fg, activebackground=num_bg, disabledforeground=num_bg,
                      bg=num_bg, fg=fg)
        nine.grid(column=2, row=0, sticky="nsew")

        zero = Button(buttons_container, text="0", font=("Arial", btn_d), command=lambda: insert_number(0),
                      activeforeground=active_fg, activebackground=num_bg, disabledforeground=num_bg,
                      bg=num_bg, fg=fg)
        zero.grid(column=3, row=0, sticky="nsew")

        clear_button = Button(buttons_container, text="Clear", font=("Arial", btn_d), command=clear,
                              activeforeground=active_fg, activebackground=bg, disabledforeground=bg,
                              bg=bg, fg=fg)
        clear_button.grid(column=3, row=1, sticky="nsew")

        confirm_button = Button(buttons_container, text="Confirm", font=("Arial", btn_d), command=confirm, state=DISABLED,
                                activeforeground=active_fg, activebackground=bg, disabledforeground=bg,
                                bg=bg, fg=fg)
        confirm_button.grid(column=3, row=2, sticky="nsew")

        def font_resize_main_page(e): 
            """Resizes font based on window height and width"""
            # Based on height, with limiter as 1161 width
            if e.width <= 1160:  # Resets button and entry font sizes to default
                btn_d = 50  # Button default font
                answer_input.config(font=('Times New Roman', 55))
                one.config(font=('Arial', btn_d))
                two.config(font=('Arial', btn_d))
                three.config(font=('Arial', btn_d))
                four.config(font=('Arial', btn_d))
                five.config(font=('Arial', btn_d))
                six.config(font=('Arial', btn_d))
                seven.config(font=('Arial', btn_d))
                eight.config(font=('Arial', btn_d))
                nine.config(font=('Arial', btn_d))
                zero.config(font=('Arial', btn_d))
                clear_button.config(font=('Arial', btn_d))
                confirm_button.config(font=('Arial', btn_d))
            elif e.height <= 610 and e.width > 1160:
                btn_ssf = 45  # Button smallest font
                answer_input.config(font=('Times New Roman', 55))
                one.config(font=('Arial', btn_ssf))
                two.config(font=('Arial', btn_ssf))
                three.config(font=('Arial', btn_ssf))
                four.config(font=('Arial', btn_ssf))
                five.config(font=('Arial', btn_ssf))
                six.config(font=('Arial', btn_ssf))
                seven.config(font=('Arial', btn_ssf))
                eight.config(font=('Arial', btn_ssf))
                nine.config(font=('Arial', btn_ssf))
                zero.config(font=('Arial', btn_ssf))
                clear_button.config(font=('Arial', btn_ssf))
                confirm_button.config(font=('Arial', btn_ssf))
            elif e.height > 610 and e.height <= 645 and e.width > 1160:
                btn_d = 50  # Button default font
                answer_input.config(font=('Times New Roman', 55))
                one.config(font=('Arial', btn_d))
                two.config(font=('Arial', btn_d))
                three.config(font=('Arial', btn_d))
                four.config(font=('Arial', btn_d))
                five.config(font=('Arial', btn_d))
                six.config(font=('Arial', btn_d))
                seven.config(font=('Arial', btn_d))
                eight.config(font=('Arial', btn_d))
                nine.config(font=('Arial', btn_d))
                zero.config(font=('Arial', btn_d))
                clear_button.config(font=('Arial', btn_d))
                confirm_button.config(font=('Arial', btn_d))
            elif e.height > 645 and e.height <= 700 and e.width > 1160:
                btn_m = 55  # Button medium font
                answer_input.config(font=('Times New Roman', 60))
                one.config(font=('Arial', btn_m))
                two.config(font=('Arial', btn_m))
                three.config(font=('Arial', btn_m))
                four.config(font=('Arial', btn_m))
                five.config(font=('Arial', btn_m))
                six.config(font=('Arial', btn_m))
                seven.config(font=('Arial', btn_m))
                eight.config(font=('Arial', btn_m))
                nine.config(font=('Arial', btn_m))
                zero.config(font=('Arial', btn_m))
                clear_button.config(font=('Arial', btn_m))
                confirm_button.config(font=('Arial', btn_m))
            elif e.height > 700 and e.height <= 715 and e.width > 1160:
                btn_l = 60  # Button large font
                answer_input.config(font=('Times New Roman', 60))
                one.config(font=('Arial', btn_l))
                two.config(font=('Arial', btn_l))
                three.config(font=('Arial', btn_l))
                four.config(font=('Arial', btn_l))
                five.config(font=('Arial', btn_l))
                six.config(font=('Arial', btn_l))
                seven.config(font=('Arial', btn_l))
                eight.config(font=('Arial', btn_l))
                nine.config(font=('Arial', btn_l))
                zero.config(font=('Arial', btn_l))
                clear_button.config(font=('Arial', btn_l))
                confirm_button.config(font=('Arial', btn_l))
            elif e.height > 740 and e.height <= 795 and e.width > 1160:
                btn_h = 65  # Button huge font
                answer_input.config(font=('Times New Roman', 60))
                one.config(font=('Arial', btn_h))
                two.config(font=('Arial', btn_h))
                three.config(font=('Arial', btn_h))
                four.config(font=('Arial', btn_h))
                five.config(font=('Arial', btn_h))
                six.config(font=('Arial', btn_h))
                seven.config(font=('Arial', btn_h))
                eight.config(font=('Arial', btn_h))
                nine.config(font=('Arial', btn_h))
                zero.config(font=('Arial', btn_h))
                clear_button.config(font=('Arial', btn_h))
                confirm_button.config(font=('Arial', btn_h))
            elif e.height > 795 and e.height <= 807 and e.width > 1160:
                btn_h = 65  # Button huge font
                answer_input.config(font=('Times New Roman', 66))
                one.config(font=('Arial', btn_h))
                two.config(font=('Arial', btn_h))
                three.config(font=('Arial', btn_h))
                four.config(font=('Arial', btn_h))
                five.config(font=('Arial', btn_h))
                six.config(font=('Arial', btn_h))
                seven.config(font=('Arial', btn_h))
                eight.config(font=('Arial', btn_h))
                nine.config(font=('Arial', btn_h))
                zero.config(font=('Arial', btn_h))
                clear_button.config(font=('Arial', btn_h))
                confirm_button.config(font=('Arial', btn_h))
            elif e.height > 807 and e.width > 1160:
                btn_h = 65  # Button huge font
                answer_input.config(font=('Times New Roman', 75))
                one.config(font=('Arial', btn_h))
                two.config(font=('Arial', btn_h))
                three.config(font=('Arial', btn_h))
                four.config(font=('Arial', btn_h))
                five.config(font=('Arial', btn_h))
                six.config(font=('Arial', btn_h))
                seven.config(font=('Arial', btn_h))
                eight.config(font=('Arial', btn_h))
                nine.config(font=('Arial', btn_h))
                zero.config(font=('Arial', btn_h))
                clear_button.config(font=('Arial', btn_h))
                confirm_button.config(font=('Arial', btn_h))
            # based on width
            if e.width <= 830:
                txt_ssf = 51  # Main text smallest font
                number_display.config(font=('Verdana', txt_ssf))
            elif e.width > 830 and e.width <= 912:
                txt_sf = 55  # Main text small font
                number_display.config(font=('Verdana', txt_sf))
            elif e.width > 912 and e.width <= 940:
                txt_m = 61  # Main text medium font
                number_display.config(font=("Verdana", txt_m))
            elif e.width > 940 and e.width <= 1160:
                txt_l = 65  # Main text large font
                number_display.config(font=("Verdana", txt_l))
            elif e.width > 1160:
                txt_d = 75  # Main text default font
                number_display.config(font=('Verdana', txt_d))


        self.bind("<Configure>", font_resize_main_page)
