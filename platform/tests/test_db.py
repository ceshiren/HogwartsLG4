from backend import db


def test_create_table():
    db.create_all()