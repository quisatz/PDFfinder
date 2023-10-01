import tkinter as tkk
from tkinter import ttk
from webbrowser import open_new
import sys
import subprocess



class PDFFinderHow(tkk.Toplevel):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.short = self.master.languages
        self.iconphoto(True, master.icon)
        self.withdraw()
        self.grab_set()
        self.title('How')

        self.resizable(False, False)
        self.label = tkk.Label(self, width=5)
        self.label2 = tkk.Label(self, width=5)
        self.label2 = tkk.Label(self, width=5)
        self.label3 = tkk.Label(self, width=5)
        self.label4 = tkk.Label(self, width=5)
        self.label5 = tkk.Label(self, width=5)

        ttk.Label(self, text=self.short["txt_PDF_finder_information__PDF_finder_ver_1_0_(x64)"] , font='Helvetica 12 bold').grid(row=0, column=0, padx=10, pady=(5,20), columnspan=2 ,sticky='')



        link1 = ttk.Label(self, text=self.short["user_manual"], font=('Arial',9,'underline'), cursor="hand2")
        link1.grid(row=3, column=0, padx=10, pady=5, sticky='sw')
        link1.bind("<Button-1>", lambda e: self.default_open('pict/Demonstration.gif'))


        link3 = ttk.Label(self, text=self.short["demonstration_of_the_program_on_youtube"],  font=('Arial',9,'underline') , cursor="hand2")
        link3.grid(row=6, column=0, pady=(10,10), padx=10, sticky='sw')
        link3.bind("<Button-1>", lambda e: open_new("https://www.youtube.com/watch?v=LrCqMymx5WE"))




        self.update_idletasks()
        self.center_window_position()
        self.deiconify()

    def center_window_position(self):
        window_width = self.winfo_reqwidth()
        window_height = self.winfo_reqheight()
        position_right = int(self.winfo_screenwidth() / 2 - window_width / 2)
        position_down = int(self.winfo_screenheight() / 2 - window_height / 2)
        self.geometry("+{}+{}".format(position_right, position_down))





    def default_open(self , something_to_open):
        """
        Open given file with default user program.
        """

        if sys.platform.startswith('linux'):
            ret_code = subprocess.call(['xdg-open', something_to_open])

        elif sys.platform.startswith('darwin'):
            ret_code = subprocess.call(['open', something_to_open])

        elif sys.platform.startswith('win'):
            ret_code = subprocess.call(['start', something_to_open], shell=True)


if __name__ == '__main__':
    import os
    import tkinter as tk

    os.chdir("../")

    root = tk.Tk()
    feedback = PDFFinderHow(root)
    root.mainloop()
