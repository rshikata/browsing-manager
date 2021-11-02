import importlib

DBAccessor = importlib.import_module("db-accessor")
DateFormatValidator = importlib.import_module("data-format-validator")


def main():

    print("[操作選択] 1: データ追加 2: 閲覧")
    mode = input("操作選択 >>")
    mode = int(mode)
    db = DBAccessor.DBAccessor()
    validator = DateFormatValidator.DateFormatValidator()

    try:
        # テーブル作成
        db.create_Table()

        # データの追加
        if mode == 1:
            name = input("名前 >>")
            date = input("日付(????-??-??) >>")
            validator.valid_date(date)
            db.insert_data(name, date)

        # elif mode == 2:

        else:
            print("操作選択が不正です。")
    except ValueError as e:
        print(e)
        print("日付のフォーマットが誤りです。")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
