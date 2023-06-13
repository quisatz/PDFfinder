import tkinter as tkk
from tkinter import Menu

from gui.feedback import PDFFinderFeedback
from gui.info import PDFFinderInfo


class Menubar(tkk.Menu):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.short = self.master.languages
        self.master.configure(menu=self)

        file = Menu(self, tearoff=0)
        tools = Menu(self, tearoff=0)
        help_ = Menu(self, tearoff=0)

        self.add_cascade(menu=file, label=self.short["txt_menu__file"])
        self.add_cascade(menu=tools, label=self.short["txt_menu__tools"])
        self.add_cascade(menu=help_, label=self.short["txt_menu__help"])

        file.add_command(label=self.short["txt_menu__new search"], command=self.master.new_search)
        file.add_separator()

        file.add_command(label=self.short["txt_menu__exit"], command=self.master.destroy)

        design = Menu(tools, tearoff=0)
        tools.add_cascade(menu=design, label=self.short["txt_menu__appearance"])
        design.add_command(label=self.short["txt_menu__light"], command=lambda: print('Saving As...'))
        design.add_command(label=self.short["txt_menu__dark"], command=lambda: print('Saving All...'))

        language = Menu(tools, tearoff=0)
        tools.add_cascade(menu=language, label=self.short["txt_menu__language"])
        language.add_command(label=self.short["txt_menu__polish"], command=lambda: self.master.change_lang('language\\pl_PL' , 1))
        language.add_command(label=self.short["txt_menu__english"], command=lambda: self.master.change_lang('language\\en_US' , 1))

        help_.add_command(label=self.short["txt_menu_help__send_feedback"], command=lambda: PDFFinderFeedback(self.master))
        help_.add_command(label=self.short["txt_menu__how_to_use"], command=lambda: print('Opening File...'))
        help_.add_separator()
        help_.add_command(label=self.short["txt_menu__PDF_finder_information"], command=lambda: PDFFinderInfo(self.master))
