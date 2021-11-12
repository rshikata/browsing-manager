from db_accessor import DBAccessor
from data_format_validator import DataFormatValidator


class DBOperator:

    # 操作選択
    def select_mode(self):
        print("[操作選択] 1: データ追加 2: 閲覧")
        mode = input("操作選択 >>")
        return int(mode)

    # modeに対応したDB操作を行う
    def operate_database(self, DATABASE_NAME, mode):

        db = DBAccessor()
        validator = DataFormatValidator()

        # テーブル作成
        db.create_table(DATABASE_NAME)

        # データの追加
        if mode == 1:
            # 閲覧者名
            print("追加情報：名前")
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

        elif mode == 2:
            # データの取得、表示
            db.select_data(DATABASE_NAME)

        else:
            print("操作選択が不正です。")
