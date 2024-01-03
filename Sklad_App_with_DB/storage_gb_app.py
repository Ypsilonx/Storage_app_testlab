import sqlite3
import os
import getpass

# NUM_GB = 0
# TMA_NUMBER = ''
# PROJECT_ALIAS = ''
# RESPONS_ENG = ''
# DATE_IN_STORAGE = ''
# LOCATION = ''
# POSITION = ''
# COMMENT = ''
# WORKER = getpass.getuser()

# # variables for table delnici:
# ALIAS_WORKER = ''
# NAME_WORKER = ''
# SURNAME_WORKER = ''

# # variables for table engineers:
# ALIAS_ENG = ''
# NAME_ENG = ''
# SURNAME_ENG = ''

# # variables for table projects:
# PROJECT = ''
# PROJECT_NAME = ''

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
            SELECT LOWER(sklad.Num_GB), LOWER(sklad.TMA_number), LOWER(sklad.Date_expiration), LOWER(projects.Project_alias), LOWER(engineers.Name_eng), LOWER(engineers.SurName_eng), LOWER(delnici.Name_worker), LOWER(delnici.SurName_worker), LOWER(sklad.Location)
                FROM sklad
                JOIN delnici ON LOWER(sklad.Alias_worker) = LOWER(delnici.Alias_worker)
                JOIN engineers ON LOWER(sklad.Alias_eng) = LOWER(engineers.Alias_eng)
                JOIN projects ON LOWER(sklad.Project_alias) = LOWER(projects.Project_alias);
        '''
        self.cursor.execute(load_query)
        return self.cursor.fetchall()
    
    def load_combobox_projects(self):
        self.cursor.execute("SELECT Project_name FROM projects")
        return self.cursor.fetchall()
    
    def get_combobox_projects(self, data):
        self.cursor.execute("SELECT Project_alias FROM projects WHERE Project_name = ?", (data,))
        return self.cursor.fetchone()[0]
    
    def load_combobox_engineers(self):
        self.cursor.execute("SELECT Name_eng, SurName_eng FROM engineers")
        return self.cursor.fetchall()
    
    def get_combobox_engineers(self, data):
        fullname = data.split()
        self.cursor.execute("SELECT Alias_eng FROM engineers WHERE Name_eng = ? AND SurName_eng = ?", (fullname[0], fullname[1]))
        return self.cursor.fetchone()[0]

    def close_connection(self):
        self.conn.close()

# Example usage:
if __name__ == "__main__":
    db_path = os.path.join('G:\\Locations_EU\\OST\\EU_S\\SVS\\01_Personal\\CCT\\APP_list\\Sklad_App_with_DB\\storage_db', 'sklad_GB.db')
    
    sklad_manager = SkladManager(db_path)

    # # Example data for sklad table
    # data_sklad = (NUM_GB, TMA_NUMBER, PROJECT, RESPONS_ENG, DATE_IN_STORAGE, LOCATION, POSITION, COMMENT, WORKER)
    # data_delnici = (ALIAS_WORKER, NAME_WORKER, SURNAME_WORKER)
    # data_engineers = (ALIAS_ENG, NAME_ENG, SURNAME_ENG)
    # data_projects = (PROJECT, PROJECT_NAME)
    
    # # Insert data to sklad table
    # sklad_manager.insert_to_sklad(data_sklad)
    # sklad_manager.insert_to_delnici(data_delnici)
    # sklad_manager.insert_to_engineers(data_engineers)
    # sklad_manager.insert_to_projects(data_projects)
    
    # print(sklad_manager.query())
    
    sklad_manager.close_connection()
