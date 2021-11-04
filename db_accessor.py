import sqlite3


class DBAccessor:

    # テーブルの作成
    def create_table(self):

        with sqlite3.connect("ojt.db") as connection:
            cursor = connection.cursor()
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS report_check_status (name TEXT, date TEXT)"
            )

    # データの追加登録
    def insert_data(self, name, date):

        with sqlite3.connect("ojt.db") as connection:
            cursor = connection.cursor()
            cursor.execute(
                "INSERT INTO report_check_status (name, date) VALUES(?,?)", (name, date)
            )
            connection.commit()

    # 全データ表示
    def select_data(self):
        with sqlite3.connect("ojt.db") as connection:
            cursor = connection.cursor()
            for data in cursor.execute(
                "select * from report_check_status ORDER BY date ASC"
            ):
                print(data)
