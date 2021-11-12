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
        operator.operate_database(DATABASE_NAME, mode)

    except ValueError as e:
        print(e)
        print("入力が不正です。")
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
