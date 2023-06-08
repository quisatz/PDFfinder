import tkinter as tkk
from tkinter import Menu

from gui.feedback import PDFFinderFeedback
from gui.info import PDFFinderInfo


class Menubar(tkk.Menu):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.master.configure(menu=self)

        file = Menu(self, tearoff=0)
        tools = Menu(self, tearoff=0)
        help_ = Menu(self, tearoff=0)

        self.add_cascade(menu=file, label='Plik')
        self.add_cascade(menu=tools, label='Narzędzia')
        self.add_cascade(menu=help_, label='Pomoc')

        file.add_command(label='Nowe szukanie', command=self.master.new_search)
        file.add_separator()

        file.add_command(label='Wyjście', command=self.master.destroy)

        design = Menu(tools, tearoff=0)
        tools.add_cascade(menu=design, label='Wygląd')
        design.add_command(label='Jasny', command=lambda: print('Saving As...'))
        design.add_command(label='Ciemny', command=lambda: print('Saving All...'))

        language = Menu(tools, tearoff=0)
        tools.add_cascade(menu=language, label='Język')
        language.add_command(label='Polski', command=lambda: print('Saving As...'))
        language.add_command(label='English', command=lambda: print('Saving All...'))

        help_.add_command(label='Wyślij opinię', command=lambda: PDFFinderFeedback(self.master))
        help_.add_command(label='Pomoc', command=lambda: print('Opening File...'))
        help_.add_separator()
        help_.add_command(label='PDF finder - info', command=lambda: PDFFinderInfo(self.master))
