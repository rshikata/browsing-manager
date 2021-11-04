from datetime import datetime


class DataFormatValidator:

    # 入力された日付のフォーマットをチェック
    def valid_date(self, date):
        datetime.strptime(date, "%Y-%m-%d")
