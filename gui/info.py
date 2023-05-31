import tkinter as tkk
from tkinter import ttk


class PDFFinderInfo:
    def __init__(self, root):
        window = tkk.Toplevel(root)  # tworze nowe okno ktore jest dzieckiem root
        window.title('PDF finder info')  # nazwa okna

        window_width = root.winfo_reqwidth()
        window_height = root.winfo_reqheight()
        position_right = int(root.winfo_screenwidth() / 2 - window_width / 2)
        position_down = int(root.winfo_screenheight() / 2 - window_height / 2)
        window.geometry("+{}+{}".format(position_right, position_down))

        window.resizable(False, False)
        self.label = tkk.Label(window, width=5)
        self.label2 = tkk.Label(window, width=5)
        self.label2 = tkk.Label(window, width=5)
        self.label3 = tkk.Label(window, width=5)
        self.label4 = tkk.Label(window, width=5)
        self.label5 = tkk.Label(window, width=5)

        ttk.Label(window, text='PdfFinder ver 1.0 (x64):').grid(row=1, column=1, padx=10, pady=5, sticky='sw')
        ttk.Label(window, text='Copyright (c) Borys Gołębiowski:').grid(row=2, column=1, padx=10, sticky='sw')

        ttk.Label(window, image=root.logo).grid(row=2, column=2, rowspan=2)

        ttk.Label(window, text='You can find me on:').grid(row=3, column=1, padx=10, pady=5, sticky='sw')

        link1 = ttk.Label(window, text='Facebook:', cursor="hand2")
        link1.grid(row=4, column=1, padx=10, pady=10, sticky='sw')
        link1.bind("<Button-1>", lambda e: root.callback("https://www.facebook.com/NathanCelina"))

        link2 = ttk.Label(window, text='Linkedin', cursor="hand2")
        link2.grid(row=5, column=1, padx=10, pady=10, sticky='sw')
        link2.bind("<Button-1>",
                   lambda e: root.callback("https://www.linkedin.com/in/borys-go%C5%82%C4%99biowski-02b883158/"))

        link3 = ttk.Label(window, text='Email', cursor="hand2")
        link3.grid(row=6, column=1, pady=10, padx=10, sticky='sw')
        link3.bind("<Button-1>", lambda e: root.callback("mailto:borysgolebiowskipl@gmail.com"))

        button_window = ttk.Button(window, text="Copy email")
        button_window.grid(row=6, column=2, sticky='sw')

        ttk.Label(window, text='PdfFinder jest programem darmowym').grid(row=7, column=1, padx=10, pady=30, sticky='sw')
