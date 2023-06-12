import tkinter as tkk
from tkinter import ttk, messagebox


class PDFFinderFeedback(tkk.Toplevel):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.short = self.master.languages
        #bg_color = '#0088FF'

        self.grab_set()

        self.title(self.short["txt_feedback_screen_feedback"])
        self.resizable(False, False)

        #self.configure(bg=bg_color)

        self.frame_header = ttk.Frame(self)
        self.frame_header.pack()

        self.frame_header.style = ttk.Style()
        # self.frame_header.style.configure('TFrame', background='#FFFFFF')
        # self.frame_header.style.configure('TButton', background='#FFFFFF')
        # self.frame_header.style.configure('TLabel', background='#FFFFFF', font=('Arial', 10))
        self.frame_header.style.configure('Header.TLabel', font=('Arial', 14))

        self.logo = tkk.PhotoImage(file='logoOpnie.png')
        ttk.Label(self.frame_header, image=self.logo).grid(row=0, column=0, rowspan=2)
        ttk.Label(self.frame_header, text=self.short["txt_feedback_screen__leave_your_opinion"], style='Header.TLabel').grid(
            row=0, column=1)

        self.frame_content = ttk.Frame(self)
        self.frame_content.pack()

        ttk.Label(self.frame_content, text=self.short["txt_feedback_screen__name"]).grid(row=0, column=0, padx=5, sticky='sw')
        ttk.Label(self.frame_content, text=self.short["txt_feedback_screen__email"]).grid(row=0, column=1, padx=5, sticky='sw')
        ttk.Label(self.frame_content, text=self.short["txt_feedback_screen__comment"]).grid(row=2, column=0, padx=5, sticky='sw')

        self.entry_name = ttk.Entry(self.frame_content, width=24, font=('Arial', 10))
        self.entry_email = ttk.Entry(self.frame_content, width=24, font=('Arial', 10))
        self.text_comments = tkk.Text(self.frame_content, width=50, height=10, font=('Arial', 10))

        self.entry_name.grid(row=1, column=0, padx=5)
        self.entry_email.grid(row=1, column=1, padx=5)
        self.text_comments.grid(row=3, column=0, columnspan=2, padx=5)

        ttk.Button(self.frame_content, text=self.short["txt_feedback_screen__send"],
                   command=self.submit).grid(row=4, column=0, padx=5, pady=5, sticky='e')
        ttk.Button(self.frame_content, text=self.short["txt_feedback_screen__clear"],
                   command=self.clear).grid(row=4, column=1, padx=5, pady=5, sticky='w')

    def submit(self):
        print('Name: {}'.format(self.entry_name.get()))
        print('Email: {}'.format(self.entry_email.get()))
        print('Comments: {}'.format(self.text_comments.get(1.0, 'end')))
        self.clear()
        messagebox.showinfo(title="txt_feedback_screen_feedback", message=self.short["txt_feedback_screen__comments_submitted"], parent=self)

    def clear(self):
        self.entry_name.delete(0, 'end')
        self.entry_email.delete(0, 'end')
        self.text_comments.delete(1.0, 'end')
