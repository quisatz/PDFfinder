from tkinter import ttk
import tkinter as tkk

class FrameNoResultsFound(tkk.Toplevel):
    def __init__(self,  master  ,flag , *arg , **kw):
        super().__init__(master   ,*arg , **kw)
        self.config(relief=tkk.SUNKEN)
        self.short = self.master.languages
        self.iconphoto(True, master.icon)
        self.config(height=50, width=400)
        self.buttom_ok = ttk.Button(self, text="ok", command=self.destroy)
        self.grab_set()
        self.withdraw()
        self.resizable(False, False)

        if flag == 'frame_no_Files_found':
            ttk.Label(self, text=self.short["no_files_found_in_directory"], font=('Arial', 12)).pack(pady=10, padx=10)
            self.buttom_ok.pack(pady=10)


        elif flag == 'txt_results_found':
            ttk.Label(self, text=self.short["txt_results_found"], font=('Arial', 12)).pack(pady=10, padx=10)
            self.buttom_ok.pack(pady=10)


        else:
            ttk.Label(self, text=self.short["txt_no_results_found"], font=('Arial', 12)).pack(pady=10, padx=10)
            self.buttom_ok.pack(pady=10)
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