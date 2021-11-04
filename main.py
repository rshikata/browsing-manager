from datetime import datetime
from db_accessor import DBAccessor

# from data_format_validator import DataFormatValidator


def main():

    print("[操作選択] 1: データ追加 2: 閲覧")
    mode = input("操作選択 >>")
    mode = int(mode)

    db = DBAccessor()
    # validator = DataFormatValidator()

    try:
        # テーブル作成
        db.create_table()

        # データの追加
        if mode == 1:
            name = input("名前 >>")
            date = input("日付(????-??-??) >>")

            # validator.valid_date(date)
            datetime.strptime(date, "%Y-%m-%d")
            if name.isalpha():
                db.insert_data(name, date)
            else:
                print("名前の入力が誤りです")

        elif mode == 2:
            db.select_data()

        else:
            print("操作選択が不正です。")
    except ValueError as e:
        print(e)
        print("日付のフォーマットが誤りです。")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
