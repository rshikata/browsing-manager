import os
from dotenv import load_dotenv
from db_operator import DBOperator
from data_format_validator import DataFormatValidator


def main():

    # .envを読み込む
    load_dotenv()
    DATABASE_NAME = os.getenv("DATABASE_NAME")

    try:
        operator = DBOperator()
        mode = operator.select_mode()
        operator.create_database(DATABASE_NAME)
        if mode == 1:
            # データベースに登録
            operator.add_data(DATABASE_NAME)

        elif mode == 2:
            # データの取得、表示
            operator.display_data(DATABASE_NAME)

        else:
            print("操作選択が不正です。")

    except ValueError as e:
        print(e)
        print("入力が不正です。")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
