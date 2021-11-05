import os
from dotenv import load_dotenv
from db_accessor import DBAccessor
from data_format_validator import DataFormatValidator


def main():

    # .envを読み込む
    load_dotenv()
    DATABASE_NAME = os.getenv("DATABASE_NAME")

    print("[操作選択] 1: データ追加 2: 閲覧")
    mode = input("操作選択 >>")
    mode = int(mode)

    db = DBAccessor()
    validator = DataFormatValidator()

    try:
        # テーブル作成
        db.create_table(DATABASE_NAME)

        # データの追加
        if mode == 1:
            name = input("名前 >>")
            validator.validate_name(name)
            validator.validate_length(name)
            date = input("日付(????-??-??) >>")
            date = validator.validate_date(date)

            # データベースに登録
            db.insert_data(DATABASE_NAME, name, date)

        elif mode == 2:
            # データの取得、表示
            db.select_data(DATABASE_NAME)

        else:
            print("操作選択が不正です。")

    except ValueError as e:
        print(e)
        print("入力が不正です。")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
