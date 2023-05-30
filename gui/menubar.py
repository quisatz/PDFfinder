import tkinter as tkk
from tkinter import Menu


def create_menubar(self):
    self.menubar = tkk.Menu(self.root)
    self.root.configure(menu=self.menubar)

    file = Menu(self.menubar, tearoff=0)
    tools = Menu(self.menubar, tearoff=0)
    help_ = Menu(self.menubar, tearoff=0)

    self.menubar.add_cascade(menu=file, label='Plik')
    self.menubar.add_cascade(menu=tools, label='Narzędzia')
    self.menubar.add_cascade(menu=help_, label='Pomoc')

    file.add_command(label='Nowe szukanie', command=self.new_search)
    file.add_separator()

    file.add_command(label='Wyjście', command=self.root.destroy)

    design = Menu(tools, tearoff=0)
    tools.add_cascade(menu=design, label='Wygląd')
    design.add_command(label='Jasny', command=lambda: print('Saving As...'))
    design.add_command(label='Ciemny', command=lambda: print('Saving All...'))

    language = Menu(tools, tearoff=0)
    tools.add_cascade(menu=language, label='Język')
    language.add_command(label='Polski', command=lambda: print('Saving As...'))
    language.add_command(label='English', command=lambda: print('Saving All...'))

    help_.add_command(label='Wyślij opinię', command=lambda: self.send_feedback())
    help_.add_command(label='Pomoc', command=lambda: print('Opening File...'))
    help_.add_separator()
    help_.add_command(label='PDF finder - info', command=lambda: self.PDF_finder_info())
