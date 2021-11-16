from db_accessor import DBAccessor
from data_format_validator import DataFormatValidator


class DBOperator:

    # 操作選択
    def select_mode(self):
        print("[操作選択] 1: データ追加 2: 閲覧")
        mode = input("操作選択 >>")
        return int(mode)

    # DBかテーブルが存在しない場合は作成
    def create_database(self, database_name):
        accessor = self._create_db_accessor()
        # テーブルの作成
        accessor.create_table(database_name)

    # 追加情報を取得し、DBに追加
    def add_data(self, database_name):
        accessor = self._create_db_accessor()
        validator = DataFormatValidator()

        # 閲覧者名
        print("追加情報：名前(ローマ字)")
        last_name = input("Last Name >>")
        first_name = input("First Name >>")
        validator.validate_name(last_name)
        validator.validate_name(first_name)
        reader_name = f"{last_name} {first_name}"
        validator.validate_length(reader_name)
        # 閲覧日
        browsing_date = input("閲覧日(????-??-??) >>")
        browsing_date = validator.validate_date(browsing_date)
        # 閲覧した日報の日付
        daily_report_date = input("日報の日付(????-??-??) >>")
        daily_report_date = validator.validate_date(daily_report_date)

        # データベースに登録
        accessor.insert_data(
            database_name, reader_name, browsing_date, daily_report_date
        )

    # DBのデータを全て表示
    def display_data(self, database_name):
        accessor = self._create_db_accessor()

        # データの取得
        registered_data = accessor.select_data(database_name)

        # データを表示
        print("{:^28s} | {:^9s} | {:^7s} | {:^3s}".format("名前", "閲覧日", "日報の日付", "閲覧回数"))
        print(
            f"-----------------------------------------------------------------------"
        )

        for i in range(len(registered_data)):
            data = []
            for j in range(4):
                data.append(registered_data[i][j])

            print(
                "{:^30s} | {:^12s} | {:^12s} | {:^5d}".format(
                    data[0], data[1], data[2], data[3]
                )
            )

    # インスタンスの作成
    def _create_db_accessor(self):
        return DBAccessor()
