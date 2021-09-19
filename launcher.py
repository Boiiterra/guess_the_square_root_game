from PIL import ImageTk, Image, ImageOps
from tkinter import font, Menu, Frame, Toplevel, Label, Tk, Button, CENTER, LEFT, NORMAL, TOP, DISABLED, SOLID
from tkinter.messagebox import showinfo, askyesno
from tkinter.ttk import Progressbar
from threading import Thread
from os import makedirs, path 
from webbrowser import open_new_tab
from requests import get
from win32api import ShellExecute

__author__ = 'TerraBoii'
__copyright__ = 'Copyright (C) 2021, TerraBoii'
__credits__ = ['TerraBoii']
__license__ = 'The MIT License (MIT)'
__version__ = '0.192'
__maintainer__ = 'TerraBoii'
__email__ = 'terraboii.ytgames@gmail.com'
__status__ = 'Beta'

_AppName_ = 'Guess the square root game launcher'


class ToolTip:

    def __init__(self, widget):
        self.widget = widget
        self.tip_window = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        """Display text in tooltip window"""
        if self.tip_window or not text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 57
        y = y + cy + self.widget.winfo_rooty() + 27
        self.tip_window = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(tw, text=text, justify=LEFT,
                      background="#ffffe0", relief=SOLID, borderwidth=1,
                      font=("Tahoma", "10", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tip_window
        self.tip_window = None
        if tw:
            tw.destroy()


def CreateToolTip(widget, text):
    tool_tip = ToolTip(widget)

    def enter(event):
        tool_tip.showtip(text)

    def leave(event):
        tool_tip.hidetip()

    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)


class Main:
    def __init__(self, parent):
        def check_updates():
            try:
                # -- Online Version File
                response = get(
                    'https://raw.githubusercontent.com/TerraBoii/guess_the_square_root_game/main/version.txt')
                data = response.text

                if float(data) > float(__version__):
                    showinfo('Software Update', 'Update Available!')
                    mb1 = askyesno('Update!', f'{_AppName_} {__version__} needs to update to version {data}')
                    if mb1 is True:
                        open_new_tab('https://github.com/TerraBoii/guess_the_square_root_game/raw' 
                                     '/main/updates/squarerootgame_setup.exe')
                        parent.destroy()
                    else:
                        pass
                else:
                    showinfo('Software Update', 'No Updates are Available.')
            except Exception as e:
                showinfo('Software Update', 'Unable to Check for Update, Error:' + str(e))

        def about_me():
            DisplayAboutMe(parent)

        def run_binary():
            ShellExecute(0, 'open', 'binaries\\Guess the square root.exe', None, None, 10)
            parent.destroy()

        def update_using_manager():
            try:
                # -- Online Version File
                response = get(
                    'https://raw.githubusercontent.com/TerraBoii/guess_the_square_root_game/main/version.txt')
                data = response.text

                if float(data) > float(__version__):
                    showinfo('Software Update', 'Update Available!')
                    mb2 = askyesno('Update!', f'{_AppName_} {__version__} needs to update to version {data}')
                    if mb2 is True:
                        UpdateManager(parent)
                    elif mb2 == 'No':
                        pass
                else:
                    showinfo('Software Update', 'No Updates are Available.')
            except Exception as e:
                print('The Error is here!')
                showinfo('Software Update', 'Unable to Check for Update, Error:' + str(e))

        menu_bar = Menu(parent)
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label='Exit', command=parent.destroy)
        menu_bar.add_cascade(label='File', menu=file_menu)
        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label='About', command=about_me)
        menu_bar.add_cascade(label='Help', menu=help_menu)
        parent.config(menu=menu_bar)

        buttons_frame = Frame(parent)
        buttons_frame.pack(side='top', fill='x')

        self._exit = ImageTk.PhotoImage(Image.open('images/exit.png'))

        exit_button = Button(buttons_frame, image=self._exit, command=parent.destroy, bg='#bababa',
                             activebackground='#bababa')
        exit_button.pack(side=LEFT, padx=1, pady=1)
        exit_button.image = self._exit

        check_btn = Button(parent, text='Check for Updates', command=check_updates, bg='#bababa',
                           activebackground='#bababa')
        check_btn.place(relx=0.5, rely=0.5, anchor=CENTER)

        run_app = Button(parent, text='Open application', command=run_binary, bg='#bababa',
                         activebackground='#bababa')
        run_app.place(x=20, y=60)

        button4 = Button(parent, text='UpdateManager', command=update_using_manager, bg='#bababa',
                         activebackground='#bababa')
        button4.place(x=-200, relx=1.0, y=60)


class UpdateManager(Toplevel):
    def __init__(self, parent):
        Toplevel.__init__(self, parent)

        self.transient(parent)
        self.result = None
        self.grab_set()
        w = 350
        h = 200
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.geometry('{0}x{1}+{2}+{3}'.format(w, h, int(x), int(y)))
        self.resizable(width=False, height=False)
        self.title('Update Manager')
        self.wm_iconbitmap('images/Contact.ico')

        image = Image.open('images/update_manager.jpg')
        photo = ImageTk.PhotoImage(image)
        label = Label(self, image=photo)
        label.image = photo
        label.pack()

        def install_update():
            url = "https://github.com/TerraBoii/guess_the_square_root_game/raw/main/updates/squarerootgame_setup.exe"
            file_name = url.split('/')[-1].replace(" ", "_")
            file_path = path.join("setup", file_name)
            ShellExecute(0, 'open', file_path, None, None, 10)
            parent.destroy()

        def start_update_manager():
            url = "https://github.com/TerraBoii/guess_the_square_root_game/raw/main/updates/squarerootgame_setup.exe"
            dest_folder = "setup"
            file_name = url.split('/')[-1].replace(" ", "_")
            file_path = path.join(dest_folder, file_name)
            if not path.exists(dest_folder):
                makedirs(dest_folder)  # create folder if it does not exist
            with get(url=url, stream=True) as r:
                self.progressbar['maximum'] = int(r.headers.get('Content-Length'))
                r.raise_for_status()
                with open(file_path, 'wb') as f:
                    for chunk in r.iter_content(chunk_size=4096):
                        if chunk:  # filter out keep-alive new chunks
                            f.write(chunk)
                            self.progressbar['value'] += 4096
            self.button1.config(text='Install', state=NORMAL)

        self.progressbar = Progressbar(self,
                                       orient='horizontal',
                                       length=200,
                                       mode='determinate',
                                       value=0,
                                       maximum=0)
        self.progressbar.place(relx=0.5, rely=0.5, anchor=CENTER)
        self.button1 = Button(self, text='Wait!', state=DISABLED, command=install_update)
        self.button1.place(x=-83, relx=1.0, y=-33, rely=1.0)

        self.t1 = Thread(target=start_update_manager)
        self.t1.start()


class DisplayAboutMe(Toplevel):
    def __init__(self, parent):
        Toplevel.__init__(self, parent)

        self.transient(parent)
        self.result = None
        self.grab_set()
        w = 285
        h = 273
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.geometry('{0}x{1}+{2}+{3}'.format(w, h, int(x), int(y)))
        self.resizable(width=False, height=False)
        self.title('About')
        self.wm_iconbitmap('images/Contact.ico')
        self.config(bg='#bababa')

        self.image = Image.open('images/TerraBoii_pp.png')
        self.size = (100, 100)
        self.thumb = ImageOps.fit(self.image, self.size, Image.ANTIALIAS)
        self.photo = ImageTk.PhotoImage(self.thumb)
        logo_label = Label(self, image=self.photo, bg="#bababa", cursor='hand2')
        logo_label.pack(side=TOP, pady=10)

        f1 = Frame(self, bg='#bababa')
        f1.pack()
        f2 = Frame(self, bg='#bababa')
        f2.pack(pady=10)
        f3 = Frame(f2, bg='#bababa')
        f3.pack()

        def call_link(*args):
            open_new_tab('https://github.com/TerraBoii')

        Label(f1, text=_AppName_ + ' ' + str(__version__), bg='#bababa').pack()
        Label(f1, text='Copyright (C) 2021 TerraBoii', bg='#bababa').pack()
        Label(f1, text='All rights reserved', bg='#bababa').pack()

        f = font.Font(size=10, slant='italic', underline=True)
        link_container = Label(f3, text='TerraBoii', font=f, cursor='hand2')
        link_container.config(fg='Blue', bg='#bababa')
        link_container.pack(side=LEFT)
        link_container.bind('<Button-1>', call_link)
        CreateToolTip(link_container, text="https://github.com/TerraBoii")
        logo_label.bind('<Button-1>', call_link)
        CreateToolTip(logo_label, text="https://github.com/TerraBoii")
        Button(self, text='OK', command=self.destroy, bg="#5e5e5e", activeforeground="#404040",
               activebackground="#5e5e5e").pack(pady=5)


def main():
    root = Tk()
    root.title(_AppName_ + ' ' + str(__version__))
    w = 650
    h = 400
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw - w) / 2
    y = (sh - h) / 2
    root.geometry('{0}x{1}+{2}+{3}'.format(w, h, int(x), int(y)))
    root.resizable(width=False, height=False)
    root.wm_iconbitmap('images/Contact.ico')
    Main(root)
    root.mainloop()


if __name__ == '__main__':
    main()
