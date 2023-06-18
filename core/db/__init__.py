from core.db.database import session


def get_database():
    db = session()  # pylint: disable=invalid-name
    try:
        yield db
    finally:
        db.close()
