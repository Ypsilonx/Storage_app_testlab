import os
import tkinter as tk
import getpass
import tkinter.font as tkFont
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime

from storage_gb_app import SkladManager

class InsertProjectDialog(tk.Toplevel):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.title("Insert project:")
        self.entry_values = None
        width = 600
        height = 200
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstring = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstring)
        
        label = tk.Label(self, text="Insert project: (please input relevant project)", font= ("Consolas", 14), anchor="center")
        label.place(x=15, y=15)
        
        label_project_alias = tk.Label(self, text="Project ALIAS:", font= ("Consolas", 12))
        label_project_alias.place(x=15, y=65)
        self.entry_project_alias = tk.Entry(self, font=("Consolas", 12))
        self.entry_project_alias.place(x=180, y=65, width=200, height=30)
        
        label_project_name = tk.Label(self, text="Project name:", font= ("Consolas", 12))
        label_project_name.place(x=15, y=110)
        self.entry_project_name = tk.Entry(self, font=("Consolas", 12))
        self.entry_project_name.place(x=180, y=110, width=200, height=30)
        
        save = tk.Button(self, text="Save", font= ("Consolas", 15), anchor="center", command=self.save_butt_command)
        save.place(x=20, y=150, width=80, height=35)
        cancel = tk.Button(self, text="Cancel", font= ("Consolas", 15), anchor="center", command=self.cancel_butt_command)
        cancel.place(x=110, y=150, width=80, height=35)
    
    def save_butt_command(self):
        PROJECT = self.entry_project_alias.get()
        PROJECT_NAME = self.entry_project_name.get()
        self.entry_values = (PROJECT, PROJECT_NAME)
        sklad_manager.insert_to_projects(self.entry_values)
        self.destroy()
        
    def cancel_butt_command(self):
        self.destroy()
        
class InsertEngineerDialog(tk.Toplevel):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.title("Insert engineer:")
        self.entry_values = None
        width = 600
        height = 250
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstring = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstring)
        
        label = tk.Label(self, text="Insert engineer: (please input relevant names)", font= ("Consolas", 14), anchor="center")
        label.place(x=15, y=15)
        
        label_engineer_alias = tk.Label(self, text="Engineer ALIAS:", font= ("Consolas", 12))
        label_engineer_alias.place(x=15, y=65)
        self.entry_engineer_alias = tk.Entry(self, font=("Consolas", 12))
        self.entry_engineer_alias.place(x=180, y=65, width=200, height=30)
        
        label_engineer_name = tk.Label(self, text="Engineer name:", font= ("Consolas", 12))
        label_engineer_name.place(x=15, y=110)
        self.entry_engineer_name = tk.Entry(self, font=("Consolas", 12))
        self.entry_engineer_name.place(x=180, y=110, width=200, height=30)
        
        label_engineer_surname = tk.Label(self, text="Engineer surname:", font= ("Consolas", 12))
        label_engineer_surname.place(x=15, y=155)
        self.entry_engineer_surname = tk.Entry(self, font=("Consolas", 12))
        self.entry_engineer_surname.place(x=180, y=155, width=200, height=30)
        
        save = tk.Button(self, text="Save", font= ("Consolas", 15), anchor="center", command=self.save_butt_command)
        save.place(x=20, y=200, width=80, height=35)
        cancel = tk.Button(self, text="Cancel", font= ("Consolas", 15), anchor="center", command=self.cancel_butt_command)
        cancel.place(x=110, y=200, width=80, height=35)
    
    def save_butt_command(self):
        ALIAS_ENG = self.entry_engineer_alias.get()
        NAME_ENG = self.entry_engineer_name.get()
        SURNAME_ENG = self.entry_engineer_surname.get()
        self.entry_values = (ALIAS_ENG, NAME_ENG, SURNAME_ENG)
        sklad_manager.insert_to_engineers(self.entry_values)
        self.destroy()
        
    def cancel_butt_command(self):
        self.destroy()

class InsertWorkerDialog(tk.Toplevel):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.title("Insert worker:")
        self.entry_values = None
        width = 600
        height = 250
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstring = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstring)
        
        label = tk.Label(self, text="Insert worker: (please input relevant names)", font= ("Consolas", 14), anchor="center")
        label.place(x=15, y=15)
        
        label_worker_alias = tk.Label(self, text="Worker ALIAS:", font= ("Consolas", 12))
        label_worker_alias.place(x=15, y=65)
        self.entry_worker_alias = tk.Entry(self, font=("Consolas", 12))
        self.entry_worker_alias.place(x=180, y=65, width=200, height=30)
        
        label_worker_name = tk.Label(self, text="Worker name:", font= ("Consolas", 12))
        label_worker_name.place(x=15, y=110)
        self.entry_worker_name = tk.Entry(self, font=("Consolas", 12))
        self.entry_worker_name.place(x=180, y=110, width=200, height=30)
        
        label_worker_surname = tk.Label(self, text="Worker surname:", font= ("Consolas", 12))
        label_worker_surname.place(x=15, y=155)
        self.entry_worker_surname = tk.Entry(self, font=("Consolas", 12))
        self.entry_worker_surname.place(x=180, y=155, width=200, height=30)
        
        save = tk.Button(self, text="Save", font= ("Consolas", 15), anchor="center", command=self.save_butt_command)
        save.place(x=20, y=200, width=80, height=35)
        cancel = tk.Button(self, text="Cancel", font= ("Consolas", 15), anchor="center", command=self.cancel_butt_command)
        cancel.place(x=110, y=200, width=80, height=35)
    
    def save_butt_command(self):
        ALIAS_WORKER = self.entry_worker_alias.get()
        NAME_WORKER = self.entry_worker_name.get()
        SURNAME_WORKER = self.entry_worker_surname.get()
        self.entry_values = (ALIAS_WORKER, NAME_WORKER, SURNAME_WORKER)
        sklad_manager.insert_to_delnici(self.entry_values)
        self.destroy()
        
    def cancel_butt_command(self):
        self.destroy()

class StorageInDialog(tk.Toplevel):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.title("LOAD to GiBo:")
        self.entry_values = None
        width = 550
        height = 515
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstring = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstring)
        
        label_gibo = tk.Label(self, text="Number GiBo:", font= ("Consolas", 12))
        label_gibo.place(x=15, y=15)
        self.entry_gibo = tk.Entry(self, font=("Consolas", 12))
        self.entry_gibo.place(x=180, y=15, width=200, height=30)
        
        label_svs = tk.Label(self, text="SVS number:", font= ("Consolas", 12))
        label_svs.place(x=15, y=110)
        self.entry_svs = tk.Entry(self, font=("Consolas", 12))
        self.entry_svs.place(x=180, y=110, width=200, height=30)
        
        label_project = tk.Label(self, text="Project ALIAS:", font= ("Consolas", 12))
        label_project.place(x=15, y=155)
        load_projects_names = sklad_manager.load_combobox_projects()
        load_projects_names_list = [item[0] for item in load_projects_names]
        self.combobox_project = ttk.Combobox(self, font=("Consolas", 12), state="readonly", values=load_projects_names_list)
        self.combobox_project.place(x=180, y=155, width=200, height=30)
        
        label_engineer = tk.Label(self, text="Engineer ALIAS:", font= ("Consolas", 12))
        label_engineer.place(x=15, y=200)
        load_engineers_names = sklad_manager.load_combobox_engineers()
        load_engineers_names_list = [f'{item[0]} {item[1]}' for item in load_engineers_names]
        self.combobox_engineer = ttk.Combobox(self, font=("Consolas", 12), state='readonly', values=load_engineers_names_list)
        self.combobox_engineer.place(x=180, y=200, width=200, height=30)
        
        label_date = tk.Label(self, text="Date IN:", font= ("Consolas", 12))
        label_date.place(x=15, y=245)
        self.current_date = datetime.now().strftime("%Y-%m-%d")
        label_date_now = tk.Label(self, text=self.current_date, font= ("Consolas", 15))
        label_date_now.place(x=180, y=245)

        label_location = tk.Label(self, text="Location:", font= ("Consolas", 12))
        label_location.place(x=15, y=290)
        self.combobox_location = ttk.Combobox(self, font=("Consolas", 12), state='readonly', values=['Kopřivnice', 'Rožnov'])
        self.combobox_location.place(x=180, y=290, width=200, height=30)
        
        label_position = tk.Label(self, text="Position:", font= ("Consolas", 12))
        label_position.place(x=15, y=335)
        self.entry_position = tk.Entry(self, font=("Consolas", 12))
        self.entry_position.place(x=180, y=335, width=200, height=30)
        
        label_comment = tk.Label(self, text="Comment:", font= ("Consolas", 12))
        label_comment.place(x=15, y=380)
        self.entry_comment = tk.Entry(self, font=("Consolas", 12))
        self.entry_comment.place(x=180, y=380, width=200, height=30)
        
        label_worker = tk.Label(self, text="Worker ALIAS:", font= ("Consolas", 12))
        label_worker.place(x=15, y=425)
        self.worker_user = getpass.getuser()
        label_worker_user = tk.Label(self, text=self.worker_user, font= ("Consolas", 15))
        label_worker_user.place(x=180, y=425)
        
        save = tk.Button(self, text="Save", font= ("Consolas", 15), anchor="center", command=self.save_butt_command)
        save.place(x=20, y=470, width=80, height=35)
        cancel = tk.Button(self, text="Cancel", font= ("Consolas", 15), anchor="center", command=self.cancel_butt_command)
        cancel.place(x=110, y=470, width=80, height=35)
    
    def save_butt_command(self):
        NUM_GB = self.entry_gibo.get()
        TMA_NUMBER = self.entry_svs.get()
        PROJECT_ALIAS = sklad_manager.get_combobox_projects(self.combobox_project.get())[0]
        ALIAS_ENG = sklad_manager.get_combobox_engineers(self.combobox_engineer.get())[0]
        DATE_IN = self.current_date
        LOCATION = self.combobox_location.get()
        POSITION = self.entry_position.get()
        COMMENT = self.entry_comment.get()
        ALIAS_WORKER = self.worker_user
        
        self.entry_values = (NUM_GB, TMA_NUMBER, PROJECT_ALIAS, ALIAS_ENG, DATE_IN, LOCATION, POSITION, COMMENT, ALIAS_WORKER)
        print(self.entry_values)
        sklad_manager.insert_to_sklad(self.entry_values)
        self.destroy()
        
    def cancel_butt_command(self):
        self.destroy()
        
class EditDataDialog(tk.Toplevel):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.title("Edit data:")
        self.entry_values = None
        width = 550
        height = 515
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstring = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstring)
        
        label_ID = tk.Label(self, text="ID:", font= ("Consolas", 12))
        label_ID.place(x=15, y=15)
        load_edit_ids = sklad_manager.load_combobox_ID()
        load_edit_ids_list= sorted([item for item in load_edit_ids])
        self.combobox_ID = ttk.Combobox(self, font=("Consolas", 12), state= 'readonly', values= load_edit_ids_list)
        self.combobox_ID.place(x=180, y=15, width=60, height=30)
        self.combobox_ID.bind("<<ComboboxSelected>>", lambda event: self.update_form_on_selection(self.combobox_ID.get()))
        
        label_gibo = tk.Label(self, text="Number GiBo:", font= ("Consolas", 12))
        label_gibo.place(x=15, y=65)
        self.entry_gibo = tk.Entry(self, font=("Consolas", 12))
        self.entry_gibo.place(x=180, y=65, width=200, height=30)
        
        label_svs = tk.Label(self, text="SVS number:", font= ("Consolas", 12))
        label_svs.place(x=15, y=110)
        self.entry_svs = tk.Entry(self, font=("Consolas", 12))
        self.entry_svs.place(x=180, y=110, width=200, height=30)
        
        label_project = tk.Label(self, text="Project ALIAS:", font= ("Consolas", 12))
        label_project.place(x=15, y=155)
        load_projects_names = sklad_manager.load_combobox_projects()
        load_projects_names_list = [item[0] for item in load_projects_names]
        self.combobox_project = ttk.Combobox(self, font=("Consolas", 12), state="readonly", values=load_projects_names_list)
        self.combobox_project.place(x=180, y=155, width=200, height=30)
        
        label_engineer = tk.Label(self, text="Engineer ALIAS:", font= ("Consolas", 12))
        label_engineer.place(x=15, y=200)
        load_engineers_names = sklad_manager.load_combobox_engineers()
        load_engineers_names_list = [f'{item[0]} {item[1]}' for item in load_engineers_names]
        self.combobox_engineer = ttk.Combobox(self, font=("Consolas", 12), state='readonly', values=load_engineers_names_list)
        self.combobox_engineer.place(x=180, y=200, width=200, height=30)
        
        label_date = tk.Label(self, text="Date IN:", font= ("Consolas", 12))
        label_date.place(x=15, y=245)
        self.label_date_now = tk.Entry(self, font= ("Consolas", 12))
        self.label_date_now.place(x=180, y=245, width=200, height=30)
        # self.entry_date = tk.Entry(self, font=("Consolas", 12))
        # self.entry_date.place(x=180, y=155, width=200, height=30)
        
        label_location = tk.Label(self, text="Location:", font= ("Consolas", 12))
        label_location.place(x=15, y=290)
        self.combobox_location = ttk.Combobox(self, font=("Consolas", 12), state='readonly', values=['Kopřivnice', 'Rožnov'])
        self.combobox_location.place(x=180, y=290, width=200, height=30)
        
        label_position = tk.Label(self, text="Position:", font= ("Consolas", 12))
        label_position.place(x=15, y=335)
        self.entry_position = tk.Entry(self, font=("Consolas", 12))
        self.entry_position.place(x=180, y=335, width=200, height=30)
        
        label_comment = tk.Label(self, text="Comment:", font= ("Consolas", 12))
        label_comment.place(x=15, y=380)
        self.entry_comment = tk.Entry(self, font=("Consolas", 12))
        self.entry_comment.place(x=180, y=380, width=200, height=30)
        
        label_worker = tk.Label(self, text="Worker ALIAS:", font= ("Consolas", 12))
        label_worker.place(x=15, y=425)
        self.worker_user = getpass.getuser()
        label_worker_user = tk.Label(self, text=self.worker_user, font= ("Consolas", 15))
        label_worker_user.place(x=180, y=425)
        
        # SCRAP Checkbutton
        label_scrap = tk.Label(self, text="Vyšrotováno:", font=("Consolas", 13))
        label_scrap.place(x=200, y=470)
        self.scrap_var = tk.IntVar()
        self.scrap_checkbutton = tk.Checkbutton(self, text='', variable=self.scrap_var, onvalue=1, offvalue=0, font=("Consolas", 12))
        self.scrap_checkbutton.config(command=self.update_scrap_text)
        self.scrap_checkbutton.place(x=330, y=472)
        
        save = tk.Button(self, text="Save", font= ("Consolas", 15), anchor="center", command=self.save_butt_command)
        save.place(x=20, y=470, width=80, height=35)
        cancel = tk.Button(self, text="Cancel", font= ("Consolas", 15), anchor="center", command=self.cancel_butt_command)
        cancel.place(x=110, y=470, width=80, height=35)
    
    def update_form_on_selection(self, selected_id):
        self.get_data_by_id(selected_id)
    
    def get_data_by_id(self, selected_id):
        id_data = sklad_manager.find_combobox_IDdata(selected_id)
        id_data_list = id_data
        self.entry_gibo.delete(0, tk.END)
        self.entry_svs.delete(0, tk.END)
        self.label_date_now.delete(0, tk.END)
        self.entry_position.delete(0, tk.END)
        self.entry_comment.delete(0, tk.END)
        self.label_date_now.insert('0', id_data_list[0][3])
        self.entry_gibo.insert(0, id_data_list[0][1])
        self.entry_svs.insert('0', id_data_list[0][2])
        self.combobox_project.set(id_data_list[0][4])
        self.combobox_engineer.set(f'{id_data_list[0][5]} {id_data_list[0][6]}')
        self.combobox_location.set(id_data_list[0][9])
        self.entry_position.insert('0', id_data_list[0][10])
        self.entry_comment.insert('0', id_data_list[0][11])
        self.scrap_var.set(id_data_list[0][12])
        self.update_scrap_text()
    
    def update_scrap_text(self):
        if self.scrap_var.get() == 1:
            self.scrap_checkbutton.config(text="ANO")
        else:
            self.scrap_checkbutton.config(text="NE")
    
    def save_butt_command(self):
        NUM_GB = self.entry_gibo.get()
        TMA_NUMBER = self.entry_svs.get()
        PROJECT_ALIAS = self.combobox_project.get()
        #print(PROJECT_ALIAS)
        ALIAS_ENG = sklad_manager.get_combobox_engineers(self.combobox_engineer.get())[0]
        #print(ALIAS_ENG)
        
        DATE_IN = self.label_date_now.get()
        LOCATION = self.combobox_location.get()
        POSITION = self.entry_position.get()
        COMMENT = self.entry_comment.get()
        ALIAS_WORKER = self.worker_user
        SCRAP = self.scrap_var.get()
        
        self.entry_values = [NUM_GB, TMA_NUMBER, str(PROJECT_ALIAS), ALIAS_ENG, DATE_IN, LOCATION, POSITION, COMMENT, ALIAS_WORKER, SCRAP]
        print(self.entry_values)
        sklad_manager.edit_id_data(self.entry_values, self.combobox_ID.get())
        self.destroy()
        
    def cancel_butt_command(self):
        self.destroy()
   
class AppSklad(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('Sklad - GiBo - zkušebna')
        self.inserted_project_value = None
        self.inserted_engineer_value = None
        self.inserted_worker_value = None
        #setting window size
        width=1200
        height=800
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)
        self.set_fonts()
        self.numbers_of_gb = list(range(200,300))

        treeview_style = ttk.Style()
        treeview_style.configure('Treeview', font = self.set_fonts(12))

        title_app_text = tk.Label(self, text='Storage MANAGER - GiBo info', bg='black', fg='White', anchor='center', font=self.set_fonts(25))
        title_app_text.place(x=0, y=0, width=width, height=50)

        insert_project_button = tk.Button(self, text='Insert project', font=self.set_fonts(12), command=self.insert_project)
        insert_project_button.place(x=510, y=60, width=150, height=40)
        
        insert_eng_button = tk.Button(self, text='Insert engineer', font=self.set_fonts(12), command=self.insert_engineer)
        insert_eng_button.place(x=180, y=60, width=150, height=40)

        insert_worker_button = tk.Button(self, text='Insert worker', font=self.set_fonts(12), command=self.insert_worker)
        insert_worker_button.place(x=345, y=60, width=150, height=40)
        
        storage_in_button = tk.Button(self, text='Storage IN', foreground= 'red', background= 'yellow', font=self.set_fonts(15), command=self.storage_in)
        storage_in_button.place(x=15, y=60, width=150, height=40)

        edit_data_button = tk.Button(self, text='Edit data', foreground= 'blue', background= 'yellow', font=self.set_fonts(15), command=self.edit_data)
        edit_data_button.place(x=675, y=60, width=150, height=40)
        
        self.combobox_get_data = ttk.Combobox(self, font=("Consolas", 15), state="readonly", values='')
        self.combobox_get_data.place(x=880, y=110, width=75, height=40)
        
        get_data_db_button = tk.Button(self, text='Scrap GB', font=self.set_fonts(12), command=self.delete_GB)
        get_data_db_button.place(x=970, y=110, width=200, height=40)

        separator = ttk.Separator(self, orient='horizontal')
        separator.pack(fill='x', padx=3, pady=165)
        
        self.find_fulltext = tk.Entry(self, font=self.set_fonts(12))
        self.find_fulltext.place(x=15, y=125, width=400, height=30)
        
        fulltext_button = tk.Button(self, text='FIND', font=self.set_fonts(12), command=self.fulltext_find)
        fulltext_button.place(x=430, y=125, width=70, height=30)
        
        expire_filter_button = tk.Button(self, text=' UPDATE EXPIRE', font=self.set_fonts(15), command=self.expire_find)
        expire_filter_button.place(x=975, y=435, width=180, height=35)

        result_label = tk.Label(self, text='ALL DATA in storage:', font=self.set_fonts(15), anchor='center', background='yellow')
        result_label.place(x=25, y=435, width=270, height=35)
        
        separator_t = ttk.Separator(self, orient='horizontal')
        separator_t.pack(fill='x', padx=3, pady=95)
        
        expire_label = tk.Label(self, text='EXPIRE DATA in storage:', font=self.set_fonts(15), anchor='center', background='red')
        expire_label.place(x=25, y=175, width=270, height=35)
        
        empty_gb_label = tk.Label(self, text='Empty GB:', font=self.set_fonts(12), anchor='center', background='grey')
        empty_gb_label.place(x=310, y=175, width=100, height=30)
        
        self.empty_gb_label_text = tk.StringVar()
        self.empty_gb_label_text.set('')
        empty_gb_result = tk.Label(self, textvariable=self.empty_gb_label_text, font=self.set_fonts(14), anchor='w', background='grey', foreground= 'white')
        empty_gb_result.place(x=410, y=175, width=750, height=30)
        
        update_button = tk.Button(self, text='Update DB', command=self.update_table, background='white', font=self.set_fonts(15))
        update_button.place(x=520, y=435, width=450, height=35)
        
        self.frame_db = tk.Frame(self)
        self.frame_db.place(x = 15, y = 480, width = 1170, height = 300)
        self.vsb = ttk.Scrollbar(self.frame_db, orient='vertical')
        self.vsb.pack(side='right', fill='y')
        
        self.frame_exp = tk.Frame(self)
        self.frame_exp.place(x = 15, y = 220, width = 1170, height = 200)
        self.vsb_exp = ttk.Scrollbar(self.frame_exp, orient='vertical')
        self.vsb_exp.pack(side='right', fill='y')
        
        self.tree = ttk.Treeview(self.frame_db, yscrollcommand=self.vsb.set)
        self.tree['columns'] = ('#0', '#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9')
        self.tree.heading('#0', text='ID')
        self.tree.heading('#1', text='č. GiBo')
        self.tree.heading('#2', text='TMA/č.dílu')
        self.tree.heading('#4', text='Projekt')
        self.tree.heading('#5', text='Jméno ENG')
        self.tree.heading('#3', text='Datum expirace')
        self.tree.heading('#6', text='Jméno WORKER')
        self.tree.heading('#7', text='Lokace')
        self.tree.heading('#8', text='Komentář')
        self.tree.heading('#9', text='šrot?')
        self.tree.column('#0', width = 50, anchor = 'w', stretch=False)
        self.tree.column('#1', width = 50, anchor = 'center', stretch=False)
        self.tree.column('#2', width = 135, anchor = 'center', stretch=False)
        self.tree.column('#3', width = 115, anchor = 'center', stretch=False)
        self.tree.column('#4', width = 85, anchor = 'center', stretch=False)
        self.tree.column('#5', width = 150, anchor = 'center', stretch=False)
        self.tree.column('#6', width = 150, anchor = 'center', stretch=False)
        self.tree.column('#7', width = 100, anchor = 'center', stretch=False)
        self.tree.column('#8', width = 200, anchor = 'center', stretch=False)
        self.tree.column('#9', width = 50, anchor = 'center', stretch=False)
        self.tree.pack(side = 'left', fill='y', expand=False)
        self.vsb.config(command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.vsb.set)
        self.tree.bind("<Control-c>", lambda event: self.copy_to_clipboard(self.tree))
                
        self.tree_exp = ttk.Treeview(self.frame_exp, yscrollcommand=self.vsb_exp.set)
        self.tree_exp['columns'] = ('#0', '#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9')
        self.tree_exp.heading('#0', text='ID')
        self.tree_exp.heading('#1', text='č. GiBo')
        self.tree_exp.heading('#2', text='TMA/č.dílu')
        self.tree_exp.heading('#4', text='Projekt')
        self.tree_exp.heading('#5', text='Jméno ENG')
        self.tree_exp.heading('#3', text='Datum expirace')
        self.tree_exp.heading('#6', text='Jméno WORKER')
        self.tree_exp.heading('#7', text='Lokace')
        self.tree_exp.heading('#8', text='Komentář')
        self.tree_exp.heading('#9', text='Šrot?')
        self.tree_exp.column('#0', width = 50, anchor = 'w', stretch=False)
        self.tree_exp.column('#1', width = 50, anchor = 'center', stretch=False)
        self.tree_exp.column('#2', width = 135, anchor = 'center', stretch=False)
        self.tree_exp.column('#3', width = 115, anchor = 'center', stretch=False)
        self.tree_exp.column('#4', width = 85, anchor = 'center', stretch=False)
        self.tree_exp.column('#5', width = 150, anchor = 'center', stretch=False)
        self.tree_exp.column('#6', width = 150, anchor = 'center', stretch=False)
        self.tree_exp.column('#7', width = 100, anchor = 'center', stretch=False)
        self.tree_exp.column('#8', width = 200, anchor = 'center', stretch=False)
        self.tree_exp.column('#9', width=50, anchor='center', stretch=False)
        self.tree_exp.place(x = 15, y = 220, width = 1170, height = 200)
        self.tree_exp.pack(side = 'left', fill='both', expand=True)
        self.vsb_exp.config(command=self.tree_exp.yview)
        self.tree_exp.bind("<Control-c>", lambda event: self.copy_to_clipboard(self.tree_exp))
   
        self.show_data = False
        self.create_dataframe()
        self.expire_find()
        self.update_gb_numbers()
        
        self.toggle_button = tk.Button(self, text="Show Scrap", command=self.toggle_data, font=self.set_fonts(12), background='lightblue')
        self.toggle_button.place(x=400, y=435, width=100, height=35)

        self.populate_data(self.show_data)
        
    #------------------------------------------------------------------------------------
    
    def toggle_data(self):
        self.show_data = not self.show_data
        self.populate_data(self.show_data)
        self.toggle_button.config(text="Hide Scrap" if self.show_data else "Show Scrap")
        
    def populate_data(self, show_data):
        rows = sklad_manager.populate_data_db(show_data)
        processed_rows = self.process_rows(rows)
        self.update_tree(self.tree, processed_rows)
        self.sort_treeview_column(self.tree, '#9')
        rows = sklad_manager.populate_data_db_exp(show_data)
        processed_rows = self.process_rows(rows)
        self.update_tree(self.tree_exp, processed_rows)
        self.sort_treeview_column(self.tree_exp, '#9')
    
    def sort_treeview_column(self, treeview, col_index):
        data = [(treeview.set(child, col_index), child) for child in treeview.get_children('')]
        data.sort(reverse=True)
        for i, item in enumerate(data):
            treeview.move(item[1], '', i)
    
    def process_rows(self, rows):
        processed_rows = []
        for row in rows:
            merged_values_eng = f"{row[5]} {row[6]}"
            merged_values_tech = f"{row[7]} {row[8]}"
            scrap_status = 'ANO' if row[11] == 1 else 'NE'
            processed_rows.append((row[0], row[1], row[2], row[3], row[4], merged_values_eng, merged_values_tech, row[9], row[10], scrap_status))
        return processed_rows

    def update_tree(self, tree, processed_rows):
        for row in tree.get_children():
            tree.delete(row)
        for row in processed_rows:
            tree.insert('', 'end', text=row[0], values=(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))

    def create_dataframe(self):       
        rows = sklad_manager.query()
        processed_rows = self.process_rows(rows)
        self.update_tree(self.tree, processed_rows)
        self.populate_data(self.show_data)
        self.sort_treeview_column(self.tree, '#9')
        
    def update_gb_numbers(self):    
        gb_numbers_full = sklad_manager.gb_numbers()
        self.combobox_get_data.config(values=gb_numbers_full)
        self.empty_numbers = '|'.join(map(str,[num for num in self.numbers_of_gb if num not in gb_numbers_full]))
        self.empty_gb_label_text.set(f'{self.empty_numbers}')

    def fulltext_find(self):
        search_string = self.find_fulltext.get()
        if search_string.isdigit():
            search_string = int(search_string)
        
        filter_data = sklad_manager.filter_query(search_string)
        processed_rows = self.process_rows(filter_data)
        self.update_tree(self.tree, processed_rows)
        self.populate_data(self.show_data)
        self.sort_treeview_column(self.tree, '#9')

    def expire_find(self):        
        rows = sklad_manager.get_expiration_data()
        processed_rows_exp = self.process_rows(rows)
        self.update_tree(self.tree_exp, processed_rows_exp)
        self.populate_data(self.show_data)
        self.sort_treeview_column(self.tree_exp, '#9')
            
    def update_table(self):
        rows = sklad_manager.query()
        processed_rows = self.process_rows(rows)
        self.update_tree(self.tree, processed_rows)
        self.update_gb_numbers()
        self.populate_data(self.show_data)
        self.sort_treeview_column(self.tree, '#9')
        self.sort_treeview_column(self.tree_exp, '#9')
        
    def edit_data(self):
        edit_data_window = EditDataDialog(self)
        edit_data_window.focus()
        
    def insert_project(self):
        insert_project_window = InsertProjectDialog(self)
        insert_project_window.focus()
        
    def insert_engineer(self):
        insert_engineer_window = InsertEngineerDialog(self)
        insert_engineer_window.focus()
    
    def insert_worker(self):
        insert_worker_window = InsertWorkerDialog(self)
        insert_worker_window.focus()
    
    def storage_in(self):
        storage_in_window = StorageInDialog(self)
        storage_in_window.focus()
    
    def control_db(self):
        try:
            sklad_manager.create_tables()
            messagebox.showinfo("Úspěch", "Databáze existuje a je připravena k práci.")
        except Exception as e:
            messagebox.showerror("Chyba", f"Chyba kontrole DB: {e}")

    def delete_GB(self):
        del_gb = int(self.combobox_get_data.get())
        sklad_manager.delete_gb_all(del_gb)

    def get_data(self):
        gbnumber = int(self.combobox_get_data.get())
        try:
            data = sklad_manager.query_all()
            messagebox.showinfo("Úspěch", "Podívej se do terminálu app.")
            for rows in data:
                if gbnumber == rows[1]:
                    print(f"GB č.{rows[1]}, č. dílu/testu: {rows[2]}, projekt: {rows[4]}, pozn.: {rows[10]}")
        except Exception as e:
            messagebox.showerror("Chyba", f"Chyba při získávání dat: {e}")

    def copy_to_clipboard(self, name_treeview):
        selected_items = name_treeview.selection()
        if selected_items:
            text_to_copy = ''
            for item in selected_items:
                row_values = name_treeview.item(item, 'values')
                row_text = '\t'.join(map(str, row_values))
                text_to_copy += row_text + '\n'
            self.clipboard_clear()
            self.clipboard_append(text_to_copy.strip())

    def set_fonts(self, font_size=12):
        ft = tkFont.Font(family='Consolas', size=font_size)
        return ft
    
if __name__ == '__main__':
    this_folder = os.path.dirname(os.path.abspath(__file__))
    db_path = 'storage_db\\sklad_GB.db'
    sklad_manager = SkladManager(db_path)
    self = AppSklad()
    self.mainloop()