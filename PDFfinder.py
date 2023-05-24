'''
do zrobienia pisane 30.04.2023:

+++++++++++++++1. Scroll                           dla yelow frame - dla wikszej ilosci wynikow
+++++++++++++++2. Rozszezenie wynikow pomiedzy 10wynikami nieco i pomiedzy plikami bardziej i kolorystyka
+++++++++++++++2.5 Stworzenie cheboxa              zaznaczajacego cala kolumne wynikow
+++++++++++3. Przechowywanie wynikow w chexboxach
+++++++++++++4.Stworzenie przyisku                dla funcki generujacej ostatecze wyniki - liste z checbox
++++++++++++5.Stworzenie funcji tworzacej liste z checboxow nr4
+++++++++++++++6. podlinkowanie przycisku z nr5 do nr4
7. stworzenie 4 fukcji exportujacej do pliku z oone wyboru gdzie zapisac wyniki ostateczne z nr5:
            csv ,
            html ,
            excel ,
            pdf
8.Podlinkowanie przyciskow z menu do 4 funcji
9.Stworzenie funkicji do nowego szukania
10.Zajecie sie problemamy pozosyalych elementow menu
11.Refactoring
12. Kontorla przez K. Lemka

'''

import sys

try:
    sys.path.append(r'D:/Python/PycharmProjects/__Repo/PDFfinder/venv/Lib/site-packages')

except:
    pass
#from pathlib import Path
import pdfplumber
import pyperclip
import fnmatch
import os
from math import floor
#import random

import webbrowser

#from tkinter import *
from tkinter import ttk, filedialog, messagebox
from tkinter import Menu

import tkinter as tkk


class Gui:

    def __init__(self):
        self.root = tkk.Tk()  # tworze okno root
        self.szukaj = ''
        width_of_window = 1200  #
        height_of_window = 700  #
        screen_width = self.root.winfo_screenwidth()  #
        screen_height = self.root.winfo_screenheight()  #
        x_coordinate = (screen_width / 2) - (width_of_window / 2)  #
        y_coordinate = (screen_height / 2) - (height_of_window / 2)  #

        self.root.geometry("%dx%d+%d+%d" % (width_of_window, height_of_window, x_coordinate, y_coordinate))
        self.scaleW_value = tkk.IntVar(value=20)
        self.scaleW_value.trace_add('write', self.refresh_frame_yelow)

        self.entry_wyszukajVar = tkk.StringVar(self.root)




        # self.logo = PhotoImage(file='logoOpnie.png')  # scizka do gif przycisku

 #       self._scrollbar()
        self._create_menubar()  # fuckcja do stwoprzenia menue
        self._create_green_Frame()
        self._create_purpure_Frame()





        self.entry_wyszukajVar.trace_add('write', self.entry_not_emplty)

        self.frame_black = ttk.Frame(self.root)


        self.frame_yelow = ttk.Frame(self.root)

        self._create_last_Frame()
        self._create_end_Frame()
        self.widgety_wyniki = []
        #self.root.state('zoomed')

    # def SetSize(self):
    #     self.width, self.height, self.X_POS, self.Y_POS = self.root.winfo_width(), self.root.winfo_height(), self.root.winfo_x(), self.root.winfo_y()
    #     self.root.state('normal')
    #     self.root.resizable(0, 0)
    #     self.root.geometry("%dx%d+%d+%d" % (self.width, self.height, self.X_POS, self.Y_POS))


    def nowe_szukanie(self , *args):
        self.full_list_reserch_patch_files = []
        self.widgety_wyniki = []

        self.entry_wyszukajVar.set("")
        self.checkbuttonFrame_purpureVar.set("0")
        self.checkbuttonFrame_frame_last.set(0)

        print('nowe szukanie')

        self.button_frame_green1.state((['!disabled']))
        self.button_frame_green1.state((['!disabled']))

        self.frame_end.forget()
        self.frame_yelow.forget()
        self.frame_black.forget()
        self.frame_last.forget()





        self.checkbutton2.state((['disabled']))
        self.zapisz_wszyskie_purpure_Frame.state(['disabled'])
        self.entry_wyszukaj.state((['disabled']))
        self.button_frame_green.state(['disabled'])
        self.checkbutton30.state(['disabled'])






    def entry_not_emplty(self , *args):
        if len(self.entry_wyszukajVar.get()) > 2:
            self.button_frame_green.state(['!disabled'])
        else:
            self.button_frame_green.state(['disabled'])

    def saveFile(self , listen , mark=0):

        self.full_txt = ''

        if mark == 0:

            for i in listen:
                nazwa_pliku = i[-1].split("/")[-1]  # wyodrebnia nazwe pliku kazdego wyszukania

                for j in i[0:-1]:
                    j.append(nazwa_pliku)
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
                ("All files", ".*"),
            ])
        if file is None:
            return

        file.write(self.full_txt)
        file.close()

   #########################################do zrobienia

    def fun_zapisz_zaznaczone(self , listen):
        #print(self.widgety_wyniki)

        self.list_indexy = []
        for i in self.widgety_wyniki:
            for slownik in i:

                try:
                    if slownik['checkbox_str'].get() == "on":
                        index_zaznaczenia = slownik['checkbox_nr_pola'].get()

                        self.list_indexy.append(index_zaznaczenia)
                except ValueError :
                    index_zaznaczenia = -1
                    self.list_indexy.append(index_zaznaczenia)


        print('self.list_indexy.append:' , self.list_indexy)

        self.zaznaczenie_reserch_patch_files = []





        self.full_txt = ''
        for plik in self.full_list_reserch_patch_files:

            nazwa_pliku = plik[-1].split("/")[-1]

            for wyniki in plik[0:-1]:
                templist = []
                print("wyniki:" , wyniki)

                for inx in self.list_indexy:
                    templist.append(wyniki[inx])

                if self.checkbuttonFrame_frame_last.get() == 1:
                    templist.append(nazwa_pliku)

                # if 19 in self.list_indexy:
                #     print('nazwa_pliku::' , nazwa_pliku)


                temp2 = ''
                for n in templist:
                    temp2 += n + ';'
                self.full_txt += (temp2[0:-1] + "\n")






        file = filedialog.asksaveasfile(
            defaultextension='.txt',
            filetypes=[
                ("Text file", ".txt"),
                ("CSV file", ".csv"),
                ("All files", ".*"),
            ])
        if file is None:
            return


#start################## do pobrania wartosci filetypes a tym samym wywoania innego kodu gdy sie wybierze rozszezenie html
        # def ask_save(self):
        #     type_var = tk.StringVar()
        #     new.path_save = filedialog.asksaveasfilename(initialdir="/",
        #                                                  title="Select the path to save the Image. ",
        #                                                  filetypes=[("PNG", '*.png'),
        #                                                             ("JPEG", '*.jpg'), ("GIF", '*.gif'),
        #                                                             ("ICON", '*.ico'), ("BMP", '*.bmp'),
        #                                                             ("IM", '*.im'), ("JFIF", '*.jfif')],
        #                                                  typevariable=type_var)
        #     if new.path_save:
        #         file_type = type_var.get()
        #         if not new.path_save.lower().endswith(".png") and file_type == "PNG":
        #             new.path_save += ".png"

        # if file:
        #     if Path(file).suffix == '.txt':
        #         print(file)
        #         print("Image")
# end################# do pobrania wartosci filetypes a tym samym wywoania innego kodu gdy sie wybierze rozszezenie html

        file.write(self.full_txt)
        file.close()













                # print('----------------------------')
                # #print(wyniki)
                # print(wyniki , 'i, ' , plik[-1])
                # print('----------------------------')

            # for result in flies[0:-1]:
            #     self.zaznaczenie_reserch_patch_files.append(result)
                # for lists in result:
                #     self.zaznaczenie_reserch_patch_files.append(lists)

        print('self.zaznaczenie_reserch_patch_files' , self.zaznaczenie_reserch_patch_files)



        #
        # for i in self.list_indexy:
        #
        #     print(self.zaznaczenie_reserch_patch_files[i])


        # self.full_txt = ''
        # for i in listen:
        #     nazwa_pliku = i[-1].split("/")[-1]  # wyodrebnia nazwe pliku kazdego wyszukania
        #
        #     for j in i[0:-1]:
        #         j.append(nazwa_pliku)
        #         temp2 = ''
        #         for n in j:
        #             temp2 += n + ';'
        #         self.full_txt += (temp2[0:-1] + "\n")
        #
        # file = filedialog.asksaveasfile(
        #     defaultextension='.txt',
        #     filetypes=[
        #         ("Text file", ".txt"),
        #         ("CSV file", ".csv"),
        #         ("All files", ".*"),
        #     ])
        # if file is None:
        #     return
        #
        # file.write(self.full_txt)
        # file.close()







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
        self.menubar = tkk.Menu(self.root)  # tworze mnue
        self.root.configure(menu=self.menubar)  # umieszczam menue w root

        file = Menu(self.menubar, tearoff=0)  # tworze obiekt menue dziecko menu
        tools = Menu(self.menubar, tearoff=0)
        help_ = Menu(self.menubar, tearoff=0)  # _ bo help to zastrzezony w python

        self.menubar.add_cascade(menu=file, label='Plik')  # dodaje obiekt do menu pod nazwa
        self.menubar.add_cascade(menu=tools, label='Narzedzia')
        self.menubar.add_cascade(menu=help_, label='Pomoc')

        file.add_command(label='Nowe szukanie', command=self.nowe_szukanie)  # co ma zrobic command
        file.add_separator()  # separator
        # file.add_command(label='Otworz szukanie', command=lambda: print('Opening File...'))
        # file.add_command(label='Zapisz szukanie', command=lambda: print('Saving File...'))
        #
        # save = Menu(file, tearoff=0)  # tworze menue aby stalo sie submenu
        # file.add_cascade(menu=save, label='Zapisz wyniki szukania jako')  # umieszczam submenu
        # save.add_command(label='do CSV', command=lambda: print('Saving As...'))  # umieszczam opcje  wsubmenue
        # save.add_command(label='do HTML', command=lambda: print('Saving All...'))
        # save.add_command(label='do EXCEL', command=lambda: print('Saving All...'))
        # save.add_command(label='do PDF - wyniki', command=lambda: print('len + self.widgety_wyniki:' , len(self.widgety_wyniki) , "i, " , self.widgety_wyniki))
        # file.add_separator()
        file.add_command(label='Wyjscie', command=self.root.destroy)

        desain = Menu(tools, tearoff=0)  # tworze menue aby stalo sie submenu
        tools.add_cascade(menu=desain, label='Wyglad')  # umieszczam submenu
        desain.add_command(label='Jasny', command=lambda: print('Saving As...'))  # umieszczam opcje  wsubmenue
        desain.add_command(label='Ciemny', command=lambda: print('Saving All...'))

        language = Menu(tools, tearoff=0)  # tworze menue aby stalo sie submenu
        tools.add_cascade(menu=language, label='Jezyk')  # umieszczam submenu
        language.add_command(label='Polski', command=lambda: print('Saving As...'))  # umieszczam opcje  wsubmenue
        language.add_command(label='English', command=lambda: print('Saving All...'))

        help_.add_command(label='Wyslij opinie', command=lambda: self.wyslij_opinie())  # co ma zrobic command
        help_.add_command(label='Pomoc', command=lambda: print('Opening File...'))
        help_.add_separator()  # separator
        help_.add_command(label='PDF finder - info', command=lambda: self.PDF_finder_info())

    def wyslij_opinie(self):
        bg_color = '#0088FF'
        window2 = tkk.Toplevel(self.root, bg=bg_color)  # tworze nowe okno ktore jest dzieckiem root
        window2.grab_set()
        window2.title('wyslij opinie')  # nazwa okna

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
        # button_window.config(command=self.funkca_do_button_window)

        ttk.Label(window, text='PdfFinder jest programem darmowym').grid(row=7, column=1, padx=10, pady=30, sticky='sw')

    def funkca_do_button_window(self):  # funcja dla przycisku
        return pyperclip.copy('borysgolebiowskipl@gmail.com')

    def callback(self, url):
        webbrowser.open_new(url)

    #########################################################################################################
    def open_folder(self):
        self.open_action = filedialog.askdirectory()
        if self.open_action:  # D: / Python / PycharmProjects / PdfFinder / pdf / zeiss inne

            self.entry_wyszukaj.state((['!disabled']))
            #self.button_frame_green.state(['!disabled'])
            self.checkbutton30.state(['!disabled'])

    def open_file(self):
        self.open_action = filedialog.askopenfilenames(
            title="Open PDF File",
            filetypes=(
                ("PDF Files", "*.pdf"),
                ("All Files", "*.*")))


        if self.open_action:  # ('D:/Python/PycharmProjects/PdfFinder/pdf/zeiss inne/zeiss1pdf-file.pdf', 'D:/Python/PycharmProjects/PdfFinder/pdf/zeiss inne/zeiss2pdf-file.pdf')
            self.entry_wyszukaj.state((['!disabled']))
            #self.button_frame_green.state(['!disabled'])
            self.checkbutton30.state(['!disabled'])


    def tworzeWpisy(self, a):  # a=(self.combo(self.open_action)) ->self.full_list_reserch_patch_files
        print('tworzeWpisy wita......')


        if len(self.full_list_reserch_patch_files[0][0]) > 1 and isinstance(self.full_list_reserch_patch_files[0][0] ,list):
            self.frame_end.forget()
            self._create__yelow_Frame(a)
            self.checkbutton2.state((['!disabled']))
            self.zapisz_wszyskie_purpure_Frame.state(['!disabled'])
            self.entry_wyszukaj.state((['disabled']))
            self.button_frame_green.state(['disabled'])
            self.checkbutton30.state(['disabled'])
            self.button_frame_green1.state(['disabled'])
            self.button_frame_green2.state(['disabled'])

        else:
            self.frame_end.pack()

        return a

    def combo(self, files):
        print('combo wita....')

        self.full_list_reserch_patch_files = []

        if not type(files) is tuple:  # jesli n ie tupla znaczy ze folder wybrany
            self.open_action = tuple()
            for path, dirs, filess in os.walk(files):

                for file in filess:
                    if fnmatch.fnmatch(file, '*.pdf'):
                        full_path = path + '/' + file
                        self.open_action += (full_path,)
            return self.combo(self.open_action)  # teraz juz bedzie tupla

        else:
            for file in files:
                # file: D: / Python / PycharmProjects / PdfFinder / pdf / zeiss inne\zeiss2pdf - file.pdf
                list_shearch_result_file = self.engine_shearch(self.pdf2txt(file))
                # wynik dla:
                # self.pdf2txt(file)                         -> plik txt ze wszyskich stron pdf
                # self.engine_shearch(self.pdf2txt(file))    ->

                # list_shearch_result_file: [['zeiss', 'calypso', 'plan', 'pomiarowy', 'data']]
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
                full_txt_from_pdf_file += pageobj.extract_text() + '\n'  # '\n' poniewaz nie robi entera na ost elemencie strony wiec skleja ost element z jedenj strony z drugim nastepnej
        return full_txt_from_pdf_file

    def engine_shearch(self, full_txt_from_pdf):
        # dzialajaca metoda do szukania slowa z "szukaj" i zwracajaca liste wszystkich wystapień w tekscie w postaci listy

        fraza_szukana = self.entry_wyszukaj.get()
        len_fraza_szukana = len(fraza_szukana.split())
        lista_list_wystapien_slowa_wraz_z_czerema_nast_jednego_pliku = []

        if self.wielkieLitVar.get():
            fraza_szukana = fraza_szukana.lower()

            full_txt_from_pdf = full_txt_from_pdf.lower()
        full_txt_from_pdf__split = full_txt_from_pdf.split()

        print('fraza_szukana zanajezona jako: ', fraza_szukana)

        for idx, elem in enumerate(full_txt_from_pdf__split):  # tu zaczynam dla 1 slowa
            listatemp = []
            textjoin = " ".join(full_txt_from_pdf__split[
                                idx:idx + len_fraza_szukana])  # textjoin slozy do tego by wziol pod uwage wyszukanie z kilku slów

            if fraza_szukana == textjoin:
                print('idx fraza_szukana:', idx)
                listatemp.append(textjoin)  # dodaje zeiss
                for i in range(idx + len_fraza_szukana,
                               idx + len_fraza_szukana + 19):  # TU MA BYC NA SZTYWNO 10 - to entry beda decydowac ile widoczne
                    # dodatkowo +- dlatego ze pdf

                    # len_fraza_szukana - jesli wiecej niz 1 tzn ze wyszukujemy wiecej niz jedno slowo
                    # idx+len_fraza_szukana - od slowa/slow(1-zeiss,2-zejs gowno)
                    try:

                        listatemp.append(full_txt_from_pdf__split[i])
                    except:
                        pass
                lista_list_wystapien_slowa_wraz_z_czerema_nast_jednego_pliku.append(listatemp)


        return lista_list_wystapien_slowa_wraz_z_czerema_nast_jednego_pliku

    def _create_green_Frame(self):

        self.frame_green = ttk.Frame(self.root)

        self.frame_green.config(height=100, width=400)

        ttk.Label(self.frame_green, text='Wybierz pliki/pliki lub folder do przeszukania', font=('Arial', 12)).grid(
            row=0,
            column=0,
            pady=20,
            padx=100,
            sticky='sw')

        self.button_frame_green1 = ttk.Button(self.frame_green, text="Folder", command=self.open_folder)
        self.button_frame_green1.grid(row=1, column=0, padx=10, pady=0, sticky='sw')

        self.button_frame_green2 = ttk.Button(self.frame_green, text="Plik", command=self.open_file)
        self.button_frame_green2.grid(row=1, column=0, padx=10, pady=0, sticky='se')

        # ttk.Label(self.frame_green, text='', font=('Arial', 8)).grid(row=2, column=0, pady=0, padx=100, sticky='sw')
        # ttk.Label(self.frame_green, text='', font=('Arial', 8)).grid(row=3, column=0, pady=0, padx=100, sticky='sw')


        self.entry_wyszukaj = ttk.Entry(self.frame_green, textvariable=self.entry_wyszukajVar, width=45,
                                        font=('Arial', 10))
        self.entry_wyszukaj.grid(row=4, column=0, padx=10, pady=0, columnspan=2, sticky='swe')
        self.entry_wyszukaj.state((['disabled']))

        self.wielkieLitVar = tkk.StringVar()
        self.checkbutton30 = ttk.Checkbutton(self.frame_green, text='ingoruj wielkosc liter?')  # kwadrat do zaznaczenia
        self.checkbutton30.grid(row=3, column=0, padx=10, pady=0, columnspan=2, sticky='swe')
        self.checkbutton30.config(variable=self.wielkieLitVar, onvalue=1,
                                  offvalue=0)
        self.checkbutton30.state(['disabled'])

        link5 = ttk.Label(self.frame_green, text='Wpisz fraze szukana', font=('Arial', 8))
        link5.grid(row=5, column=0, pady=0, padx=100, columnspan=2)
        self.wyniki = lambda: self.tworzeWpisy(self.combo(self.open_action))
        self.button_frame_green = ttk.Button(self.frame_green, text="Szukaj",
                                             command=self.wyniki)
        self.button_frame_green.grid(row=6, column=0, padx=10, pady=20, sticky='sw')
        self.button_frame_green.state(['disabled'])
        self.frame_green.pack()





    def _create_purpure_Frame(self):
        self.frame_purpure = ttk.Frame(self.root)
        self.frame_purpure.pack()



        self.canvas = tkk.Canvas(self.frame_purpure)  # tworze prótno


        self.canvas.pack()
        self.canvas.config(height=30)

        self.canvas.create_line(0, 30, 10000, 30, fill='black', width=2)


        self.checkbuttonFrame_purpureVar = tkk.StringVar(value='0')
        self.checkbutton2 = ttk.Checkbutton(self.frame_purpure, text='zaawansowane?')  # kwadrat do zaznaczenia
        self.checkbutton2.state((['disabled']))

        self.checkbutton2.pack(side=tkk.TOP, anchor='nw')
        self.checkbutton2.config(variable=self.checkbuttonFrame_purpureVar, onvalue=1,
                                 offvalue=0, command=self.display_input)  # display_input pack okna



















        # self.checkbutton2.state(['disabled'])
        ttk.Label(self.frame_purpure, text='', font=('Arial', 8)).pack(pady=20)

        self.zapisz_wszyskie_purpure_Frame = ttk.Button(self.frame_purpure, text="Zapisz wszyskie",
                                               command=lambda: self.saveFile(self.full_list_reserch_patch_files))
        self.zapisz_wszyskie_purpure_Frame.pack(side=tkk.TOP, )
        self.zapisz_wszyskie_purpure_Frame.state(['disabled'])









    def _create__yelow_Frame(self, listaPelneWynikiWyszukaniaZsciezka):
        self.button_frame_green.state((['disabled']))
        self.frame_yelow.config(relief=tkk.SUNKEN, padding=(30, 15))  # FLAT(domyslnie),RAISED,S


        # nisze wszystkie wyniki jesli istnieja a widgety_wyniki stworzylem w __init__
        for wynik in self.widgety_wyniki:
            for widgety in wynik:
                widgety['entry'].destroy()
                widgety['checkbox'].destroy()

        nr_wyniku = 0
        self.widgety_wyniki = []

        # plik to zwrotsc wsyzskich wyszukan i nazwa pliku -> [['zeiss', 'calypso', 'plan', 'pomiarowy', 'data'], 'D:/Python/PycharmProjects/PdfFinder/pdf/zeiss inne\\zeiss2pdf-file.pdf']


         #zmiana koncepcji: pierwotnie program mial program tworzyc widgety dla kazdego wyszukania kazdego pliku ale trwa to za dlugo i zaciemnia fukcjonalnosc programu

        listaPelneWynikiWyszukaniaZsciezka_1szego = []


        if len(self.full_list_reserch_patch_files[0][0]) > 1 and isinstance(self.full_list_reserch_patch_files[0][0] ,list):
            listaPelneWynikiWyszukaniaZsciezka_1szego = [listaPelneWynikiWyszukaniaZsciezka[0]]


        for plik in listaPelneWynikiWyszukaniaZsciezka_1szego:  ##listaPelneWynikiWyszukaniaZsciezka= [[['zeiss', 'calypso', 'plan', 'pomiarowy', 'data'], 'D:/Python/PycharmProjects/PdfFinder/pdf/zeiss inne\\zeiss1pdf-file.pdf'], [['zeiss', 'calypso', 'plan', 'pomiarowy', 'data'], 'D:/Python/PycharmProjects/PdfFinder/pdf/zeiss inne\\zeiss2pdf-file.pdf']]

            widgety_1go_wyniku = []

            plik = [plik[0]] + [plik[-1]]  # zmiana koncepcj uproszenie!!!!!!!!!!!!!!!!!!!!!

            # 'wynik -> ['kontroler', 'cmm', 'nr', 'sztuki', 'master'] * ilosc wyszukan w pliku
            for wynik in plik[:-1]:  # -1 bo ostatni to nazwa pliku


                # nr_wyniku zrestetuje sie po pelnym stworzeniu widgetów
                nr_wyniku += 1

                # nr_pola cyfry to 0-9
                for nr_pola in range(int(self.scaleW_value.get())):  # 10 entry
                    widgety = {}
                    widgety['entry_str'] = tkk.StringVar(self.root)
                    if nr_pola < len(wynik):  # aby nie dodawalo do pola wyniku ktorego juz nie ma
                        widgety['entry_str'].set(wynik[nr_pola])  # ustawi entry_str na warosc wynolu

                    widgety['entry'] = ttk.Entry(self.frame_yelow, textvariable=widgety['entry_str'], width=15,
                                                 font=('Arial', 10))

                    if not floor(nr_pola / 10):  # floor -5.1=-6 33.33=33 ===>   0.5=0    tworze numer row dla nr_pola
                        row = (nr_wyniku - 1) * 4 + 1  # 0-9 pole 1-1*4 +1 = 1 dal 1szego wyszukania =1 dla2giego =5
                    else:
                        row = (nr_wyniku - 1) * 4 + 3  # 10+ pole                 1szego wyszukania =3 dla2giego =7
                    widgety['entry'].grid(row=row, column=nr_pola % 10, padx=0, pady=0)

                    widgety['entry'].state(['readonly'])

                    widgety['checkbox_str'] = tkk.StringVar(value='off')
                    widgety['checkbox_nr_pola'] = tkk.IntVar(value=nr_pola)




                    if not floor(nr_pola / 10):
                        row = (nr_wyniku - 1) * 4 + 2
                    else:
                        row = (nr_wyniku - 1) * 4 + 4
                    widgety['checkbox'] = ttk.Checkbutton(self.frame_yelow ,text='dodać?'  )  # kwadrat do zaznaczenia
                    widgety['checkbox'].config(variable=widgety['checkbox_str'], onvalue='on', offvalue='off')
                    widgety['checkbox'].grid(row=row, column=nr_pola % 10, padx=0, pady=(0,20) , sticky = 'n')

                    widgety_1go_wyniku.append(widgety)


                #################widgety['entry_str'].set(plik[-1][0])
                # # print('widgety::::::::::::' , widgety)
                # # print('widgety[entry_str].set(plik[-1][0]):', widgety)
                # print('---------------------------------')
                # print('self.widgety_wyniki przed append' , self.widgety_wyniki)
                self.widgety_wyniki.append(widgety_1go_wyniku)
                # print('---------------------------------')
                # print('self.widgety_wyniki.append(widgety_1go_wyniku ---------> self.widgety_wyniki' , self.widgety_wyniki)
                # print('---------------widgety_1go_wyniku------------------')
                # print(widgety_1go_wyniku)



        self.scaleW = tkk.Scale(self.frame_black, from_=10, label='ilość wyszukanych slow po', variable=self.scaleW_value,
                            length=300, to=20, resolution=10,orient=tkk.HORIZONTAL  ) #command=lambda e: self.root.after(100,self.SetSize)
        # self.scaleW.set(3)
        self.scaleW.grid(row=0, column=2, padx=0, pady=20)

        self.iw = len(listaPelneWynikiWyszukaniaZsciezka[0]) - 1  # prawidolowa zmienna iw
        self.ik = self.scaleW.get()  # prawidlowa zmienna ik

        print('iw:', self.iw)
        print('ik:', self.ik)

        #        self.iw = 4 #zmienna do usuniecia natpisuja te wyzej tylko do testow
        #        self.ik = 7 #zmienna do usuniecia natpisuja te wyzej tylko do testow


        ################# NO I TUTAJ SIE ZABAWA ZACZYNA
        '''
        for i in range(1, iw+1):
            for j in range(1, ik+1):




                tempus = i                
                tempVar1 = globals()['box{}{}Var'.format(i, j)] = StringVar(self.root)    
                #globals()['box{}{}Var'.format(i, j)] = StringVar(self.root)

                globals()['entry_wyszukaj{}{}'.format(i, j)] = ttk.Entry(self.frame_yelow, textvariable=tempVar1,
                                                                width=15, font=('Arial', 10)).grid(row=i+1,
                                                                                           column=j,
                                                                                           padx=0,
                                                                                           pady=0)



                #globals()['entry_wyszukaj{}{}'.format(i, j)].state(['readonly'])

                tempVar3 = globals()['checkbutton{}{}Var'.format(i, j)] = StringVar()
                tempVar4 = globals()['checkbutton{}{}'.format(i, j)] = ttk.Checkbutton(self.frame_yelow, text='dodać?').grid(row=i+2,
                                                                                      column=j,
                                                                                      padx=0,
                                                                                      pady=0)

                #globals()['checkbutton{}{}'.config(variable=tempVar3, onvalue='on', offvalue='off')





        '''
        # ttk.Label(self.frame_yelow, text='', font=('Arial', 8)).grid(row=0, column=0, padx=0, pady=20)

        ################# NO I TUTAJ SIE ZABAWA KONCZY
        self.button_frame_green.state((['!disabled']))


    def _create_end_Frame(self):


        self.frame_end = ttk.Frame(self.root)
        self.frame_end.config(height=50, width=400)

        nothing = ttk.Label(self.frame_end, text='Nie znaleziono żadnych wynikow!', font=('Arial', 20))
        nothing.grid(row=5, column=0, pady=50, padx=100, columnspan=2)




    def _create_last_Frame(self):
        self.frame_last = ttk.Frame(self.root)
        self.frame_last.config(height=50, width=400)

        self.zapisz_zaznaczone_last_Frame = ttk.Button(self.frame_last, text="Zapisz zaznaczone",
                                               command= lambda: self.fun_zapisz_zaznaczone(self.full_list_reserch_patch_files))

        self.zapisz_zaznaczone_last_Frame.grid(row=0, column=0, padx=0, pady=10)
        self.zapisz_zaznaczone_last_Frame.state(['!disabled'])




        self.checkbuttonFrame_frame_last = tkk.IntVar(value=0)
        self.checkbutton33 = ttk.Checkbutton(self.frame_last, text='dodać nazwe plków??')  # kwadrat do zaznaczenia
        self.checkbutton33.state((['!disabled']))

        self.checkbutton33.grid(row=0, column=2, padx=30, pady=10)
        self.checkbutton33.config(variable=self.checkbuttonFrame_frame_last, onvalue=1,
                                 offvalue=0)  # display_input pack okna






    def display_input(self):
        if self.checkbuttonFrame_purpureVar.get() == '1':
            self.zapisz_wszyskie_purpure_Frame.state(['disabled'])
            #self.root.state('zoomed')
            self.frame_black.pack()
            self.frame_yelow.pack()
            self.frame_last.pack()

        else:
            self.frame_black.forget()
            self.frame_yelow.forget()
            self.frame_last.forget()
            self.zapisz_wszyskie_purpure_Frame.state(['!disabled'])

    def refresh_frame_yelow(self, *args):
        # self.frame_yelow.destroy()
        #self.root.state('zoomed')
        self.tworzeWpisy(self.full_list_reserch_patch_files)

        print('self.scaleW.get()!!!', self.scaleW_value.get())
        self.zapisz_wszyskie_purpure_Frame.state(['disabled'])
        # print('------------KONIEC---------')
        # print('---------------------------')
        # print('---START----self.widgety_wyniki:--------------------')
        # print(self.widgety_wyniki)
        # print('---KONIEC----self.widgety_wyniki:-------------------')
        # print('----------------------------------------------------')
        # print('---START----for i in self.widgety_wyniki:--------------------')
        # for i in self.widgety_wyniki:
        #     print('i:' , i)
        # print('---koniec----for i in self.widgety_wyniki:--------------------')





def main():
    gui_Obiect = Gui()
    tkk.mainloop()


if __name__ == "__main__": main()
