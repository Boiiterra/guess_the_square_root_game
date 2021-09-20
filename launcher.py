from tkinter.messagebox import askyesno, showinfo
from tkinter import Tk, Toplevel, Button, Label
from tkinter.ttk import Progressbar
from win32api import ShellExecute
from PIL import Image, ImageTk
from os import path, makedirs
from threading import Thread
from requests import get

__version__ = '0.21'
_AppName_ = 'Guess the square root game launcher'

url = "https://github.com/TerraBoii/guess_the_square_root_game/raw/main/updates/squarerootgame_setup.exe"
file_name = url.split('/')[-1].replace(" ", "_")
file_path = path.join("setup", file_name)

class UpdateManager(Toplevel):
    def __init__(self, parent):
        Toplevel.__init__(self, parent)

        self.transient(parent)
        self.attributes("-disabled", True)
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
            self.attributes("-disabled", False)
            install_update()

        self.progressbar = Progressbar(self,
                                       orient='horizontal',
                                       length=200,
                                       mode='determinate',
                                       value=0,
                                       maximum=0)
        self.progressbar.place(relx=0.5, rely=0.5, anchor="center")
        self.install_btn = Button(self, text='Wait!', state="disabled", command=install_update)
        self.install_btn.place(x=-83, relx=1.0, y=-33, rely=1.0)

        self.t1 = Thread(target=start_update_manager)
        self.t1.start()

tmp = Tk()
tmp.geometry(f"{650}x{400}+{int((tmp.winfo_screenwidth()-650)/2)}+{int((tmp.winfo_screenheight()-400)/2)}")
tmp.withdraw()

try:
    response = get(
        'https://raw.githubusercontent.com/TerraBoii/guess_the_square_root_game/main/version.txt')
    data = response.text

    if float(data) > float(__version__):
        showinfo(title='Software Update', message="Update Available!")
        get_update = askyesno('Update!', f'{_AppName_} {__version__} needs to update to version {data}')
        if get_update is True:
            UpdateManager(tmp)
        elif get_update is False:
            tmp.destroy()
            ShellExecute(0, 'open', 'binaries\\Guess the square root.exe', None, None, 10)
    else:
        tmp.destroy()
        ShellExecute(0, 'open', 'binaries\\Guess the square root.exe', None, None, 10)
except Exception:
    tmp.destroy()
    ShellExecute(0, 'open', 'binaries\\Guess the square root.exe', None, None, 10)
tmp.mainloop()
