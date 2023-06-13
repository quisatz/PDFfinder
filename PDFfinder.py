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
import os
import pdfplumber
import fnmatch

import pandas as pd

from math import floor
from tkinter import ttk, filedialog
import tkinter as tkk

from gui.menubar import Menubar
from gui.frames.no_results_found import FrameNoResultsFound

import glob
import json

class Gui(tkk.Tk):

    def __init__(self , lang):
        super().__init__()

        self.lang = lang
        self.change_lang(lang)
        self.search = ''

        self.scaleW_value = tkk.IntVar(value=20)
        self.scaleW_value.trace_add('write', self.refresh_frame_yellow)

        self.entry_searchVar = tkk.StringVar(self)
        self.entry_searchVar.trace_add('write', self.entry_not_empty)

        self.widgets_results = []

        width_of_window = 1200
        height_of_window = 700

        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x_coordinate = (screen_width / 2) - (width_of_window / 2)
        y_coordinate = (screen_height / 2) - (height_of_window / 2)
        self.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate))

        self.menubar = Menubar(self)
        self._create_green_frame()
        self._create_purple_frame()

        self.frame_black = ttk.Frame(self)
        self.frame_yellow = ttk.Frame(self)

        self._save_selected__add_file_names()
        self.frame_no_results_found = FrameNoResultsFound(self)

    def change_lang(self , language , flag=0):
        self.languages = {}
        self.language_list = glob.glob("language/*.json")
        for lang in self.language_list:
            filename = lang.split('/')[-1]
            lang_code = filename.split('.')[0]
            with open(lang, 'r', encoding='utf8') as file:
                self.languages[lang_code] = json.loads(file.read())
        self.languages = self.languages[language]

        if flag:
            self.destroy()
            gui_object = Gui(language)
        return self.languages

    def new_search(self, *args):
        self.full_list_reserch_patch_files = []
        self.widgets_results = []
        self.uppercaseVar.set("0")
        self.entry_searchVar.set("")
        self.checkbuttonFrame_purpleVar.set("0")
        self.Var_save_selected.set(0)
        self.button_folder.state((['!disabled']))
        self.button_folder.state((['!disabled']))
        self.frame__save_selected__add_file_names.forget()
        self.frame_yellow.forget()
        self.frame_black.forget()
        self.frame_no_results_found.forget()
        self.advanced.state((['disabled']))
        self.save_all_purple_Frame.state(['disabled'])
        self.entry_search.state((['disabled']))
        self.button_search.state(['disabled'])
        self.ignore_case.state(['disabled'])

    def entry_not_empty(self, *args):
        if len(self.entry_searchVar.get()) > 2:
            self.button_search.state(['!disabled'])
        else:
            self.button_search.state(['disabled'])

    def save_to_specific_prefix(self, file):
        if file.name.split('.')[-1] == 'xlsx':

            data = self.full_txt
            read_file = pd.DataFrame([x.split(';') for x in data.split('\n')])

            read_file.to_excel(file.name, index=False, header=False)

            file.close()


        elif file.name.split('.')[-1] == 'html':

            data = self.full_txt[:-1]
            read_file = pd.DataFrame([x.split(';') for x in data.split('\n')])
            read_file.to_html(file.name, index=False, header=False)
            file.close()

        else:
            file.write(self.full_txt)
            file.close()


    def save_file(self, listen, mark=0):
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
                ("Excel", ".xlsx"),
            ])

        if file is None:
            return

        self.save_to_specific_prefix(file)


    def function_save_selected(self, listen):
        self.list_selection = []
        for results in self.widgets_results:
            for _dict in results:
                try:
                    if _dict['checkbox_str'].get() == "on":
                        selection_index = _dict['checkbox_field_no'].get()
                        self.list_selection.append(selection_index)
                except ValueError:
                    selection_index = -1
                    self.list_selection.append(selection_index)
        self.select_reserch_patch_files = []

        self.full_txt = ''

        for plik in self.full_list_reserch_patch_files:

            file_name = plik[-1].split("/")[-1]

            for results in plik[0:-1]:
                temp_list = []

                for inx in self.list_selection:
                    temp_list.append(results[inx])

                if self.Var_save_selected.get() == 1:
                    temp_list.append(file_name)

                temp2 = ''

                for n in temp_list:
                    temp2 += n + ';'

                self.full_txt += (temp2[0:-1] + "\n")

        file = filedialog.asksaveasfile(
            defaultextension='.txt',
            filetypes=[
                ("Text file", ".txt"),
                ("CSV file", ".csv"),
                ("HTML file", ".html"),
                ("Excel", ".xlsx"),
            ])
        if file is None:
            return

        self.save_to_specific_prefix(file)

    def _scrollbar(self):
        self.main_frame = tkk.Frame(self)
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

    def open_folder(self):
        self.open_action = filedialog.askdirectory()
        if self.open_action:

            self.entry_search.state((['!disabled']))
            self.ignore_case.state(['!disabled'])

    def open_file(self):
        self.open_action = filedialog.askopenfilenames(
            title=self.languages["txt_window_name__screen_open PDF files"],
            filetypes=(
                ("PDF Files", "*.pdf"),
                ("All Files", "*.*")))

        if self.open_action:
            self.entry_search.state((['!disabled']))
            self.ignore_case.state(['!disabled'])

    def create_text_in_entries(self, full_list_reserch_patch_files):

        if len(self.full_list_reserch_patch_files[0][0]) > 1 and isinstance(self.full_list_reserch_patch_files[0][0], list):
            self.frame_no_results_found.forget()
            self._create__yellow_frame(full_list_reserch_patch_files)
            self.advanced.state((['!disabled']))
            self.save_all_purple_Frame.state(['!disabled'])
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
                list_search_result_file = self.engine_search(self.pdf2txt(file))
                list_search_result_file.append(file)
                self.full_list_reserch_patch_files.append(list_search_result_file)
        return self.full_list_reserch_patch_files

    def pdf2txt(self, fill_patch_pdf_file):
        with pdfplumber.open(fill_patch_pdf_file) as pdf:
            full_txt_from_pdf_file = ''
            total_pages = len(pdf.pages)
            for i in range(0, total_pages):
                page_obj = pdf.pages[i]
                full_txt_from_pdf_file += page_obj.extract_text() + '\n'
        return full_txt_from_pdf_file

    def engine_search(self, full_txt_from_pdf):
        search_phrase = self.entry_search.get()
        len_search_phrase = len(search_phrase.split())
        # temp_list3 -a list of lists of occurrences of the word followed by occurrences of one file
        temp_list3 = []

        full_txt_from_pdf__split = full_txt_from_pdf.split()

        for idx, elem in enumerate(full_txt_from_pdf__split):
            lista_temp = []
            text_join = " ".join(full_txt_from_pdf__split[
                                idx:idx + len_search_phrase])

            if self.uppercaseVar.get() == "1":
                has_phrase_found = search_phrase.lower() == text_join.lower()
            else:
                has_phrase_found = search_phrase == text_join

            if has_phrase_found:
                lista_temp.append(text_join)
                for i in range(idx + len_search_phrase,
                               # hard 19 words after we found it
                               idx + len_search_phrase + 19):
                    try:

                        lista_temp.append(full_txt_from_pdf__split[i])
                    except:
                        pass
                temp_list3.append(lista_temp)

        return temp_list3

    def _create_green_frame(self):

        self.frame_green = ttk.Frame(self)
        self.frame_green.config(height=100, width=400 )
        self.frame_green_label = ttk.Label(self.frame_green,
                                           text=self.languages["txt_main_screen__select_files_or_folder_to_search"],
                                           font=('Arial', 12))
        self.frame_green_label.grid(row=0, column=0, pady=20, padx=100, sticky='sw')

        self.button_folder = ttk.Button(self.frame_green, text=self.languages["txt_main_screen__folder"], command=self.open_folder)
        self.button_folder.grid(row=1, column=0, padx=10, pady=0, sticky='sw')
        self.button_files = ttk.Button(self.frame_green, text=self.languages["txt_main_screen__files"], command=self.open_file)
        self.button_files.grid(row=1, column=0, padx=10, pady=0, sticky='se')

        self.entry_search = ttk.Entry(self.frame_green, textvariable=self.entry_searchVar, width=45,
                                      font=('Arial', 10))
        self.entry_search.grid(row=4, column=0, padx=10, pady=0, columnspan=2, sticky='swe')
        self.entry_search.state((['disabled']))

        self.uppercaseVar = tkk.StringVar(value='0')
        self.ignore_case = ttk.Checkbutton(self.frame_green, text=self.languages["txt_main_screen__Ignore case"])
        self.ignore_case.grid(row=3, column=0, padx=10, pady=(30, 0), columnspan=2, sticky='swe')
        self.ignore_case.config(variable=self.uppercaseVar, onvalue="1",
                                offvalue="0")
        self.ignore_case.state(['disabled'])

        link5 = ttk.Label(self.frame_green, text=self.languages["txt_main_screen__enter_search_term"], font=('Arial', 8))
        link5.grid(row=5, column=0, pady=0, padx=100, columnspan=2)
        self.wyniki = lambda: self.create_text_in_entries(self.combo(self.open_action))
        self.button_search = ttk.Button(self.frame_green, text=self.languages["txt_main_screen__search"],
                                        command=self.wyniki)
        self.button_search.grid(row=6, column=0, padx=10, pady=20, sticky='sw')
        self.button_search.state(['disabled'])
        self.frame_green.pack()

    def _create_purple_frame(self):
        self.frame_purple = ttk.Frame(self)
        self.frame_purple.pack()

        self.canvas = tkk.Canvas(self.frame_purple)
        self.canvas.config(height=30)
        self.canvas.create_line(0, 30, 10000, 30, fill='black', width=2)
        self.canvas.pack()

        self.checkbuttonFrame_purpleVar = tkk.StringVar(value='0')

        self.advanced = ttk.Checkbutton(self.frame_purple, text=self.languages["txt_main_screen__advanced"])
        self.advanced.state((['disabled']))
        self.advanced.pack(side=tkk.TOP, anchor='nw')
        self.advanced.config(variable=self.checkbuttonFrame_purpleVar, onvalue=1,
                             offvalue=0, command=self.display_input)

        ttk.Label(self.frame_purple, text='', font=('Arial', 8)).pack(pady=20)

        self.save_all_purple_Frame = ttk.Button(self.frame_purple, text=self.languages["txt_main_screen__save_all"],
                                                 command=lambda: self.save_file(self.full_list_reserch_patch_files))
        self.save_all_purple_Frame.pack(side=tkk.TOP, )
        self.save_all_purple_Frame.state(['disabled'])

    def _create__yellow_frame(self, list_full_search_results_from_path):
        self.button_search.state((['disabled']))
        self.frame_yellow.config(relief=tkk.SUNKEN, padding=(30, 15))

        for result in self.widgets_results:
            for widgets in result:
                widgets['entry'].destroy()
                widgets['checkbox'].destroy()

        result_no = 0
        self.widgets_results = []
        list_full_search_results_from_1st_path = []

        if (len(self.full_list_reserch_patch_files[0][0]) > 1
                and isinstance(self.full_list_reserch_patch_files[0][0], list)):
            list_full_search_results_from_1st_path = [list_full_search_results_from_path[0]]  # concept change

        for file in list_full_search_results_from_1st_path:
            first_result_widgets = []
            file = [file[0]] + [file[-1]]  # concept change

            for result in file[:-1]:
                result_no += 1
                for field_no in range(int(self.scaleW_value.get())):
                    widgets = {'entry_str': tkk.StringVar(self)}
                    if field_no < len(result):
                        widgets['entry_str'].set(result[field_no])

                    widgets['entry'] = ttk.Entry(self.frame_yellow, textvariable=widgets['entry_str'], width=15,
                                                 font=('Arial', 10))

                    if not floor(field_no / 10):
                        row = (result_no - 1) * 4 + 1
                    else:
                        row = (result_no - 1) * 4 + 3
                    widgets['entry'].grid(row=row, column=field_no % 10, padx=0, pady=0)
                    widgets['entry'].state(['readonly'])
                    widgets['checkbox_str'] = tkk.StringVar(value='off')
                    widgets['checkbox_field_no'] = tkk.IntVar(value=field_no)

                    if not floor(field_no / 10):
                        row = (result_no - 1) * 4 + 2
                    else:
                        row = (result_no - 1) * 4 + 4
                    widgets['checkbox'] = ttk.Checkbutton(self.frame_yellow, text=self.languages["txt_main_screen__add"])
                    widgets['checkbox'].config(variable=widgets['checkbox_str'], onvalue='on', offvalue='off')
                    widgets['checkbox'].grid(row=row, column=field_no % 10, padx=0, pady=(0, 20), sticky='n')

                    first_result_widgets.append(widgets)

                self.widgets_results.append(first_result_widgets)

        self.scaleW = tkk.Scale(
            self.frame_black, from_=10, label=self.languages["txt_main_screen__display_the_number_of_searched_words_by_phrase_on"],
            variable=self.scaleW_value,length=300, to=20, resolution=10,orient=tkk.HORIZONTAL)

        self.scaleW.grid(row=0, column=2, padx=0, pady=20)

        self.iw = len(list_full_search_results_from_path[0]) - 1
        self.ik = self.scaleW.get()

        self.button_search.state((['!disabled']))

    def _save_selected__add_file_names(self):
        self.frame__save_selected__add_file_names = ttk.Frame(self)
        self.frame__save_selected__add_file_names.config(height=50, width=400)

        self.save_selected = ttk.Button(
            self.frame__save_selected__add_file_names,
            text=self.languages["txt_main_screen__save_selected"],
            command=lambda: self.function_save_selected(self.full_list_reserch_patch_files))

        self.save_selected .grid(row=0, column=0, padx=0, pady=10)
        self.save_selected .state(['!disabled'])

        self.Var_save_selected = tkk.IntVar(value=0)
        self.button_save_selected = ttk.Checkbutton(
            self.frame__save_selected__add_file_names,
            text=self.languages["txt_main_screen__add_file_names"])
        self.button_save_selected.state((['!disabled']))

        self.button_save_selected.grid(row=0, column=2, padx=30, pady=10)
        self.button_save_selected.config(variable=self.Var_save_selected, onvalue=1, offvalue=0)

    def display_input(self):
        if self.checkbuttonFrame_purpleVar.get() == '1':
            self.save_all_purple_Frame.state(['disabled'])
            self.frame_black.pack()
            self.frame_yellow.pack()
            self.frame__save_selected__add_file_names.pack()

        else:
            self.frame_black.forget()
            self.frame_yellow.forget()
            self.frame__save_selected__add_file_names.forget()
            self.save_all_purple_Frame.state(['!disabled'])

    def refresh_frame_yellow(self, *args):
        self.create_text_in_entries(self.full_list_reserch_patch_files)
        self.save_all_purple_Frame.state(['disabled'])


def main():
    gui_object = Gui('language\\pl_PL')
    gui_object.mainloop()


if __name__ == "__main__":
    main()
