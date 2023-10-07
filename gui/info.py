import tkinter as tkk
from tkinter import ttk
from webbrowser import open_new
import pyperclip


class PDFFinderInfo(tkk.Toplevel):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.short = self.master.languages
        self.iconphoto(True, master.icon)
        self.withdraw()
        self.grab_set()
        self.title('PDF finder info')

        self.resizable(False, False)
        self.label = tkk.Label(self, width=5)
        self.label2 = tkk.Label(self, width=5)
        self.label2 = tkk.Label(self, width=5)
        self.label3 = tkk.Label(self, width=5)
        self.label4 = tkk.Label(self, width=5)
        self.label5 = tkk.Label(self, width=5)

        ttk.Label(self, text=self.short["txt_PDF_finder_information__PDF_finder_ver_1_0_(x64)"] , font='Helvetica 12 bold').grid(row=0, column=0, padx=10, pady=5, columnspan=3 ,sticky='')

        self.logo = tkk.PhotoImage(file='pict/me.png')
        ttk.Label(self, image=self.logo).grid(row=3, column=1, rowspan=5 , columnspan=4)
        ttk.Label(self, text=self.short["txt_PDF_finder_information__you_can_find_me_on"]).grid(row=3, column=0, padx=10, pady=0, sticky='sw')

        link1 = ttk.Label(self, text='Github', cursor="hand2")
        link1.grid(row=4, column=0, padx=10, pady=(10,5), sticky='sw')
        link1.bind("<Button-1>", lambda e: open_new("https://github.com/quisatz"))


        link2 = ttk.Label(self, text='Facebook', cursor="hand2")
        link2.grid(row=6, column=0, padx=10, pady=5, sticky='sw')
        link2.bind("<Button-1>", lambda e: open_new("https://www.facebook.com/NathanCelina"))

        link3 = ttk.Label(self, text='Linkedin', cursor="hand2")
        link3.grid(row=5, column=0, padx=10, pady=5, sticky='sw')
        link3.bind("<Button-1>",
                   lambda e: open_new("https://www.linkedin.com/in/borys-go%C5%82%C4%99biowski-02b883158/"))

        link4 = ttk.Label(self, text='Email', cursor="hand2")
        link4.grid(row=7, column=0, pady=5, padx=10, sticky='sw')
        link4.bind("<Button-1>", lambda e: open_new("mailto:borysgolebiowskipl@gmail.com"))

        button_window = ttk.Button(self, text=self.short["txt_PDF_finder_information__copy_email"])
        button_window.grid(row=7, column=0, columnspan=2 ,padx=(0,50) ,sticky='s')
        button_window.bind("<Button-1>", lambda e: pyperclip.copy('borysgolebiowskipl@gmail.com'))

        ttk.Label(self, text=self.short["txt_PDF_finder_information__copyright_c_Borys_Gołębiowski"], font='Helvetica 7').grid(
                                        row=8, column=0, padx=10,pady=(20 ,0) ,  sticky='sw')

        ttk.Label(self, text=self.short["txt_PDF_finder_information__PDF_finder_is_a_free_program_for_non-commercial_use"]
                  , font='Helvetica 7').grid(row=9,column=0, padx=10, pady=(0 ,10), columnspan=2 ,sticky='sw')

        link5 = ttk.Label(self, text=self.short["info"] , font='Helvetica 6' , cursor="hand2")
        link5.grid(row=10,column=0, padx=10, pady=(0 ,10), columnspan=2 ,)
        link5.bind("<Button-1>", lambda e: open_new("https://github.com/Arthan/"))
        self.window_update()

    def window_update(self):
        """Update window posiotion"""
        self.update_idletasks()
        self.center_window_position()
        self.deiconify()

    def center_window_position(self):
        window_width = self.winfo_reqwidth()
        window_height = self.winfo_reqheight()
        position_right = int(self.winfo_screenwidth() / 2 - window_width / 2)
        position_down = int(self.winfo_screenheight() / 2 - window_height / 2)
        self.geometry("+{}+{}".format(position_right, position_down))


if __name__ == '__main__':
    import os
    import tkinter as tk

    os.chdir("../")

    root = tk.Tk()
    feedback = PDFFinderInfo(root)
    root.mainloop()
