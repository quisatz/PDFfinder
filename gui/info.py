import tkinter as tkk
from tkinter import ttk
from webbrowser import open_new
import pyperclip


class PDFFinderInfo(tkk.Toplevel):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.short = self.master.languages
        self.iconbitmap("app_icon.ico")
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

        ttk.Label(self, text=self.short["txt_PDF_finder_information__PDF_finder_ver_1_0_(x64)"]).grid(row=1, column=1, padx=10, pady=5, sticky='sw')
        ttk.Label(self, text=self.short["txt_PDF_finder_information__copyright_c_Borys_Gołębiowski"]).grid(row=2, column=1, padx=10, sticky='sw')

        self.logo = tkk.PhotoImage(file='me.png')
        ttk.Label(self, image=self.logo).grid(row=2, column=2, rowspan=2)

        ttk.Label(self, text=self.short["txt_PDF_finder_information__you_can_find_me_on"]).grid(row=3, column=1, padx=10, pady=5, sticky='sw')

        link1 = ttk.Label(self, text='Facebook:', cursor="hand2")
        link1.grid(row=4, column=1, padx=10, pady=10, sticky='sw')
        link1.bind("<Button-1>", lambda e: open_new("https://www.facebook.com/NathanCelina"))

        link2 = ttk.Label(self, text='Linkedin', cursor="hand2")
        link2.grid(row=5, column=1, padx=10, pady=10, sticky='sw')
        link2.bind("<Button-1>",
                   lambda e: open_new("https://www.linkedin.com/in/borys-go%C5%82%C4%99biowski-02b883158/"))

        link3 = ttk.Label(self, text='Email', cursor="hand2")
        link3.grid(row=6, column=1, pady=10, padx=10, sticky='sw')
        link3.bind("<Button-1>", lambda e: open_new("mailto:borysgolebiowskipl@gmail.com"))

        button_window = ttk.Button(self, text=self.short["txt_PDF_finder_information__copy_email"])
        button_window.grid(row=6, column=2, sticky='sw')
        button_window.bind("<Button-1>", lambda e: pyperclip.copy('borysgolebiowskipl@gmail.com'))

        ttk.Label(self, text=self.short["txt_PDF_finder_information__PDF_finder_is_a_free_program_for_non-commercial_use"]
                  ).grid(row=7,column=1, padx=10, pady=30, sticky='sw')

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
