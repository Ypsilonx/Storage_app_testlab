import sqlite3
import os
from datetime import datetime, timedelta

class SkladManager:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS sklad (
                ID INTEGER PRIMARY KEY,
                Num_GB INTEGER NOT NULL,
                TMA_number TEXT UNIQUE NOT NULL,
                Project_alias TEXT NOT NULL,
                Alias_eng TEXT NOT NULL,
                Date_IN DATE,
                Date_expiration DATE,
                Location TEXT NOT NULL CHECK (Location IN ('Kopřivnice', 'Rožnov')),
                Position TEXT,
                Comment TEXT,
                Alias_worker TEXT NOT NULL
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS delnici (
                Alias_worker TEXT UNIQUE NOT NULL PRIMARY KEY,
                Name_worker TEXT,
                SurName_worker TEXT
            )
        ''')
        
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS engineers (
                Alias_eng TEXT UNIQUE NOT NULL PRIMARY KEY,
                Name_eng TEXT,
                SurName_eng TEXT
            )
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS projects (
                Project_alias TEXT UNIQUE NOT NULL PRIMARY KEY,
                Project_name TEXT NOT NULL
            )
        ''')

        self.cursor.execute('''
            CREATE TRIGGER IF NOT EXISTS set_expiration
            AFTER INSERT ON sklad
            FOR EACH ROW
            BEGIN
                UPDATE sklad
                SET Date_expiration = DATE(NEW.Date_IN, '+1 year')
                WHERE ID = NEW.ID AND NEW.Date_IN IS NOT NULL;
            END;
        ''')

        self.cursor.execute('''
            CREATE TRIGGER IF NOT EXISTS update_expiration
            AFTER UPDATE ON sklad
            FOR EACH ROW
            BEGIN
                UPDATE sklad
                SET Date_expiration = DATE(NEW.Date_IN, '+1 year')
                WHERE ID = NEW.ID AND NEW.Date_IN IS NOT NULL;
            END;
        ''')

        self.conn.commit()

    def insert_to_sklad(self, data):
        insert_query = '''
            INSERT INTO sklad (Num_GB, TMA_number, Project_alias, Alias_eng, Date_IN, Location, Position, Comment, Alias_worker)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        '''
        self.cursor.execute(insert_query, data)
        self.conn.commit()
        
    def insert_to_delnici(self, data):
        insert_query = '''
            INSERT INTO delnici (Alias_worker, Name_worker, SurName_worker)
            VALUES (?, ?, ?)
        '''
        self.cursor.execute(insert_query, data)
        self.conn.commit()
        
    def insert_to_engineers(self, data):
        insert_query = '''
            INSERT INTO engineers (Alias_eng, Name_eng, SurName_eng)
            VALUES (?, ?, ?)
        '''
        self.cursor.execute(insert_query, data)
        self.conn.commit()
        
    def insert_to_projects(self, data):
        insert_query = '''
            INSERT INTO projects (Project_alias, Project_name)
            VALUES (?, ?)
        '''
        self.cursor.execute(insert_query, data)
        self.conn.commit()

    def query(self):
        load_query = '''
            SELECT (sklad.ID), (sklad.Num_GB), (sklad.TMA_number), (sklad.Date_expiration), (projects.Project_alias), (engineers.Name_eng), (engineers.SurName_eng), (delnici.Name_worker), (delnici.SurName_worker), (sklad.Location), (sklad.Comment), (sklad.Scrap)
                FROM sklad
                JOIN delnici ON (sklad.Alias_worker) = (delnici.Alias_worker)
                JOIN engineers ON (sklad.Alias_eng) = (engineers.Alias_eng)
                JOIN projects ON (sklad.Project_alias) = (projects.Project_alias);
        '''
        self.cursor.execute(load_query)
        return self.cursor.fetchall()
    
    def query_all(self):
        load_query = '''
            SELECT (sklad.ID), (sklad.Num_GB), (sklad.TMA_number), (sklad.Date_expiration), (projects.Project_alias), (engineers.Name_eng), (engineers.SurName_eng), (delnici.Name_worker), (delnici.SurName_worker), (sklad.Location), (sklad.Comment), (sklad.Scrap)
                FROM sklad
                JOIN delnici ON (sklad.Alias_worker) = (delnici.Alias_worker)
                JOIN engineers ON (sklad.Alias_eng) = (engineers.Alias_eng)
                JOIN projects ON (sklad.Project_alias) = (projects.Project_alias);
        '''
        self.cursor.execute(load_query)
        return self.cursor.fetchall()
    
    def get_expiration_data(self, dny_pred_expiraci=0):
        dnes = datetime.now()
        load_query = '''
            SELECT (sklad.ID), (sklad.Num_GB), (sklad.TMA_number), (sklad.Date_expiration), (projects.Project_alias), (engineers.Name_eng), (engineers.SurName_eng), (delnici.Name_worker), (delnici.SurName_worker), (sklad.Location), (sklad.Comment), (sklad.Scrap)
                FROM sklad
                JOIN delnici ON (sklad.Alias_worker) = (delnici.Alias_worker)
                JOIN engineers ON (sklad.Alias_eng) = (engineers.Alias_eng)
                JOIN projects ON (sklad.Project_alias) = (projects.Project_alias)
                WHERE Date_expiration <= ?;
        '''
        self.cursor.execute(load_query, (dnes + timedelta(days=dny_pred_expiraci),))
        return self.cursor.fetchall()
    
    def filter_query(self, search_string):
        load_query = f'''
            SELECT sklad.ID, sklad.Num_GB, sklad.TMA_number, sklad.Date_expiration, projects.Project_alias, engineers.Name_eng, engineers.SurName_eng, delnici.Name_worker, delnici.SurName_worker, sklad.Location, sklad.Comment, sklad.Scrap
                FROM sklad
                JOIN delnici ON sklad.Alias_worker = delnici.Alias_worker
                JOIN engineers ON sklad.Alias_eng = engineers.Alias_eng
                JOIN projects ON sklad.Project_alias = projects.Project_alias
            WHERE sklad.Num_GB = '{search_string}' OR sklad.TMA_number = '{search_string}' OR sklad.Date_expiration = '{search_string}' OR projects.Project_alias = '{search_string}' OR engineers.Name_eng = '{search_string}' OR engineers.SurName_eng = '{search_string}' OR delnici.Name_worker = '{search_string}' OR delnici.SurName_worker = '{search_string}' OR sklad.Location = '{search_string}' OR sklad.Scrap = '{search_string}';        '''
        self.cursor.execute(load_query)
        return self.cursor.fetchall()
    
    def load_combobox_projects(self):
        self.cursor.execute("SELECT Project_name FROM projects")
        return self.cursor.fetchall()
    
    def get_combobox_projects(self, data):
        self.cursor.execute("SELECT Project_alias FROM projects WHERE Project_name = ?", (data,))
        return self.cursor.fetchall()[0]
    
    def load_combobox_engineers(self):
        self.cursor.execute("SELECT Name_eng, SurName_eng FROM engineers")
        return self.cursor.fetchall()
    
    def get_combobox_engineers(self, data):
        fullname = data.split()
        self.cursor.execute("SELECT Alias_eng FROM engineers WHERE Name_eng = ? AND SurName_eng = ?", (fullname[0], fullname[1]))
        return self.cursor.fetchall()[0]

    def load_combobox_ID(self):
        self.cursor.execute("SELECT ID FROM sklad")
        return self.cursor.fetchall()
    
    def find_combobox_IDdata(self, selected_id):
        self.cursor.execute('''SELECT (sklad.ID), (sklad.Num_GB), (sklad.TMA_number), (sklad.Date_IN), (projects.Project_alias), (engineers.Name_eng), (engineers.SurName_eng), (delnici.Name_worker), (delnici.SurName_worker), (sklad.Location), (sklad.Position), (sklad.Comment), (sklad.Scrap)
                                FROM sklad  
                                JOIN delnici ON (sklad.Alias_worker) = (delnici.Alias_worker)
                                JOIN engineers ON (sklad.Alias_eng) = (engineers.Alias_eng)
                                JOIN projects ON (sklad.Project_alias) = (projects.Project_alias)
                                WHERE ID = ?''', (selected_id,))
        return self.cursor.fetchall()
    
    # def edit_id_data(self, data, selected_id):
    #     edit_query = f'''
    #         UPDATE sklad
    #         SET Num_GB = '{data[0]}', TMA_number = '{data[1]}', Project_alias = '{data[2]}', Alias_eng = '{data[3]}', Date_IN = '{data[4]}', Location = '{data[5]}', Position = '{data[6]}', Comment = '{data[7]}', Alias_worker = '{data[8]}', Scrap = '{data[9]}'
    #         WHERE ID = '{selected_id}';
    #     '''
    #     self.cursor.execute(edit_query)
    #     self.conn.commit()
        
    def edit_id_data(self, data, selected_id):
        edit_query = '''
            UPDATE sklad
            SET Num_GB = ?, TMA_number = ?, Project_alias = ?, Alias_eng = ?, Date_IN = ?, Location = ?, Position = ?, Comment = ?, Alias_worker = ?, Scrap = ?
            WHERE ID = ?;
        '''
        self.cursor.execute(edit_query, (data[0], data[1], data[2], data[3], data[4], data[5], data[6], data[7], data[8], data[9], selected_id))
        self.conn.commit()
        
    def gb_numbers(self):
        self.cursor.execute('SELECT DISTINCT Num_GB FROM sklad WHERE Scrap != 1;')
        return [row[0] for row in self.cursor.fetchall()]
    
    def populate_data_db(self, show_data):    
        if show_data:
            load_query = f'''
            SELECT sklad.ID, sklad.Num_GB, sklad.TMA_number, sklad.Date_expiration, projects.Project_alias, engineers.Name_eng, engineers.SurName_eng, delnici.Name_worker, delnici.SurName_worker, sklad.Location, sklad.Comment, sklad.Scrap
                FROM sklad
                JOIN delnici ON sklad.Alias_worker = delnici.Alias_worker
                JOIN engineers ON sklad.Alias_eng = engineers.Alias_eng
                JOIN projects ON sklad.Project_alias = projects.Project_alias
            ;
            '''
            self.cursor.execute(load_query)
        else:
            load_query = '''
            SELECT sklad.ID, sklad.Num_GB, sklad.TMA_number, sklad.Date_expiration, projects.Project_alias, engineers.Name_eng, engineers.SurName_eng, delnici.Name_worker, delnici.SurName_worker, sklad.Location, sklad.Comment, sklad.Scrap
                FROM sklad
                JOIN delnici ON sklad.Alias_worker = delnici.Alias_worker
                JOIN engineers ON sklad.Alias_eng = engineers.Alias_eng
                JOIN projects ON sklad.Project_alias = projects.Project_alias
            WHERE sklad.Scrap = 0;
            '''
            self.cursor.execute(load_query)
        return self.cursor.fetchall()
    
    def populate_data_db_exp(self, show_data, dny_pred_expiraci=0):    
        if show_data:
            dnes = datetime.now()
            load_query = '''
                SELECT (sklad.ID), (sklad.Num_GB), (sklad.TMA_number), (sklad.Date_expiration), (projects.Project_alias), (engineers.Name_eng), (engineers.SurName_eng), (delnici.Name_worker), (delnici.SurName_worker), (sklad.Location), (sklad.Comment), (sklad.Scrap)
                    FROM sklad
                    JOIN delnici ON (sklad.Alias_worker) = (delnici.Alias_worker)
                    JOIN engineers ON (sklad.Alias_eng) = (engineers.Alias_eng)
                    JOIN projects ON (sklad.Project_alias) = (projects.Project_alias)
                    WHERE Date_expiration <= ?;
            '''
            self.cursor.execute(load_query, (dnes + timedelta(days=dny_pred_expiraci),))
        else:
            dnes = datetime.now()
            load_query = '''
                SELECT (sklad.ID), (sklad.Num_GB), (sklad.TMA_number), (sklad.Date_expiration), (projects.Project_alias), (engineers.Name_eng), (engineers.SurName_eng), (delnici.Name_worker), (delnici.SurName_worker), (sklad.Location), (sklad.Comment), (sklad.Scrap)
                    FROM sklad
                    JOIN delnici ON (sklad.Alias_worker) = (delnici.Alias_worker)
                    JOIN engineers ON (sklad.Alias_eng) = (engineers.Alias_eng)
                    JOIN projects ON (sklad.Project_alias) = (projects.Project_alias)
                    WHERE Date_expiration <= ? AND Scrap = 0;
            '''
            self.cursor.execute(load_query, (dnes + timedelta(days=dny_pred_expiraci),))
        return self.cursor.fetchall()
    
    def delete_gb_all(self, selected_gb):
        delete_query = f'''
            UPDATE sklad
            SET Scrap = 1
            WHERE Num_GB = {selected_gb}
        '''
        self.cursor.execute(delete_query)
        self.conn.commit()
    
    def close_connection(self):
        self.conn.close()

# Example usage:
if __name__ == "__main__":
    this_folder = os.path.dirname(os.path.abspath(__file__)) # získání cesty k tomuto souboru
    db_path = 'storage_db\\sklad_GB.db'
    sklad_manager = SkladManager(db_path)

    sklad_manager.close_connection()
