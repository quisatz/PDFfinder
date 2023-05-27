'''
do zrobienia pisane 27.05.2023:

7. stworzenie 4 fukcji exportujacej do pliku z oone wyboru gdzie zapisac wyniki ostateczne z nr5:
            csv ,
            html ,
            excel ,
8.Podlinkowanie przyciskow z menu do 4 funcji
+++++++++++++++++++++++++9.Stworzenie funkicji do nowego szukania
10.Zajecie sie problemamy pozosyalych elementow menu
11.Refactoring
12. Kontorla przez K. Lemka

'''
###################path to work when having packages locally#######################################
# import sys
# try:
#     sys.path.append(r'D:/Python/PycharmProjects/__Repo/PDFfinder/venv/Lib/site-packages')
#
# except:
#     pass
###################################################################################################
# from pathlib import Path

import os
import pdfplumber
import pyperclip
import webbrowser
import fnmatch

from math import floor
from tkinter import ttk, filedialog, messagebox, Menu
import tkinter as tkk


class Gui:

    def __init__(self):
        self.root = tkk.Tk()

        self.search = ''

        self.scaleW_value = tkk.IntVar(value=20)
        self.scaleW_value.trace_add('write', self.refresh_frame_yelow)

        self.entry_searchVar = tkk.StringVar(self.root)
        self.entry_searchVar.trace_add('write', self.entry_not_emplty)

        self.widgets_results = []

        width_of_window = 1200
        height_of_window = 700

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_coordinate = (screen_width / 2) - (width_of_window / 2)
        y_coordinate = (screen_height / 2) - (height_of_window / 2)
        self.root.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate))

        self._create_menubar()
        self._create_green_Frame()
        self._create_purpure_Frame()

        self.frame_black = ttk.Frame(self.root)
        self.frame_yelow = ttk.Frame(self.root)

        self._save_selected__add_file_names()
        self.no_results_found()


    def new_search(self, *args):
        self.full_list_reserch_patch_files = []
        self.widgets_results = []
        self.uppercaseVar.set("0")
        self.entry_searchVar.set("")
        self.checkbuttonFrame_purpureVar.set("0")
        self.Var_save_selected.set(0)
        self.button_folder.state((['!disabled']))
        self.button_folder.state((['!disabled']))
        self.frame__save_selected__add_file_names.forget()
        self.frame_yelow.forget()
        self.frame_black.forget()
        self.frame_no_results_found.forget()
        self.advanced.state((['disabled']))
        self.save_all_purpure_Frame.state(['disabled'])
        self.entry_search.state((['disabled']))
        self.button_search.state(['disabled'])
        self.ignore_case.state(['disabled'])


    def entry_not_emplty(self , *args):
        if len(self.entry_searchVar.get()) > 2:
            self.button_search.state(['!disabled'])
        else:
            self.button_search.state(['disabled'])

    def saveFile(self , listen , mark=0):
        self.full_txt = ''

        if mark == 0:
            for i in listen:
                file_name = i[-1].split("/")[-1]  # wyodrebnia nazwe pliku kazdego wyszukania
                for j in i[0:-1]:
                    j.append(file_name)
                    temp2 = ''
                    for n in j:
                        temp2 += n + ';'
                    self.full_txt += (temp2[0:-1] + "\n")
        else:
            pass
        file = filedialog.asksaveasfile(
            defaultextension='.txt',
            filetypes=[
                ("Text file", ".txt"),
                ("CSV file", ".csv"),
                ("HTML file", ".html"),
                ("All files", ".*"),
            ])

        if file is None:
            return

###############  html code generator

###HTML
        if file.name.split('.')[-1] == 'html':
           print('TEST: is html')
            ##### insert the code to generate the tables in html here




        file.write(self.full_txt)
        file.close()



    def function_save_selected(self , listen):
        self.list_selection = []
        for results in self.widgets_results:
            for _dict in results:
                try:
                    if _dict['checkbox_str'].get() == "on":
                        selection_index = _dict['checkbox_field_no'].get()
                        self.list_selection.append(selection_index)
                except ValueError :
                    selection_index = -1
                    self.list_selection.append(selection_index)
        self.select_reserch_patch_files = []

        self.full_txt = ''

        for plik in self.full_list_reserch_patch_files:

            file_name = plik[-1].split("/")[-1]

            for results in plik[0:-1]:
                templist = []

                for inx in self.list_selection:
                    templist.append(results[inx])

                if self.Var_save_selected.get() == 1:
                    templist.append(file_name)

                temp2 = ''

                for n in templist:
                    temp2 += n + ';'

                self.full_txt += (temp2[0:-1] + "\n")

        file = filedialog.asksaveasfile(
            defaultextension='.txt',
            filetypes=[
                ("Text file", ".txt"),
                ("CSV file", ".csv"),
                ("HTML file", ".html"),
                ("All files", ".*"),
            ])
        if file is None:
            return

        ###############  html code generator

        ###HTML
        if file.name.split('.')[-1] == 'html':
            print('is html')
            ##### insert the code to generate the tables in html here

        file.write(self.full_txt)
        file.close()

    def _scrollbar(self):
        self.main_frame = tkk.Frame(self.root)
        self.main_frame.pack(fill=tkk.BOTH, expand=1)

        self.main_canvas = tkk.Canvas(self.main_frame)
        self.main_canvas.pack(side=tkk.LEFT, fill=tkk.BOTH, expand=1)

        self.main_scrollbar = ttk.Scrollbar(self.main_frame, orient=tkk.VERTICAL, command=self.main_canvas.yview)
        self.main_scrollbar.pack(side=tkk.RIGHT, fill=tkk.Y)

        self.main_canvas.configure(yscrollcommand=self.main_scrollbar.set)

        self.main_canvas.bind('<Configure>',
                              lambda e: self.main_canvas.configure(scrollregion=self.main_canvas.bbox("all")))

        self.top_frame = tkk.Frame(self.main_canvas)

        self.main_canvas.create_window((0, 0), window=self.top_frame, anchor="nw")



    def _create_menubar(self):
        self.menubar = tkk.Menu(self.root)
        self.root.configure(menu=self.menubar)

        file = Menu(self.menubar, tearoff=0)
        tools = Menu(self.menubar, tearoff=0)
        help_ = Menu(self.menubar, tearoff=0)

        self.menubar.add_cascade(menu=file, label='Plik')
        self.menubar.add_cascade(menu=tools, label='Narzedzia')
        self.menubar.add_cascade(menu=help_, label='Pomoc')

        file.add_command(label='Nowe szukanie', command=self.new_search)
        file.add_separator()

        file.add_command(label='Wyjscie', command=self.root.destroy)

        desain = Menu(tools, tearoff=0)
        tools.add_cascade(menu=desain, label='Wyglad')
        desain.add_command(label='Jasny', command=lambda: print('Saving As...'))
        desain.add_command(label='Ciemny', command=lambda: print('Saving All...'))

        language = Menu(tools, tearoff=0)
        tools.add_cascade(menu=language, label='Jezyk')
        language.add_command(label='Polski', command=lambda: print('Saving As...'))
        language.add_command(label='English', command=lambda: print('Saving All...'))

        help_.add_command(label='Wyslij opinie', command=lambda: self.send_feedback())
        help_.add_command(label='Pomoc', command=lambda: print('Opening File...'))
        help_.add_separator()
        help_.add_command(label='PDF finder - info', command=lambda: self.PDF_finder_info())

    def send_feedback(self):
        bg_color = '#0088FF'
        window2 = tkk.Toplevel(self.root, bg=bg_color)
        window2.grab_set()
        window2.title('wyslij opinie')

        window2.title('Feedback')
        window2.resizable(False, False)

        window2.configure(bg=bg_color)

        self.frame_header = ttk.Frame(window2)
        self.frame_header.pack()

        self.frame_header.style = ttk.Style()
        self.frame_header.style.configure('TFrame', background='#0088FF')
        self.frame_header.style.configure('TButton', background='#0088FF')
        self.frame_header.style.configure('TLabel', background='#0088FF', font=('Arial', 10))
        self.frame_header.style.configure('Header.TLabel', font=('Arial', 14))

        self.logo = tkk.PhotoImage(file='logoOpnie.png')
        ttk.Label(self.frame_header, image=self.logo).grid(row=0, column=0, rowspan=2)
        ttk.Label(self.frame_header, text='Zostaw swoja opinie.', style='Header.TLabel', background=bg_color).grid(
            row=0, column=1)

        self.frame_content = ttk.Frame(window2)
        self.frame_content.pack()

        ttk.Label(self.frame_content, text='Name:').grid(row=0, column=0, padx=5, sticky='sw')
        ttk.Label(self.frame_content, text='Email:').grid(row=0, column=1, padx=5, sticky='sw')
        ttk.Label(self.frame_content, text='Comments:').grid(row=2, column=0, padx=5, sticky='sw')

        self.entry_name = ttk.Entry(self.frame_content, width=24, font=('Arial', 10), background=bg_color)
        self.entry_email = ttk.Entry(self.frame_content, width=24, font=('Arial', 10), background=bg_color)
        self.text_comments = tkk.Text(self.frame_content, width=50, height=10, font=('Arial', 10), background=bg_color)

        self.entry_name.grid(row=1, column=0, padx=5)
        self.entry_email.grid(row=1, column=1, padx=5)
        self.text_comments.grid(row=3, column=0, columnspan=2, padx=5)

        ttk.Button(self.frame_content, text='Submit',
                   command=self.submit).grid(row=4, column=0, padx=5, pady=5, sticky='e')
        ttk.Button(self.frame_content, text='Clear',
                   command=self.clear).grid(row=4, column=1, padx=5, pady=5, sticky='w')

    def submit(self):
        print('Name: {}'.format(self.entry_name.get()))
        print('Email: {}'.format(self.entry_email.get()))
        print('Comments: {}'.format(self.text_comments.get(1.0, 'end')))
        self.clear()
        messagebox.showinfo(title='Feedback', message='Comments Submitted!')

    def clear(self):
        self.entry_name.delete(0, 'end')
        self.entry_email.delete(0, 'end')
        self.text_comments.delete(1.0, 'end')

    def PDF_finder_info(self):
        window = tkk.Toplevel(self.root)  # tworze nowe okno ktore jest dzieckiem root
        window.title('PDF finder info')  # nazwa okna

        windowWidth = self.root.winfo_reqwidth()
        windowHeight = self.root.winfo_reqheight()
        positionRight = int(self.root.winfo_screenwidth() / 2 - windowWidth / 2)
        positionDown = int(self.root.winfo_screenheight() / 2 - windowHeight / 2)
        window.geometry("+{}+{}".format(positionRight, positionDown))

        window.resizable(False, False)
        self.label = tkk.Label(window, width=5)
        self.label2 = tkk.Label(window, width=5)
        self.label2 = tkk.Label(window, width=5)
        self.label3 = tkk.Label(window, width=5)
        self.label4 = tkk.Label(window, width=5)
        self.label5 = tkk.Label(window, width=5)

        ttk.Label(window, text='PdfFinder ver 1.0 (x64):').grid(row=1, column=1, padx=10, pady=5, sticky='sw')
        ttk.Label(window, text='Copyright (c) Borys Gołębiowski:').grid(row=2, column=1, padx=10, sticky='sw')

        ttk.Label(window, image=self.logo).grid(row=2, column=2, rowspan=2)

        ttk.Label(window, text='You can find me on:').grid(row=3, column=1, padx=10, pady=5, sticky='sw')

        link1 = ttk.Label(window, text='Facebook:', cursor="hand2")
        link1.grid(row=4, column=1, padx=10, pady=10, sticky='sw')
        link1.bind("<Button-1>", lambda e: self.callback("https://www.facebook.com/NathanCelina"))

        link2 = ttk.Label(window, text='Linkedin', cursor="hand2")
        link2.grid(row=5, column=1, padx=10, pady=10, sticky='sw')
        link2.bind("<Button-1>",
                   lambda e: self.callback("https://www.linkedin.com/in/borys-go%C5%82%C4%99biowski-02b883158/"))

        link3 = ttk.Label(window, text='Email', cursor="hand2")
        link3.grid(row=6, column=1, pady=10, padx=10, sticky='sw')
        link3.bind("<Button-1>", lambda e: self.callback("mailto:borysgolebiowskipl@gmail.com"))

        button_window = ttk.Button(window, text="Copy email")
        button_window.grid(row=6, column=2, sticky='sw')

        ttk.Label(window, text='PdfFinder jest programem darmowym').grid(row=7, column=1, padx=10, pady=30, sticky='sw')

    def pyperclip_function(self):
        return pyperclip.copy('borysgolebiowskipl@gmail.com')

    def callback(self, url):
        webbrowser.open_new(url)


    def open_folder(self):
        self.open_action = filedialog.askdirectory()
        if self.open_action:

            self.entry_search.state((['!disabled']))
            self.ignore_case.state(['!disabled'])

    def open_file(self):
        self.open_action = filedialog.askopenfilenames(
            title="Open PDF File",
            filetypes=(
                ("PDF Files", "*.pdf"),
                ("All Files", "*.*")))


        if self.open_action:
            self.entry_search.state((['!disabled']))
            self.ignore_case.state(['!disabled'])


    def create_text_in_entries(self, full_list_reserch_patch_files):

        if len(self.full_list_reserch_patch_files[0][0]) > 1 and isinstance(self.full_list_reserch_patch_files[0][0], list):
            self.frame_no_results_found.forget()
            self._create__yelow_Frame(full_list_reserch_patch_files)
            self.advanced.state((['!disabled']))
            self.save_all_purpure_Frame.state(['!disabled'])
            self.entry_search.state((['disabled']))
            self.button_search.state(['disabled'])
            self.ignore_case.state(['disabled'])
            self.button_folder.state(['disabled'])
            self.button_files.state(['disabled'])

        else:
            self.frame_no_results_found.pack()

        return full_list_reserch_patch_files

    def combo(self, files):
        self.full_list_reserch_patch_files = []

        if not type(files) is tuple:
            self.open_action = tuple()
            for path, dirs, filess in os.walk(files):

                for file in filess:
                    if fnmatch.fnmatch(file, '*.pdf'):
                        full_path = path + '/' + file
                        self.open_action += (full_path,)
            return self.combo(self.open_action)

        else:
            for file in files:
                list_shearch_result_file = self.engine_shearch(self.pdf2txt(file))
                list_shearch_result_file.append(file)
                self.full_list_reserch_patch_files.append(list_shearch_result_file)
        print('------>return self.full_list_reserch_patch_files', self.full_list_reserch_patch_files)
        return self.full_list_reserch_patch_files

    def pdf2txt(self, fill_patch_pdf_file):
        with pdfplumber.open(fill_patch_pdf_file) as pdf:
            full_txt_from_pdf_file = ''
            totalpages = len(pdf.pages)
            for i in range(0, totalpages):
                pageobj = pdf.pages[i]
                full_txt_from_pdf_file += pageobj.extract_text() + '\n'
        return full_txt_from_pdf_file

    def engine_shearch(self, full_txt_from_pdf):
        search_phrase = self.entry_search.get()
        len_search_phrase = len(search_phrase.split())
        #templist3 -a list of lists of occurrences of the word followed by occurrences of one file
        templist3 = []

        full_txt_from_pdf__split = full_txt_from_pdf.split()

        print('search phrase find as: ', search_phrase)

        for idx, elem in enumerate(full_txt_from_pdf__split):
            listatemp = []
            textjoin = " ".join(full_txt_from_pdf__split[
                                idx:idx + len_search_phrase])

            if self.uppercaseVar.get() == "1":
                has_phrase_found = search_phrase.lower() == textjoin.lower()
            else:
                has_phrase_found = search_phrase == textjoin

            if has_phrase_found:
                listatemp.append(textjoin)
                for i in range(idx + len_search_phrase,
                               #hard 19 words after we found it
                               idx + len_search_phrase + 19):
                    try:

                        listatemp.append(full_txt_from_pdf__split[i])
                    except:
                        pass
                templist3.append(listatemp)

        return templist3

    def _create_green_Frame(self):

        self.frame_green = ttk.Frame(self.root)
        self.frame_green.config(height=100, width=400 , ) #relief=tkk.SUNKEN,

        ttk.Label(self.frame_green, text='Wybierz pliki/pliki lub folder do przeszukania', font=('Arial', 12)).grid(
            row=0,
            column=0,
            pady=20,
            padx=100,
            sticky='sw')

        self.button_folder = ttk.Button(self.frame_green, text="Folder", command=self.open_folder)
        self.button_folder.grid(row=1, column=0, padx=10, pady=0, sticky='sw')

        self.button_files = ttk.Button(self.frame_green, text="Plik", command=self.open_file)
        self.button_files.grid(row=1, column=0, padx=10, pady=0, sticky='se')

        self.entry_search = ttk.Entry(self.frame_green, textvariable=self.entry_searchVar, width=45,
                                      font=('Arial', 10))
        self.entry_search.grid(row=4, column=0, padx=10, pady=0, columnspan=2, sticky='swe')
        self.entry_search.state((['disabled']))

        self.uppercaseVar = tkk.StringVar(value='0')
        self.ignore_case = ttk.Checkbutton(self.frame_green, text='ingoruj wielkosc liter?')  # kwadrat do zaznaczenia
        self.ignore_case.grid(row=3, column=0, padx=10, pady=0, columnspan=2, sticky='swe')
        self.ignore_case.config(variable=self.uppercaseVar, onvalue="1",
                                offvalue="0")
        self.ignore_case.state(['disabled'])

        link5 = ttk.Label(self.frame_green, text='Wpisz fraze szukana', font=('Arial', 8))
        link5.grid(row=5, column=0, pady=0, padx=100, columnspan=2)
        self.wyniki = lambda: self.create_text_in_entries(self.combo(self.open_action))
        self.button_search = ttk.Button(self.frame_green, text="Szukaj",
                                        command=self.wyniki)
        self.button_search.grid(row=6, column=0, padx=10, pady=20, sticky='sw')
        self.button_search.state(['disabled'])
        self.frame_green.pack()


    def _create_purpure_Frame(self):
        self.frame_purpure = ttk.Frame(self.root)
#        self.frame_purpure.config(relief=tkk.SUNKEN)  # relief=tkk.SUNKEN,
        self.frame_purpure.pack()

        self.canvas = tkk.Canvas(self.frame_purpure)  # tworze prótno
        self.canvas.config(height=30)
        self.canvas.create_line(0, 30, 10000, 30, fill='black', width=2)
        self.canvas.pack()

        self.checkbuttonFrame_purpureVar = tkk.StringVar(value='0')

        self.advanced = ttk.Checkbutton(self.frame_purpure, text='zaawansowane?')  # kwadrat do zaznaczenia
        self.advanced.state((['disabled']))
        self.advanced.pack(side=tkk.TOP, anchor='nw')
        self.advanced.config(variable=self.checkbuttonFrame_purpureVar, onvalue=1,
                             offvalue=0, command=self.display_input)  # display_input pack okna

        ttk.Label(self.frame_purpure, text='', font=('Arial', 8)).pack(pady=20)

        self.save_all_purpure_Frame = ttk.Button(self.frame_purpure, text="Zapisz wszyskie",
                                                 command=lambda: self.saveFile(self.full_list_reserch_patch_files))
        self.save_all_purpure_Frame.pack(side=tkk.TOP, )
        self.save_all_purpure_Frame.state(['disabled'])


    def _create__yelow_Frame(self, list_full_search_results_from_path):
        self.button_search.state((['disabled']))
        self.frame_yelow.config(relief=tkk.SUNKEN, padding=(30, 15))

        for result in self.widgets_results:
            for widgety in result:
                widgety['entry'].destroy()
                widgety['checkbox'].destroy()

        result_no = 0
        self.widgets_results = []
        list_full_search_results_from_1st_path = []

        if len(self.full_list_reserch_patch_files[0][0]) > 1 and isinstance(self.full_list_reserch_patch_files[0][0] ,list):
            list_full_search_results_from_1st_path = [list_full_search_results_from_path[0]] # concept change


        for file in list_full_search_results_from_1st_path:
            first_result_widgets = []
            file = [file[0]] + [file[-1]]  # concept change

            for result in file[:-1]:
                result_no += 1
                for field_no in range(int(self.scaleW_value.get())):
                    widgety = {}
                    widgety['entry_str'] = tkk.StringVar(self.root)
                    if field_no < len(result):
                        widgety['entry_str'].set(result[field_no])

                    widgety['entry'] = ttk.Entry(self.frame_yelow, textvariable=widgety['entry_str'], width=15,
                                                 font=('Arial', 10))

                    if not floor(field_no / 10):
                        row = (result_no - 1) * 4 + 1
                    else:
                        row = (result_no - 1) * 4 + 3
                    widgety['entry'].grid(row=row, column=field_no % 10, padx=0, pady=0)
                    widgety['entry'].state(['readonly'])
                    widgety['checkbox_str'] = tkk.StringVar(value='off')
                    widgety['checkbox_field_no'] = tkk.IntVar(value=field_no)

                    if not floor(field_no / 10):
                        row = (result_no - 1) * 4 + 2
                    else:
                        row = (result_no - 1) * 4 + 4
                    widgety['checkbox'] = ttk.Checkbutton(self.frame_yelow ,text='dodać?'  )
                    widgety['checkbox'].config(variable=widgety['checkbox_str'], onvalue='on', offvalue='off')
                    widgety['checkbox'].grid(row=row, column=field_no % 10, padx=0, pady=(0,20) , sticky = 'n')

                    first_result_widgets.append(widgety)

                self.widgets_results.append(first_result_widgets)

        self.scaleW = tkk.Scale(self.frame_black, from_=10, label='ilość wyszukanych slow po', variable=self.scaleW_value,
                            length=300, to=20, resolution=10,orient=tkk.HORIZONTAL )

        self.scaleW.grid(row=0, column=2, padx=0, pady=20)

        self.iw = len(list_full_search_results_from_path[0]) - 1
        self.ik = self.scaleW.get()

        print('iw:', self.iw)
        print('ik:', self.ik)

        self.button_search.state((['!disabled']))

    def no_results_found(self):
        self.frame_no_results_found = ttk.Frame(self.root)
        self.frame_no_results_found.config(height=50, width=400)
        nothing = ttk.Label(self.frame_no_results_found, text='Nie znaleziono żadnych wynikow!', font=('Arial', 20))
        nothing.grid(row=5, column=0, pady=50, padx=100, columnspan=2)




    def _save_selected__add_file_names(self):
        self.frame__save_selected__add_file_names = ttk.Frame(self.root)
        self.frame__save_selected__add_file_names.config(height=50, width=400 )

        self.save_selected = ttk.Button(self.frame__save_selected__add_file_names, text="Zapisz zaznaczone",
                                                       command= lambda: self.function_save_selected(self.full_list_reserch_patch_files))

        self.save_selected .grid(row=0, column=0, padx=0, pady=10)
        self.save_selected .state(['!disabled'])

        self.Var_save_selected = tkk.IntVar(value=0)
        self.button_save_selected = ttk.Checkbutton(self.frame__save_selected__add_file_names, text='dodać nazwe plków??')
        self.button_save_selected.state((['!disabled']))

        self.button_save_selected.grid(row=0, column=2, padx=30, pady=10)
        self.button_save_selected.config(variable=self.Var_save_selected, onvalue=1,
                                 offvalue=0)


    def display_input(self):
        if self.checkbuttonFrame_purpureVar.get() == '1':
            self.save_all_purpure_Frame.state(['disabled'])
            self.frame_black.pack()
            self.frame_yelow.pack()
            self.frame__save_selected__add_file_names.pack()

        else:
            self.frame_black.forget()
            self.frame_yelow.forget()
            self.frame__save_selected__add_file_names.forget()
            self.save_all_purpure_Frame.state(['!disabled'])

    def refresh_frame_yelow(self, *args):
        self.create_text_in_entries(self.full_list_reserch_patch_files)
        self.save_all_purpure_Frame.state(['disabled'])

def main():
    gui_Obiect = Gui()
    tkk.mainloop()


if __name__ == "__main__": main()