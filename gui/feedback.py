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

        cookies = {
            'svSession': '2396594eac4e78a8f3e539b9554617d38bb02a315f272702cd9ad3cf4676037b91660634cf9fe02e232e0ac79d3be90d1e60994d53964e647acf431e4f798bcdce9a7f8d3e16c027af28bb0538bfde4c328007f22dda61ba1a95ae3eb862e5bcc4ee86258d3e2a1a877cb452cebdeca0f08ba019d731afa2fc78c8a9b0696afba31176df2ab7e392bff671756e774370',
            'TS018a76eb': '01d72e6d1628bdb066ddcf4e45958783a51edc72a3c07ad936c1927ceb306d1eae9f716b023fd348acc74c00ae480532b7a06e07d4',
            'ssr-caching': 'cache#desc=hit#varnish=hit#dc#desc=84_g',
            'XSRF-TOKEN': '1696004164|3U0gAOjerBAO',
            'hs': '2032116472',
            'bSession': '1d25d1f4-7c96-40ff-a1d4-144320c23297|2',
        }

        headers = {
            'authority': 'borysgolebiowskipl.wixsite.com',
            'accept': '*/*',
            'accept-language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7',
            'cache-control': 'no-cache',
            # 'cookie': 'svSession=2396594eac4e78a8f3e539b9554617d38bb02a315f272702cd9ad3cf4676037b91660634cf9fe02e232e0ac79d3be90d1e60994d53964e647acf431e4f798bcdce9a7f8d3e16c027af28bb0538bfde4c328007f22dda61ba1a95ae3eb862e5bcc4ee86258d3e2a1a877cb452cebdeca0f08ba019d731afa2fc78c8a9b0696afba31176df2ab7e392bff671756e774370; TS018a76eb=01d72e6d1628bdb066ddcf4e45958783a51edc72a3c07ad936c1927ceb306d1eae9f716b023fd348acc74c00ae480532b7a06e07d4; ssr-caching=cache#desc=hit#varnish=hit#dc#desc=84_g; XSRF-TOKEN=1696004164|3U0gAOjerBAO; hs=2032116472; bSession=1d25d1f4-7c96-40ff-a1d4-144320c23297|2',
            'pragma': 'no-cache',
            'referer': 'https://borysgolebiowskipl.wixsite.com/borys/contact',
            'sec-ch-ua': '"Google Chrome";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
        }

        response = requests.get('https://borysgolebiowskipl.wixsite.com/borys/_api/v2/dynamicmodel', cookies=cookies,
                                headers=headers)
        slownik = response.json()

        authorization_list = []

        for i in slownik['apps']:
            authorization_list.append(slownik['apps'][i]['instance'])

        headers2 = {
            'Referer': 'https://borysgolebiowskipl.wixsite.com/borys/_partials/wix-thunderbolt/dist/clientWorker.b151dd12.bundle.min.js',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
            'Authorization': '',
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

        headers2['Authorization'] = authorization_list[0]

        response = requests.post(
            'https://borysgolebiowskipl.wixsite.com/borys/_api/wix-forms/v1/submit-form',
            headers=headers2,
            json=json_data,
        )
        soup = BeautifulSoup(response.text, features='html.parser')

        # print('Name: {}'.format(self.entry_name.get()))
        # print('Email: {}'.format(self.entry_email.get()))
        # print('Comments: {}'.format(self.text_comments.get(1.0, 'end')))


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
