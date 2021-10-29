import sqlite3
class DBAccecer: 

    def __init__(self,dbName):
        self.__dbName = dbName

    # テーブルの作成
    def createTable(self):
        conn = sqlite3.connect(self.__dbName) 
        cur = conn.cursor()
        cur.execute('CREAT TABLE IF NOT EXISTS report_check_status (name TEXT, date TEXT)')
        conn.commit()
        conn.close()

+