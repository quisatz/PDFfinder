from tkinter import ttk


class FrameNoResultsFound(ttk.Frame):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.config(height=50, width=400)
        nothing = ttk.Label(self, text='Nie znaleziono żadnych wyników!', font=('Arial', 20))
        nothing.grid(row=5, column=0, pady=50, padx=100, columnspan=2)
