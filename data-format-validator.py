from datetime import datetime


class DataFormatValidator:

    # 入力された日付のフォーマットをチェック
    def valid_date(self, date):
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError as e:
            raise e
