from tkinter import ttk
import tkinter as tkk

class FrameNoResultsFound(ttk.Frame):
    def __init__(self,  master  ,flag ,  **kw):
        super().__init__(master   ,**kw)
        self.config(relief=tkk.SUNKEN)
        self.short = self.master.languages
        self.config(height=50, width=400)

        if flag == 'frame_no_Files_found':
            nothing = ttk.Label(self, text=self.short["no_files_found_in_directory"], font=('Arial', 20))
        else:
            nothing = ttk.Label(self, text=self.short["txt_no_results_found"], font=('Arial', 20))
        nothing.grid(row=5, column=0, pady=50, padx=100, columnspan=2)
