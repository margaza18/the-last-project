from tkinter import *
from tkinter.filedialog import askopenfilename


def open_window_dialog():
    # we don't want a full GUI, so keep the root window from appearing
    Tk().withdraw()
    filename = askopenfilename(filetypes=[("Excel files", ".xlsx .xls")])
    return filename

