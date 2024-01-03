import os
import tkinter as tk
import pandas as pd
import getpass
import tkinter.font as tkFont
from tkinter import ttk
from tkinter import messagebox
from pandastable import Table
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
        
        label = tk.Label(self, text="Inser project: (please input relevant project)", font= ("Consolas", 14), anchor="center")
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
        
        label = tk.Label(self, text="Inser engineer: (please input relevant names)", font= ("Consolas", 14), anchor="center")
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
        
        label = tk.Label(self, text="Inser worker: (please input relevant names)", font= ("Consolas", 14), anchor="center")
        label.place(x=15, y=15)
        
        label_worker_alias = tk.Label(self, text="Engineer ALIAS:", font= ("Consolas", 12))
        label_worker_alias.place(x=15, y=65)
        self.entry_worker_alias = tk.Entry(self, font=("Consolas", 12))
        self.entry_worker_alias.place(x=180, y=65, width=200, height=30)
        
        label_worker_name = tk.Label(self, text="Engineer name:", font= ("Consolas", 12))
        label_worker_name.place(x=15, y=110)
        self.entry_worker_name = tk.Entry(self, font=("Consolas", 12))
        self.entry_worker_name.place(x=180, y=110, width=200, height=30)
        
        label_worker_surname = tk.Label(self, text="Engineer surname:", font= ("Consolas", 12))
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
        # self.entry_worker = tk.Entry(self, font=("Consolas", 12))
        # self.entry_worker.place(x=180, y=155, width=200, height=30)
        
        save = tk.Button(self, text="Save", font= ("Consolas", 15), anchor="center", command=self.save_butt_command)
        save.place(x=20, y=470, width=80, height=35)
        cancel = tk.Button(self, text="Cancel", font= ("Consolas", 15), anchor="center", command=self.cancel_butt_command)
        cancel.place(x=110, y=470, width=80, height=35)
    
    def save_butt_command(self):
        NUM_GB = self.entry_gibo.get()
        TMA_NUMBER = self.entry_svs.get()
        PROJECT_ALIAS = sklad_manager.get_combobox_projects(self.combobox_project.get())
        #print(PROJECT_ALIAS)
        ALIAS_ENG = sklad_manager.get_combobox_engineers(self.combobox_engineer.get())
        #print(ALIAS_ENG)
        DATE_IN = self.current_date
        LOCATION = self.combobox_location.get()
        POSITION = self.entry_position.get()
        COMMENT = self.entry_comment.get()
        ALIAS_WORKER = self.worker_user
        
        self.entry_values = (NUM_GB, TMA_NUMBER, PROJECT_ALIAS, ALIAS_ENG, DATE_IN, LOCATION, POSITION, COMMENT, ALIAS_WORKER)
        sklad_manager.insert_to_sklad(self.entry_values)
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

        title_app_text = tk.Label(self, text='Storage MANAGER - GiBo info', bg='#ff0000', fg='#ffffff', anchor='w', font=self.set_fonts(25))
        title_app_text.place(x=0, y=0, width=width, height=50)

        insert_project_button = tk.Button(self, text='Insert project', font=self.set_fonts(12), command=self.insert_project)
        insert_project_button.place(x=15, y=60, width=150, height=40)
        
        insert_eng_button = tk.Button(self, text='Insert engineer', font=self.set_fonts(12), command=self.insert_engineer)
        insert_eng_button.place(x=180, y=60, width=150, height=40)

        insert_worker_button = tk.Button(self, text='Insert worker', font=self.set_fonts(12), command=self.insert_worker)
        insert_worker_button.place(x=345, y=60, width=150, height=40)
        
        storage_in_button = tk.Button(self, text='Storage IN', font=self.set_fonts(15), command=self.storage_in)
        storage_in_button.place(x=510, y=60, width=150, height=40)

        create_db_button = tk.Button(self, text='Create/Control storage', font=self.set_fonts(12), command=self.control_db)
        create_db_button.place(x=935, y=60, width=250, height=40)
        
        get_data_db_button = tk.Button(self, text='Získat data', font=self.set_fonts(12), command=self.get_data)
        get_data_db_button.place(x=935, y=110, width=250, height=40)

        separator = ttk.Separator(self, orient='horizontal')
        separator.pack(fill='x', padx=3, pady=105)
        
        self.find_fulltext = tk.Entry(self, font=self.set_fonts(12))
        self.find_fulltext.place(x=15, y=125, width=400, height=30)
        
        fulltext_button = tk.Button(self, text='FIND', font=self.set_fonts(12), command=self.fulltext_find)
        fulltext_button.place(x=430, y=125, width=70, height=30)

        self.create_dataframe()
    
        update_button = tk.Button(self, text='Updat DB', command=self.update_table)
        update_button.place(x=30, y=290, width=150, height=30)

    def create_dataframe(self):
        self.data = sklad_manager.query()
        self.columns = ["Č. GB", "Č. testu", "Datum expirace", "Projekt", "Jméno ENG", "Přijemní ENG", "Jméno TECH", "Přijmení TECH", "Lokace"]
        self.df = pd.DataFrame(self.data, columns=self.columns)
        column_name_eng = "Jméno ENG"
        column_surname_eng = "Přijemní ENG"
        column_name_worker = "Jméno TECH"
        column_surname_worker = "Přijmení TECH"
        self.df["Odpovědná osoba"] = self.df[column_name_eng] + " " + self.df[column_surname_eng]
        self.df["Zaskladnil"] = self.df[column_name_worker] + " " + self.df[column_surname_worker]
        self.df = self.df.drop(columns=[column_name_eng, column_surname_eng])
        self.df = self.df.drop(columns=[column_name_worker, column_surname_worker])
        self.df["Č. GB"] = self.df["Č. GB"].astype(int)
        self.df_sorted = self.df.sort_values(by='Č. GB')

        result_pole = tk.Frame(self, borderwidth=5, relief='ridge')
        result_pole.place(x=15, y=335, width=1170, height=450)
        # Vytvoření tk.Table widgetu
        self.table = Table(result_pole, dataframe=self.df_sorted)
        self.table.show()
    
    def fulltext_find(self):
        search_string = self.find_fulltext.get()
        new_columns = ["Č. GB", "Č. testu", "Datum expirace", "Projekt","Odpovědná osoba", "Zaskladnil", "Lokace"]
        self.df["Č. GB"] = self.df["Č. GB"].astype(int)
        self.df_sorted = self.df.sort_values(by='Č. GB')
        condition = self.df_sorted[new_columns].apply(lambda x: x.astype(str).str.contains(search_string, case=False, na=False)).any(axis=1)
        result_df = self.df_sorted[condition]
        self.table.destroy()
        result_pole = tk.Frame(self, borderwidth=5, relief='ridge')
        result_pole.place(x=15, y=335, width=1170, height=450)
        self.table = Table(result_pole, dataframe=result_df)
        self.table.show()
        
    def update_table(self):
        # Aktualizace dat v DataFrame z databáze
        self.create_dataframe()

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

    def get_data(self):
        try:
            # Volání metody pro získání dat ze třídy pro práci s databází
            data = sklad_manager.query()
            messagebox.showinfo("Úspěch", f"Kuk do terminálu app.{print(data)}")
            # Zobrazení dat v GUI (implementuj podle potřeby)
        except Exception as e:
            messagebox.showerror("Chyba", f"Chyba při získávání dat: {e}")

    def set_fonts(self, font_size=12):
        ft = tkFont.Font(family='Consolas', size=font_size)
        return ft
    
    
if __name__ == '__main__':
    db_path = os.path.join('G:\\Locations_EU\\OST\\EU_S\\SVS\\01_Personal\\CCT\\APP_list\\Sklad_App_with_DB\\storage_db', 'sklad_GB.db')
    sklad_manager = SkladManager(db_path)
    self = AppSklad()
    self.mainloop()