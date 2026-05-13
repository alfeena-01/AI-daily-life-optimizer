import sqlite3
import pandas as pd

DB_PATH = "data/activity.db"

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS activity (
        date TEXT,
        sleep_hours REAL,
        steps INTEGER,
        screen_time REAL
    )
    """)
    conn.commit()
    conn.close()

def insert_activity(date, sleep_hours, steps, screen_time):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO activity (date, sleep_hours, steps, screen_time)
    VALUES (?, ?, ?, ?)
    """, (date, sleep_hours, steps, screen_time))
    conn.commit()
    conn.close()

def get_all_activity():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("SELECT * FROM activity", conn)
    conn.close()
    return df

def get_weekly_summary():
    conn = sqlite3.connect(DB_PATH)
    df = pd.read_sql_query("""
        SELECT 
            AVG(sleep_hours) AS avg_sleep,
            SUM(steps) AS total_steps,
            AVG(screen_time) AS avg_screen
        FROM activity
        WHERE date >= date('now', '-7 day')
    """, conn)
    conn.close()
    return df.iloc[0].to_dict()
