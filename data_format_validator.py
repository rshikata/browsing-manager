from datetime import datetime


class DataFormatValidator:

    # 入力された日付のチェックとフォーマット
    def validate_date(self, date):
        date = datetime.strptime(date, "%Y-%m-%d")
        return date.strftime("%Y-%m-%d")

    # 入力された名前に記号が含まれていないかチェック
    def validate_name(self, name):
        if not name.isalpha():
            raise ValueError

    # 入力された文字列の長さをチェック
    def validate_length(self, text):
        if len(text) > 50:
            raise ValueError
