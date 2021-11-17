import sqlite3


class DBAccessor:

    # テーブルの作成
    def create_table(self, database_name):

        with sqlite3.connect(database_name) as connection:
            cursor = connection.cursor()
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS report_check_status (reader_name TEXT, browsing_date TEXT, daily_report_date TEXT,times INTEGER)"
            )

    # データの追加登録
    def insert_data(self, database_name, reader_name, browsing_date, daily_report_date):

        with sqlite3.connect(database_name) as connection:
            cursor = connection.cursor()
            # 同じ名前の登録数をカウント
            cursor.execute(
                "SELECT * from report_check_status WHERE reader_name = ?", [reader_name]
            )
            times = len(cursor.fetchall()) + 1
            # DBにデータを登録
            cursor.execute(
                "INSERT INTO report_check_status VALUES(?,?,?,?)",
                [reader_name, browsing_date, daily_report_date, times],
            )
            connection.commit()

    # 全データ表示
    def select_data(self, database_name):
        with sqlite3.connect(database_name) as connection:
            cursor = connection.cursor()

            cursor.execute(
                "select * from report_check_status ORDER BY browsing_date ASC"
            )
            # 全データを取得
            registered_data = cursor.fetchall()

            return registered_data
