import sqlite3


class DBAccessor:

    # テーブルの作成
    def create_table(self, database_name):

        with sqlite3.connect(database_name) as connection:
            cursor = connection.cursor()
            cursor.execute(
                "CREATE TABLE IF NOT EXISTS report_check_status (name TEXT, browsing_date TEXT, daily_report_date TEXT,times INTEGER)"
            )

    # データの追加登録
    def insert_data(self, database_name, name, browsing_date, daily_report_date):

        with sqlite3.connect(database_name) as connection:
            cursor = connection.cursor()
            # 同じ名前の登録数をカウント
            cursor.execute("SELECT * from report_check_status WHERE name = ?", [name])
            times = len(cursor.fetchall()) + 1
            # DBにデータを登録
            cursor.execute(
                "INSERT INTO report_check_status VALUES(?,?,?,?)",
                [name, browsing_date, daily_report_date, times],
            )
            connection.commit()

    # 全データ表示
    def select_data(self, database_name):
        with sqlite3.connect(database_name) as connection:
            cursor = connection.cursor()
            print(
                "{:^28s} | {:^9s} | {:^7s} | {:^3s}".format(
                    "名前", "閲覧日", "日報の日付", "閲覧回数"
                )
            )
            print(
                f"-----------------------------------------------------------------------"
            )
            for data in cursor.execute(
                "select * from report_check_status ORDER BY browsing_date ASC"
            ):
                print(
                    "{:^30s} | {:^12s} | {:^12s} | {:^5d}".format(
                        data[0], data[1], data[2], data[3]
                    )
                )
