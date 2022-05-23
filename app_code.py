from tkinter import Tk, Frame, Label, Button, Entry, Grid
from configparser import ConfigParser
from webbrowser import open_new_tab
from platform import system
from random import randint

# Color section
parser = ConfigParser()

parser.read("theme_colors.txt")
bg = parser.get("colors", "background")
num_fg = parser.get("colors", "num_btn_fore")
home_btn_fg = parser.get("colors", "home_btn_fore")
active_fg = parser.get("colors", "active_foreground")
home_btn_active_fg = parser.get("colors", "home_bts_active_fore")
num_active_fg = parser.get("colors", "num_btn_active_fore")
current_theme = parser.get('theme', "current_theme")
main_btn_bg = parser.get("colors", "main_btn_back")
num_bg = parser.get("colors", "num_btn_back")
fg = parser.get("colors", "foreground")


def neon_theme_colors():

    global parser
    parser.read("theme_colors.txt")
    parser.set('theme', "current_theme", "neon")
    parser.set("colors", "background", "#000000")
    parser.set("colors", "foreground", "#00ff00")
    parser.set("colors", "num_btn_fore", "#00ff00")
    parser.set("colors", "num_btn_back", "#0a0a0a")
    parser.set("colors", "home_btn_fore", "#0000FF")
    parser.set("colors", "main_btn_back", "#000000")
    parser.set("colors", "active_foreground", "#008000")
    parser.set("colors", "home_bts_active_fore", "#00008B")
    parser.set("colors", "num_btn_active_fore", "#008000")
    with open("theme_colors.txt", "w") as config_file:
        parser.write(config_file)

    # Set colors
    parser.read("colors.txt")
    global bg, fg, active_fg, home_btn_fg, home_btn_active_fg, main_btn_bg, num_bg, num_fg, num_active_fg, current_theme
    home_btn_active_fg = parser.get("colors", "home_bts_active_fore")
    num_active_fg = parser.get("colors", "num_btn_active_fore")
    active_fg = parser.get("colors", "active_foreground")
    current_theme = parser.get('theme', "current_theme")
    main_btn_bg = parser.get("colors", "main_btn_back")
    home_btn_fg = parser.get("colors", "home_btn_fore")
    num_fg = parser.get("colors", "num_btn_fore")
    num_bg = parser.get("colors", "num_btn_back")
    fg = parser.get("colors", "foreground")
    bg = parser.get("colors", "background")


def dark_theme_colors():

    global parser
    parser.read("theme_colors.txt")
    parser.set("theme", "current_theme", "dark")
    parser.set("colors", "background", "#000000")
    parser.set("colors", "foreground", "#ffffff")
    parser.set("colors", "num_btn_back", "#0a0a0a")
    parser.set("colors", "num_btn_fore", "#8c8c8c")
    parser.set("colors", "home_btn_fore", "#474747")
    parser.set("colors", "main_btn_back", "#000000")
    parser.set("colors", "active_foreground", "#5e5e5e")
    parser.set("colors", "num_btn_active_fore", "#5e5e5e")
    parser.set("colors", "home_bts_active_fore", "#333333")
    with open("theme_colors.txt", 'w') as config_file:
        parser.write(config_file)

    # Set colors
    parser.read("colors.txt")
    global bg, fg, active_fg, home_btn_fg, home_btn_active_fg, main_btn_bg, num_bg, num_fg, num_active_fg, current_theme
    home_btn_active_fg = parser.get("colors", "home_bts_active_fore")
    num_active_fg = parser.get("colors", "num_btn_active_fore")
    active_fg = parser.get("colors", "active_foreground")
    current_theme = parser.get('theme', "current_theme")
    home_btn_fg = parser.get("colors", "home_btn_fore")
    main_btn_bg = parser.get("colors", "main_btn_back")
    num_bg = parser.get("colors", "num_btn_back")
    num_fg = parser.get("colors", "num_btn_fore")
    fg = parser.get("colors", "foreground")
    bg = parser.get("colors", "background")


def light_theme_colors():

    global parser
    parser.read("theme_colors.txt")
    parser.set('theme', "current_theme", "light")
    parser.set("colors", "background", "#bababa")
    parser.set("colors", "foreground", "#000000")
    parser.set("colors", "num_btn_fore", "#4d4d4d")
    parser.set("colors", "num_btn_back", "#999999")
    parser.set("colors", "home_btn_fore", "#404040")
    parser.set("colors", "main_btn_back", "#292929")
    parser.set("colors", "active_foreground", "#000000")
    parser.set("colors", "num_btn_active_fore", "#787878")
    parser.set("colors", "home_bts_active_fore", "#5e5e5e")
    with open("theme_colors.txt", 'w') as config_file:
        parser.write(config_file)

    # Set colors
    parser.read("colors.txt")
    global bg, fg, active_fg, home_btn_fg, home_btn_active_fg, main_btn_bg, num_bg, num_fg, num_active_fg, current_theme
    home_btn_active_fg = parser.get("colors", "home_bts_active_fore")
    num_active_fg = parser.get("colors", "num_btn_active_fore")
    active_fg = parser.get("colors", "active_foreground")
    current_theme = parser.get('theme', "current_theme")
    home_btn_fg = parser.get("colors", "home_btn_fore")
    main_btn_bg = parser.get("colors", "main_btn_back")
    num_bg = parser.get("colors", "num_btn_back")
    num_fg = parser.get("colors", "num_btn_fore")
    fg = parser.get("colors", "foreground")
    bg = parser.get("colors", "background")


class MainAppBody(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.title("Guess the square root of random number")
        if system().lower() != "linux":
            self.iconbitmap("icon.ico")
        self.geometry(f"{(self.winfo_screenwidth() // 2) + 500}x{(self.winfo_screenheight() // 2) + 200}")
        self.minsize(800, 600)
        self.maxsize(self.winfo_screenwidth(), self.winfo_screenheight())

        container = Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame_collection = (GreetingsPage, MainPage, SettingsPage)

        for current_frame in frame_collection:
            frame = current_frame(container, self)
            self.frames[current_frame] = frame
            frame.grid(column=0, row=0, sticky="nsew")

        self.show_frame(GreetingsPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    def get_page(self, page_class):
        return self.frames[page_class]


class GreetingsPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=bg)
        self.controller = controller

        text = "Welcome to 'guess the square root\n" \
               "of random number' game. Range of\n" \
               "numbers starts at 11 and ends at 99.\n" \
               "\nPress start to continue."

        self.welcome_text = Label(self, text=text, font=("Verdana", 45), bg=bg, fg=fg)
        self.welcome_text.pack(fill='both', expand=True)

        self.start_button = Button(self, text="Start", bg=num_bg, fg=fg, font=("Arial", 45),
                                   activeforeground=active_fg, activebackground=num_bg, bd=0, highlightthickness=0,
                                   disabledforeground=num_bg, command=lambda: controller.show_frame(MainPage))
        self.start_button.pack(fill='both', pady=2, expand=True)

        self.settings_button = Button(self, text="Settings", bg=num_bg, fg=home_btn_fg, font=("Arial", 45),
                                      activeforeground=home_btn_active_fg, activebackground=num_bg, bd=0, highlightthickness=0,
                                      disabledforeground=num_bg, command=lambda: controller.show_frame(SettingsPage))
        self.settings_button.pack(fill='both', side='bottom', expand=True)

        def font_resize(e):
            """Resizes font based on window's height and width"""
            # Text resize and buttons minimal resize
            if e.width <= 912:
                self.welcome_text.config(font=('Verdana', 30))
                self.settings_button.config(font=('Arial', 45))
                self.start_button.config(font=('Arial', 45))
            elif 912 < e.width <= 1004:
                self.welcome_text.config(font=("Verdana", 36))
                self.settings_button.config(font=('Arial', 45))
                self.start_button.config(font=('Arial', 45))
            elif 1004 < e.width < 1160:
                self.welcome_text.config(font=("Verdana", 40))
                self.settings_button.config(font=('Arial', 45))
                self.start_button.config(font=('Arial', 45))
            elif e.width > 1160:
                self.welcome_text.config(font=('Verdana', 45))
                self.settings_button.config(font=('Arial', 45))
                self.start_button.config(font=('Arial', 45))

        self.bind("<Configure>", font_resize)

    def greetings_page_theme_update(self):
        self.config(bg=bg)
        self.welcome_text.config(bg=bg, fg=fg)
        self.start_button.config(bg=num_bg, fg=fg, activeforeground=active_fg, activebackground=num_bg,
                                 disabledforeground=num_bg)
        self.settings_button.config(bg=num_bg, fg=home_btn_fg, activeforeground=home_btn_active_fg,
                                    activebackground=num_bg, disabledforeground=num_bg)


class SettingsPage(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=bg)
        self.controller = controller


        def call_link(*_):
            open_new_tab("https://github.com/TerraBoii")

        def enter(_):
            self.created_by.config(font=("Tahoma", 15, "underline"))

        def leave(_):
            self.created_by.config(font=("Tahoma", 15))

        self.created_by= Label(self, bg=bg, fg="#213c91", text="Created by: TerraBoii", 
                               font=("Tahoma", 15), cursor='hand2')
        self.created_by.pack(side='top')
        self.created_by.bind("<Button-1>", call_link)
        self.created_by.bind("<Enter>", enter)
        self.created_by.bind("<Leave>", leave)
        
        self.theme_info = Label(self, bg=bg, fg=fg, font=("Arial", 35), text='Choose the theme:')
        self.theme_info.pack(side='top', expand=True)

        self.themes_changers_container = Label(self, bg=bg)
        self.themes_changers_container.pack(side='top', anchor='n')

        Grid.rowconfigure(self.themes_changers_container, 0, weight=1)
        Grid.columnconfigure(self.themes_changers_container, 0, weight=1)
        Grid.columnconfigure(self.themes_changers_container, 1, weight=1)
        Grid.columnconfigure(self.themes_changers_container, 2, weight=1)

        self.neon_theme_btn = Button(self.themes_changers_container, text="Neon green", bg=num_bg, fg=num_fg,
                                     font=("Times New Roman", 55), highlightthickness=0, bd=0,
                                     activeforeground=num_active_fg, activebackground=num_bg,
                                     disabledforeground=num_bg, command=self.change_theme_to_neon)
        self.neon_theme_btn.grid(row=0, column=1, sticky='nsew')

        self.dark_theme_btn = Button(self.themes_changers_container, text="Dark", bg=bg, fg=fg, font=("Times New Roman", 55),
                                     highlightthickness=0, bd=0, activeforeground=active_fg, activebackground=bg,
                                     disabledforeground=bg, command=self.change_theme_to_dark)
        self.dark_theme_btn.grid(row=0, column=0, sticky='nsew')

        self.light_theme_btn = Button(self.themes_changers_container, text="light", bg=bg, fg=fg, bd=0,
                                      font=("Times New Roman", 55), highlightthickness=0, activebackground=bg,
                                      activeforeground=active_fg, disabledforeground=bg, command=self.change_theme_to_light)
        self.light_theme_btn.grid(row=0, column=2, sticky='nsew')

        self.home_button = Button(self, text="Home", bg=num_bg, fg=home_btn_fg, font=("Arial", 45), highlightthickness=0,
                                  activeforeground=home_btn_active_fg, activebackground=num_bg, bd=0,
                                  disabledforeground=num_bg, command=lambda: controller.show_frame(GreetingsPage))
        self.home_button.pack(fill='both', side='bottom', expand=True)

        self.placeholder = Label(self, font=('Arial', 55), bg=bg)
        self.placeholder.pack(side='bottom')

        if current_theme == "neon":
            self.dark_theme_btn.config(state='normal')
            self.light_theme_btn.config(state='normal')
            self.neon_theme_btn.config(state='disabled')
        elif current_theme == 'dark':
            self.dark_theme_btn.config(state='disabled')
            self.light_theme_btn.config(state='normal')
            self.neon_theme_btn.config(state='normal')
        elif current_theme == 'light':
            self.dark_theme_btn.config(state='normal')
            self.neon_theme_btn.config(state='normal')
            self.light_theme_btn.config(state='disabled')

        def font_resize_settings(e):
            """Resizes font based on window height and width"""
            # Change font for big buttons
            if e.width <= 912:
                # self.home_button.config(font=('Arial', 45))
                self.neon_theme_btn.config(font=('Times New Roman', 42))
                self.dark_theme_btn.config(font=('Times New Roman', 42))
                self.light_theme_btn.config(font=('Times New Roman', 42))
            elif 912 < e.width <= 1160:
                # self.home_button.config(font=('Arial', 55))
                self.neon_theme_btn.config(font=('Times New Roman', 50))
                self.dark_theme_btn.config(font=('Times New Roman', 50))
                self.light_theme_btn.config(font=('Times New Roman', 50))
            elif e.width > 1160:
                # self.home_button.config(font=('Arial', 55))
                self.neon_theme_btn.config(font=('Times New Roman', 55))
                self.dark_theme_btn.config(font=('Times New Roman', 55))
                self.light_theme_btn.config(font=('Times New Roman', 55))

        self.bind("<Configure>", font_resize_settings)

    def settings_page_theme_update(self):
        self.config(bg=bg)
        self.created_by.config(bg=bg)
        self.placeholder.config(bg=bg)
        self.theme_info.config(bg=bg, fg=fg)
        self.themes_changers_container.config(bg=bg)
        self.dark_theme_btn.config(bg=bg, fg=fg, activeforeground=active_fg, activebackground=bg, disabledforeground=bg)
        self.light_theme_btn.config(bg=bg, fg=fg, activeforeground=active_fg, activebackground=bg,
                                    disabledforeground=bg)
        self.home_button.config(bg=num_bg, fg=home_btn_fg, activeforeground=home_btn_active_fg, activebackground=num_bg,
                                disabledforeground=num_bg)
        self.neon_theme_btn.config(bg=num_bg, fg=num_fg, activeforeground=num_active_fg, activebackground=num_bg,
                                   disabledforeground=num_bg)

    def change_theme_to_dark(self):
        self.dark_theme_btn.config(state='disabled')
        self.neon_theme_btn.config(state='normal')
        self.light_theme_btn.config(state='normal')
        dark_theme_colors()
        self.settings_page_theme_update()
        page = self.controller.get_page(MainPage)
        page.main_page_theme_update()
        page = self.controller.get_page(GreetingsPage)
        page.greetings_page_theme_update()

    def change_theme_to_neon(self):
        self.dark_theme_btn.config(state='normal')
        self.neon_theme_btn.config(state='disabled')
        self.light_theme_btn.config(state='normal')
        neon_theme_colors()
        self.settings_page_theme_update()
        page = self.controller.get_page(MainPage)
        page.main_page_theme_update()
        page = self.controller.get_page(GreetingsPage)
        page.greetings_page_theme_update()

    def change_theme_to_light(self):
        self.dark_theme_btn.config(state='normal')
        self.neon_theme_btn.config(state='normal')
        self.light_theme_btn.config(state='disabled')
        light_theme_colors()
        self.settings_page_theme_update()
        page = self.controller.get_page(MainPage)
        page.main_page_theme_update()
        page = self.controller.get_page(GreetingsPage)
        page.greetings_page_theme_update()


class MainPage(Frame):
    integer = None

    def __init__(self, parent, controller):
        Frame.__init__(self, parent, bg=bg)
        self.controller = controller

        MainPage.integer = randint(11, 99)
        text = f"Square root of {MainPage.integer ** 2} is"

        self.number_display = Label(self, text=text, font=("Verdana", 75), bg=bg, fg=fg)
        self.number_display.pack(expand=True)

        self.answer_input = Entry(self, justify='center', font=("Times New Roman", 55), bg=bg, fg=fg,
                                  state='disabled', disabledbackground=bg, width=2, bd=1, disabledforeground=fg,
                                  cursor="arrow")
        self.answer_input.pack(expand=True)

        def insert_number(number):
            if number == 0 and self.answer_input.get() == "":
                pass
            else:
                self.answer_input.config(state='normal')
                self.answer_input.insert('end', str(number))
                self.answer_input.config(state='disabled')
                self.clear_button.config(state='normal')
                if len(self.answer_input.get()) >= 2:
                    self.confirm_button.config(state='normal')

        def clear():
            self.answer_input.config(state='normal')
            self.answer_input.delete(0, 'end')
            self.answer_input.config(state='disabled')
            self.confirm_button.config(state='disabled')
            self.clear_button.config(state='disabled')

        def home():
            controller.show_frame(GreetingsPage)
            MainPage.integer = randint(11, 99)
            new_text = f"Square root of {MainPage.integer ** 2} is"
            self.number_display.config(text=new_text)
            self.answer_input.config(bd=1)
            buttons_on()
            self.clear_button.config(text="Clear", command=clear, fg=fg, activeforeground=active_fg, state='disabled')
            self.confirm_button.config(state='disabled')
            self.answer_input.config(state='disabled')

        def buttons_on():
            self.one.config(state='normal')
            self.two.config(state='normal')
            self.three.config(state='normal')
            self.four.config(state='normal')
            self.five.config(state='normal')
            self.six.config(state='normal')
            self.seven.config(state='normal')
            self.eight.config(state='normal')
            self.nine.config(state='normal')
            self.zero.config(state='normal')

        def buttons_off():
            self.one.config(state='disabled')
            self.two.config(state='disabled')
            self.three.config(state='disabled')
            self.four.config(state='disabled')
            self.five.config(state='disabled')
            self.six.config(state='disabled')
            self.seven.config(state='disabled')
            self.eight.config(state='disabled')
            self.nine.config(state='disabled')
            self.zero.config(state='disabled')

        def confirm():
            self.answer_input.config(state='normal')
            if len(self.answer_input.get()) != 0:
                answer = int(self.answer_input.get())
                if answer == MainPage.integer:
                    new_text = f"Your answer is correct."
                    self.number_display.config(text=new_text)
                    self.answer_input.config(bd=0)
                    buttons_off()
                    self.clear_button.config(text="Home", command=home, fg=home_btn_fg,
                                             activeforeground=home_btn_active_fg)
                else:
                    new_text = f"Correct answer was {MainPage.integer}"
                    self.number_display.config(text=new_text)
                    self.answer_input.config(bd=0)
                    buttons_off()
                    self.clear_button.config(text="Home", command=home, fg=home_btn_fg,
                                             activeforeground=home_btn_active_fg)
            else:
                MainPage.integer = randint(11, 99)
                new_text = f"Square root of {MainPage.integer ** 2} is"
                self.number_display.config(text=new_text)
                self.answer_input.config(bd=1)
                buttons_on()
                self.clear_button.config(text="Clear", command=clear, fg=fg, activeforeground=active_fg)
                self.confirm_button.config(state='disabled')
                self.clear_button.config(state='disabled')
            self.answer_input.delete(0, 'end')
            self.answer_input.config(state='disabled')

        self.buttons_container = Label(self, bg=bg)
        self.buttons_container.pack(expand=True, side='bottom', anchor='s')

        Grid.rowconfigure(self.buttons_container, 0, weight=1)
        Grid.rowconfigure(self.buttons_container, 1, weight=1)
        Grid.rowconfigure(self.buttons_container, 2, weight=1)
        Grid.columnconfigure(self.buttons_container, 0, weight=1)
        Grid.columnconfigure(self.buttons_container, 1, weight=1)
        Grid.columnconfigure(self.buttons_container, 2, weight=1)
        Grid.columnconfigure(self.buttons_container, 3, weight=1)

        btn_d = 50

        self.one = Button(self.buttons_container, text="1", font=("Arial", btn_d), command=lambda: insert_number(1),
                          activeforeground=num_active_fg, activebackground=num_bg, disabledforeground=num_bg,
                          bg=num_bg, fg=num_fg)
        self.one.grid(column=0, row=2, sticky="nsew")

        self.two = Button(self.buttons_container, text="2", font=("Arial", btn_d), command=lambda: insert_number(2),
                          activeforeground=num_active_fg, activebackground=num_bg, disabledforeground=num_bg,
                          bg=num_bg, fg=num_fg)
        self.two.grid(column=1, row=2, sticky="nsew")

        self.three = Button(self.buttons_container, text="3", font=("Arial", btn_d), command=lambda: insert_number(3),
                            activeforeground=num_active_fg, activebackground=num_bg, disabledforeground=num_bg,
                            bg=num_bg, fg=num_fg)
        self.three.grid(column=2, row=2, sticky="nsew")

        self.four = Button(self.buttons_container, text="4", font=("Arial", btn_d), command=lambda: insert_number(4),
                           activeforeground=num_active_fg, activebackground=num_bg, disabledforeground=num_bg,
                           bg=num_bg, fg=num_fg)
        self.four.grid(column=0, row=1, sticky="nsew")

        self.five = Button(self.buttons_container, text="5", font=("Arial", btn_d), command=lambda: insert_number(5),
                           activeforeground=num_active_fg, activebackground=num_bg, disabledforeground=num_bg,
                           bg=num_bg, fg=num_fg)
        self.five.grid(column=1, row=1, sticky="nsew")

        self.six = Button(self.buttons_container, text="6", font=("Arial", btn_d), command=lambda: insert_number(6),
                          activeforeground=num_active_fg, activebackground=num_bg, disabledforeground=num_bg,
                          bg=num_bg, fg=num_fg)
        self.six.grid(column=2, row=1, sticky="nsew")

        self.seven = Button(self.buttons_container, text="7", font=("Arial", btn_d), command=lambda: insert_number(7),
                            activeforeground=num_active_fg, activebackground=num_bg, disabledforeground=num_bg,
                            bg=num_bg, fg=num_fg)
        self.seven.grid(column=0, row=0, sticky="nsew")

        self.eight = Button(self.buttons_container, text="8", font=("Arial", btn_d), command=lambda: insert_number(8),
                            activeforeground=num_active_fg, activebackground=num_bg, disabledforeground=num_bg,
                            bg=num_bg, fg=num_fg)
        self.eight.grid(column=1, row=0, sticky="nsew")

        self.nine = Button(self.buttons_container, text="9", font=("Arial", btn_d), command=lambda: insert_number(9),
                           activeforeground=num_active_fg, activebackground=num_bg, disabledforeground=num_bg,
                           bg=num_bg, fg=num_fg)
        self.nine.grid(column=2, row=0, sticky="nsew")

        self.zero = Button(self.buttons_container, text="0", font=("Arial", btn_d), command=lambda: insert_number(0),
                           activeforeground=num_active_fg, activebackground=num_bg, disabledforeground=num_bg,
                           bg=num_bg, fg=num_fg)
        self.zero.grid(column=3, row=0, sticky="nsew")

        self.clear_button = Button(self.buttons_container, text="Clear", font=("Arial", btn_d), command=clear,
                                   activeforeground=active_fg, activebackground=bg, disabledforeground=bg,
                                   bg=bg, fg=fg, state='disabled')
        self.clear_button.grid(column=3, row=1, sticky="nsew")

        self.confirm_button = Button(self.buttons_container, text="Confirm", font=("Arial", btn_d), command=confirm,
                                     state='disabled', bg=bg, fg=fg,
                                     activeforeground=active_fg, activebackground=bg, disabledforeground=bg)
        self.confirm_button.grid(column=3, row=2, sticky="nsew")

        def font_resize_main_page(e):
            """Resizes font based on window height and width"""
            # Buttons and entry resize
            if e.width <= 935:
                btn_ssf1 = 45  # Button smallest font
                self.answer_input.config(font=('Times New Roman', 55))
                self.one.config(font=('Arial', btn_ssf1))
                self.two.config(font=('Arial', btn_ssf1))
                self.three.config(font=('Arial', btn_ssf1))
                self.four.config(font=('Arial', btn_ssf1))
                self.five.config(font=('Arial', btn_ssf1))
                self.six.config(font=('Arial', btn_ssf1))
                self.seven.config(font=('Arial', btn_ssf1))
                self.eight.config(font=('Arial', btn_ssf1))
                self.nine.config(font=('Arial', btn_ssf1))
                self.zero.config(font=('Arial', btn_ssf1))
                self.clear_button.config(font=('Arial', btn_ssf1))
                self.confirm_button.config(font=('Arial', btn_ssf1))
            elif 935 < e.width <= 1160:  # Resets button and entry font sizes to default
                btn_dm = 50  # Button default font (method variable)
                self.answer_input.config(font=('Times New Roman', 55))
                self.one.config(font=('Arial', btn_dm))
                self.two.config(font=('Arial', btn_dm))
                self.three.config(font=('Arial', btn_dm))
                self.four.config(font=('Arial', btn_dm))
                self.five.config(font=('Arial', btn_dm))
                self.six.config(font=('Arial', btn_dm))
                self.seven.config(font=('Arial', btn_dm))
                self.eight.config(font=('Arial', btn_dm))
                self.nine.config(font=('Arial', btn_dm))
                self.zero.config(font=('Arial', btn_dm))
                self.clear_button.config(font=('Arial', btn_dm))
                self.confirm_button.config(font=('Arial', btn_dm))
            elif e.height <= 610 and e.width > 1160:
                btn_ssf = 45  # Button smallest font
                self.answer_input.config(font=('Times New Roman', 55))
                self.one.config(font=('Arial', btn_ssf))
                self.two.config(font=('Arial', btn_ssf))
                self.three.config(font=('Arial', btn_ssf))
                self.four.config(font=('Arial', btn_ssf))
                self.five.config(font=('Arial', btn_ssf))
                self.six.config(font=('Arial', btn_ssf))
                self.seven.config(font=('Arial', btn_ssf))
                self.eight.config(font=('Arial', btn_ssf))
                self.nine.config(font=('Arial', btn_ssf))
                self.zero.config(font=('Arial', btn_ssf))
                self.clear_button.config(font=('Arial', btn_ssf))
                self.confirm_button.config(font=('Arial', btn_ssf))
            elif 610 < e.height <= 645 and e.width > 1160:
                btn_dm = 50  # Button default font
                self.answer_input.config(font=('Times New Roman', 55))
                self.one.config(font=('Arial', btn_dm))
                self.two.config(font=('Arial', btn_dm))
                self.three.config(font=('Arial', btn_dm))
                self.four.config(font=('Arial', btn_dm))
                self.five.config(font=('Arial', btn_dm))
                self.six.config(font=('Arial', btn_dm))
                self.seven.config(font=('Arial', btn_dm))
                self.eight.config(font=('Arial', btn_dm))
                self.nine.config(font=('Arial', btn_dm))
                self.zero.config(font=('Arial', btn_dm))
                self.clear_button.config(font=('Arial', btn_dm))
                self.confirm_button.config(font=('Arial', btn_dm))
            elif 645 < e.height <= 700 and e.width > 1160:
                btn_m = 55  # Button medium font
                self.answer_input.config(font=('Times New Roman', 60))
                self.one.config(font=('Arial', btn_m))
                self.two.config(font=('Arial', btn_m))
                self.three.config(font=('Arial', btn_m))
                self.four.config(font=('Arial', btn_m))
                self.five.config(font=('Arial', btn_m))
                self.six.config(font=('Arial', btn_m))
                self.seven.config(font=('Arial', btn_m))
                self.eight.config(font=('Arial', btn_m))
                self.nine.config(font=('Arial', btn_m))
                self.zero.config(font=('Arial', btn_m))
                self.clear_button.config(font=('Arial', btn_m))
                self.confirm_button.config(font=('Arial', btn_m))
            elif 700 < e.height <= 715 and e.width > 1160:
                btn_l = 60  # Button large font
                self.answer_input.config(font=('Times New Roman', 60))
                self.one.config(font=('Arial', btn_l))
                self.two.config(font=('Arial', btn_l))
                self.three.config(font=('Arial', btn_l))
                self.four.config(font=('Arial', btn_l))
                self.five.config(font=('Arial', btn_l))
                self.six.config(font=('Arial', btn_l))
                self.seven.config(font=('Arial', btn_l))
                self.eight.config(font=('Arial', btn_l))
                self.nine.config(font=('Arial', btn_l))
                self.zero.config(font=('Arial', btn_l))
                self.clear_button.config(font=('Arial', btn_l))
                self.confirm_button.config(font=('Arial', btn_l))
            elif 740 < e.height <= 795 and e.width > 1160:
                btn_h = 65  # Button huge font
                self.answer_input.config(font=('Times New Roman', 60))
                self.one.config(font=('Arial', btn_h))
                self.two.config(font=('Arial', btn_h))
                self.three.config(font=('Arial', btn_h))
                self.four.config(font=('Arial', btn_h))
                self.five.config(font=('Arial', btn_h))
                self.six.config(font=('Arial', btn_h))
                self.seven.config(font=('Arial', btn_h))
                self.eight.config(font=('Arial', btn_h))
                self.nine.config(font=('Arial', btn_h))
                self.zero.config(font=('Arial', btn_h))
                self.clear_button.config(font=('Arial', btn_h))
                self.confirm_button.config(font=('Arial', btn_h))
            elif 795 < e.height <= 807 and e.width > 1160:
                btn_h = 65  # Button huge font
                self.answer_input.config(font=('Times New Roman', 66))
                self.one.config(font=('Arial', btn_h))
                self.two.config(font=('Arial', btn_h))
                self.three.config(font=('Arial', btn_h))
                self.four.config(font=('Arial', btn_h))
                self.five.config(font=('Arial', btn_h))
                self.six.config(font=('Arial', btn_h))
                self.seven.config(font=('Arial', btn_h))
                self.eight.config(font=('Arial', btn_h))
                self.nine.config(font=('Arial', btn_h))
                self.zero.config(font=('Arial', btn_h))
                self.clear_button.config(font=('Arial', btn_h))
                self.confirm_button.config(font=('Arial', btn_h))
            elif e.height > 807 and e.width > 1160:
                btn_h = 65  # Button huge font
                self.answer_input.config(font=('Times New Roman', 75))
                self.one.config(font=('Arial', btn_h))
                self.two.config(font=('Arial', btn_h))
                self.three.config(font=('Arial', btn_h))
                self.four.config(font=('Arial', btn_h))
                self.five.config(font=('Arial', btn_h))
                self.six.config(font=('Arial', btn_h))
                self.seven.config(font=('Arial', btn_h))
                self.eight.config(font=('Arial', btn_h))
                self.nine.config(font=('Arial', btn_h))
                self.zero.config(font=('Arial', btn_h))
                self.clear_button.config(font=('Arial', btn_h))
                self.confirm_button.config(font=('Arial', btn_h))

            # Main text resize
            if e.width <= 830:
                txt_ssf = 51  # Main text smallest font
                self.number_display.config(font=('Verdana', txt_ssf))
            elif 860 < e.width <= 935:
                txt_sf = 55  # Main text small font
                self.number_display.config(font=('Verdana', txt_sf))
            elif 935 < e.width <= 1010:
                txt_m = 61  # Main text medium font
                self.number_display.config(font=("Verdana", txt_m))
            elif 1010 < e.width <= 1160:
                txt_l = 65  # Main text large font
                self.number_display.config(font=("Verdana", txt_l))
            elif e.width > 1160:
                txt_d = 75  # Main text default font
                self.number_display.config(font=('Verdana', txt_d))

        self.bind("<Configure>", font_resize_main_page)

    def main_page_theme_update(self):
        self.config(bg=bg)
        self.buttons_container.config(bg=bg)
        self.number_display.config(bg=bg, fg=fg)
        self.answer_input.config(bg=bg, fg=fg, disabledbackground=bg, disabledforeground=fg)
        self.one.config(activeforeground=num_active_fg, activebackground=num_bg, disabledforeground=num_bg, bg=num_bg,
                        fg=num_fg)
        self.two.config(activeforeground=num_active_fg, activebackground=num_bg, disabledforeground=num_bg, bg=num_bg,
                        fg=num_fg)
        self.three.config(activeforeground=num_active_fg, activebackground=num_bg, disabledforeground=num_bg, bg=num_bg,
                          fg=num_fg)
        self.four.config(activeforeground=num_active_fg, activebackground=num_bg, disabledforeground=num_bg, bg=num_bg,
                         fg=num_fg)
        self.five.config(activeforeground=num_active_fg, activebackground=num_bg, disabledforeground=num_bg, bg=num_bg,
                         fg=num_fg)
        self.six.config(activeforeground=num_active_fg, activebackground=num_bg, disabledforeground=num_bg, bg=num_bg,
                        fg=num_fg)
        self.seven.config(activeforeground=num_active_fg, activebackground=num_bg, disabledforeground=num_bg, bg=num_bg,
                          fg=num_fg)
        self.eight.config(activeforeground=num_active_fg, activebackground=num_bg, disabledforeground=num_bg, bg=num_bg,
                          fg=num_fg)
        self.nine.config(activeforeground=num_active_fg, activebackground=num_bg, disabledforeground=num_bg, bg=num_bg,
                         fg=num_fg)
        self.zero.config(activeforeground=num_active_fg, activebackground=num_bg, disabledforeground=num_bg, bg=num_bg,
                         fg=num_fg)
        self.clear_button.config(bg=bg, fg=fg, activeforeground=active_fg, activebackground=bg, disabledforeground=bg)
        self.confirm_button.config(bg=bg, fg=fg, activeforeground=active_fg, activebackground=bg, disabledforeground=bg)


if __name__ == '__main__':
    MainAppBody().mainloop()
