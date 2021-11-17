from datetime import datetime
import re


class DataFormatValidator:

    # 入力された日付のチェックとフォーマット
    def validate_date(self, date):
        date = datetime.strptime(date, "%Y-%m-%d")
        return date.strftime("%Y-%m-%d")

    # 入力された名前のチェック
    def validate_name(self, name):
        pattern = re.compile("[a-zA-Z]")
        if not name.isalpha():
            raise Exception("名前に記号が含まれています。")
        if len(name) != len(re.findall(pattern, name)):
            raise Exception("名前に全角文字が含まれています。")

    # 入力された文字列の長さをチェック
    def validate_length(self, text):
        if len(text) > 50:
            raise ValueError
