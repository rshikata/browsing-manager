import DBAccecer


def main():
    db = DBAccecer.DBAccecer("ojt")

    try:
        db.createTable()
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()