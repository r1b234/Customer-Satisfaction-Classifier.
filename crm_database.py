import sqlite3
import pandas as pd

DB_NAME = "crm_database.db"

def init_crm_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS surveys (
            survey_id INTEGER PRIMARY KEY,
            customer_name TEXT,
            tier TEXT,
            comment TEXT,
            sentiment_score REAL,
            classification TEXT,
            date TEXT
        )
    '''
    )
    conn.commit()
    
    cursor.execute("SELECT COUNT(*) FROM surveys")
    if cursor.fetchone()[0] == 0:
        df = pd.read_csv("survey_data.csv")
        df.to_sql("surveys", conn, if_exists="append", index=False)
        
    conn.close()

def fetch_crm_data():
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql("SELECT * FROM surveys", conn)
    conn.close()
    return df
