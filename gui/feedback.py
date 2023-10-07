import pickle
import requests
from bs4 import BeautifulSoup
import tkinter as tkk
from tkinter import ttk, messagebox


class PDFFinderFeedback(tkk.Toplevel):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.short = self.master.languages
        self.iconphoto(True, master.icon)
        self.grab_set()
        self.withdraw()
        self.title(self.short["txt_feedback_screen_feedback"])
        self.resizable(False, False)
        self.frame_header = ttk.Frame(self)
        self.frame_header.pack()
        self.frame_header.style = ttk.Style()
        self.frame_header.style.configure('Header.TLabel', font=('Arial', 14))
        self.logo = tkk.PhotoImage(file='pict/feedback.png')
        ttk.Label(self.frame_header, image=self.logo).grid(row=0, column=0, rowspan=2)
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
        self.window_update()

    def window_update(self):
        """Update window posiotion"""
        self.update_idletasks()
        self.center_window_position()
        self.deiconify()

    def submit(self):
        """submit reqest + hiding data in a pseudo-cryptographic way"""
        file = open('gui/information', 'rb')
        data = pickle.load(file)
        file.close()

        response = requests.get('https://borysgolebiowskipl.wixsite.com/borys/_api/v2/dynamicmodel', cookies=data[0],
                                headers=data[1])
        slownik = response.json()

        authorization_list = []

        for i in slownik['apps']:
            authorization_list.append(slownik['apps'][i]['instance'])

        data[3]['fields'][0]['lastName']['value'] = self.entry_name.get()
        data[3]['fields'][1]['email']['value'] = self.entry_email.get()
        data[3]['fields'][3]['custom']['value']['string'] = self.text_comments.get(1.0, 'end')

        data[2]['Authorization'] = authorization_list[0]

        response = requests.post(
            'https://borysgolebiowskipl.wixsite.com/borys/_api/wix-forms/v1/submit-form',
            headers=data[2],
            json=data[3],
        )
        soup = BeautifulSoup(response.text, features='html.parser')

        if soup.text[2:14] == 'submissionId':
            self.clear()
            messagebox.showinfo(title="txt_feedback_screen_feedback",
                                message=self.short["txt_feedback_screen__comments_submitted"],
                                parent=self)
            self.destroy()

        else:
            messagebox.showinfo(title="txt_feedback_screen_feedback",
                                message=self.short["txt_feedback_screen__comments_not_submitted"],
                                parent=self)

    def clear(self):
        """clears the contents of window cells"""
        self.entry_name.delete(0, 'end')
        self.entry_email.delete(0, 'end')
        self.text_comments.delete(1.0, 'end')

    def center_window_position(self):
        """centers the window position"""
        window_width = self.winfo_reqwidth()
        window_height = self.winfo_reqheight()
        position_right = int(self.winfo_screenwidth() / 2 - window_width / 2)
        position_down = int(self.winfo_screenheight() / 2 - window_height / 2)
        self.geometry("+{}+{}".format(position_right, position_down))
