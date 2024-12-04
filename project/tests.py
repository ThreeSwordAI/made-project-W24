import os
import sqlite3
import pandas as pd
import unittest


DATA_DIR = "../data/"
SQLITE_FILE = os.path.join(DATA_DIR, "traffic_data_cleaned.sqlite")
TARGET_COLUMNS = [
    'date', 'time', 'zone', 'race', 'sex', 'type', 'arrest_made', 
    'warning_issued', 'outcome', 'contraband_found', 'contraband_drugs', 
    'contraband_weapons', 'contraband_alcohol', 'contraband_other', 
    'frisk_performed', 'search_conducted', 'search_basis', 'reason_for_search', 
    'reason_for_stop', 'vehicle_make', 'vehicle_model', 'state'
]

class TestDatabase(unittest.TestCase):
    
    # Check for the traffic_data_cleaned.sqlite file
    def test_pipeline(self):
        self.assertTrue(os.path.exists(SQLITE_FILE), "Output SQLite file does not exist.")


    # check in the .sqlite file for the traffic_data table
    def test_table_exists(self):
        conn = sqlite3.connect(SQLITE_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        conn.close()
        self.assertIn(('traffic_data',), tables, "Table 'traffic_data' does not exist in the database.")


    # check if the columns are in the table or not
    def test_columns_exist(self):
        conn = sqlite3.connect(SQLITE_FILE)
        cursor = conn.cursor()
        cursor.execute("PRAGMA table_info(traffic_data);")
        columns = [info[1] for info in cursor.fetchall()]
        conn.close()
        self.assertEqual(set(columns), set(TARGET_COLUMNS), "Table columns do not match the expected columns.")


    # check if the table has all the rows
    def test_row_count(self):
        conn = sqlite3.connect(SQLITE_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM traffic_data;")
        row_count = cursor.fetchone()[0]
        conn.close()
        #print(f"Row count in the table: {row_count}")
        self.assertGreater(row_count, 0, "There are no rows.")



if __name__ == "__main__":
    unittest.main()