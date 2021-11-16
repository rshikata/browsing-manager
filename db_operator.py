from db_accessor import DBAccessor
from data_format_validator import DataFormatValidator


class DBOperator:

    # 操作選択
    def select_mode(self):
        print("[操作選択] 1: データ追加 2: 閲覧")
        mode = input("操作選択 >>")
        return int(mode)

    # DBかテーブル存在しない場合は作成
    def create_database(self, DATABASE_NAME):
        db = DBAccessor()
        # DB、テーブルの作成
        db.create_table(DATABASE_NAME)

    # 追加情報を取得し、DBに追加
    def add_data(self, DATABASE_NAME):
        db = DBAccessor()
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
        db.insert_data(DATABASE_NAME, reader_name, browsing_date, daily_report_date)

    # DBのデータを全て表示
    def display_data(self, DATABASE_NAME):
        db = DBAccessor()
        # データの取得、表示
        db.select_data(DATABASE_NAME)
