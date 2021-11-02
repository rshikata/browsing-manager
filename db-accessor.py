import sqlite3


class DBAccessor:

    # テーブルの作成
    def create_Table(self):
        try:
            connection = sqlite3.connect("ojt.db")
            cursor = connection.cursor()
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS report_check_status (name TEXT, date TEXT)"
            )
        except sqlite3.Error as e:
            raise e
        finally:
            connection.close()

    # データの追加登録
    def insert_data(self, name, date):
        try:
            connection = sqlite3.connect("ojt.db")
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO report_check_status (name, date) VALUES(?,?)", (name, date)
            )
            connection.commit()
        except sqlite3.Error as e:
            raise e
        finally:
            connection.close()
