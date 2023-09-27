import requests
from bs4 import BeautifulSoup
import tkinter as tkk
from tkinter import ttk, messagebox


class PDFFinderFeedback(tkk.Toplevel):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.short = self.master.languages
        #bg_color = '#0088FF'
        self.iconphoto(True, master.icon)
        self.grab_set()
        self.withdraw()
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

        self.logo = tkk.PhotoImage(file='feedback.png')
        ttk.Label(self.frame_header, image=self.logo).grid(row=0, column=0, rowspan=2)
        # ttk.Label(self.frame_header, text=self.short["txt_feedback_screen__leave_your_opinion"], style='Header.TLabel').grid(
        #     row=0, column=1)

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

        self.update_idletasks()
        self.center_window_position()
        self.deiconify()

    def submit(self):

        headers = {
            'Referer': 'https://borysgolebiowskipl.wixsite.com/borys/_partials/wix-thunderbolt/dist/clientWorker.b151dd12.bundle.min.js',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            'Authorization': 'IjLnBgbcij6t1fgckD_Vcs3vEYKl5nvXb5Nfma1ekug.eyJpbnN0YW5jZUlkIjoiMWFlNDQ4ODUtNmQ0Ny00MjFkLWFiZDktNzBlNmExNzdkZGI5IiwiYXBwRGVmSWQiOiIxNGNlMTIxNC1iMjc4LWE3ZTQtMTM3My0wMGNlYmQxYmVmN2MiLCJtZXRhU2l0ZUlkIjoiMDhkZDMyODAtNTRlOS00ZTA5LWFiZTUtZjJiMjgxMzAxNWQ3Iiwic2lnbkRhdGUiOiIyMDIzLTA5LTI3VDE1OjM5OjU3LjIzOFoiLCJkZW1vTW9kZSI6ZmFsc2UsIm9yaWdpbkluc3RhbmNlSWQiOiJjNTFhMmRlNC0xZTBmLTQxYzMtYTQ0ZS0xMDY3N2NhMjE0MjMiLCJhaWQiOiJhYTUxMGM3My0yYTYyLTQ4ZGEtYjQwNy0xMjFkMzMwYTM1MDIiLCJiaVRva2VuIjoiMTIzOTdhMDUtMzlhZS0wYzE0LTAwM2MtODI1NDIwNDdjODZlIiwic2l0ZU93bmVySWQiOiJhYTIwMTdkNS1mMzQyLTQ2OTItOTQ0OC1lYWNlN2I4YTFlYTMifQ',
            'X-Wix-Client-Artifact-Id': 'wix-form-builder',
            'Content-Type': 'application/json',
        }

        json_data = {
            'formProperties': {
                'formName': 'Contacts Form',
                'formId': 'comp-jxabkofu',
            },
            'emailConfig': {
                'sendToOwnerAndEmails': {
                    'emailIds': [],
                },
            },
            'viewMode': 'Site',
            'fields': [
                {
                    'fieldId': 'comp-jxabkog6',
                    'label': 'Name',
                    'lastName': {
                        'value': self.entry_name.get(),
                    },
                },
                {
                    'fieldId': 'comp-jxabkogd',
                    'label': 'Email',
                    'email': {
                        'value': self.entry_email.get(),
                        'tag': 'main',
                    },
                },
                {
                    'fieldId': 'comp-jxabkogj',
                    'label': 'Subject',
                    'custom': {
                        'value': {
                            'string': 'Comments from PDFfinder',
                        },
                        'customFieldId': '0f8b898c-3d5a-439d-b101-b4a7d9e5d678',
                    },
                },
                {
                    'fieldId': 'comp-jxabkogq',
                    'label': 'Message',
                    'custom': {
                        'value': {
                            'string': self.text_comments.get(1.0, 'end'),
                        },
                        'customFieldId': '9b3942c4-5ad2-4be2-aef5-df9f55c3a6bf',
                    },
                },
            ],
            'labelKeys': [
                'contacts.contacted-me',
                'custom.contacts-form',
            ],
        }

        response = requests.post(
            'https://borysgolebiowskipl.wixsite.com/borys/_api/wix-forms/v1/submit-form',
            headers=headers,
            json=json_data,
        )





        print('Name: {}'.format(self.entry_name.get()))
        print('Email: {}'.format(self.entry_email.get()))
        print('Comments: {}'.format(self.text_comments.get(1.0, 'end')))


        soup = BeautifulSoup(response.text, features='html.parser')
        print('soup.text:', soup.text)
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
        self.entry_name.delete(0, 'end')
        self.entry_email.delete(0, 'end')
        self.text_comments.delete(1.0, 'end')

    def center_window_position(self):
        window_width = self.winfo_reqwidth()
        window_height = self.winfo_reqheight()
        position_right = int(self.winfo_screenwidth() / 2 - window_width / 2)
        position_down = int(self.winfo_screenheight() / 2 - window_height / 2)
        self.geometry("+{}+{}".format(position_right, position_down))
