import sqlite3


def open_db(db_url):
    db = sqlite3.connect(db_url)
    db.row_factory = sqlite3.Row
    return db


def get_barbers(db_url):
    with open_db(db_url) as db:
        barbers = db.cursor().execute(
            'SELECT t_barbers.id, t_barbers.name, t_barbers.level, t_service.price, count(t_clients.id) as clients FROM t_barbers, t_service, t_clients WHERE t_barbers.level = t_service.level and t_barbers.id = t_clients.barber_id'
        ).fetchall()
        return barbers


def save_barber(db_url, barber_id, name, level):
    with open_db(db_url) as db:
        if barber_id is not 'new':
            db.cursor().execute(
                'UPDATE t_barbers SET name = :name, level = :level WHERE id = :barber_id', {'id': barber_id, 'name': name, 'level': level}
            )
        else:
            db.cursor().execute(
                'INSERT INTO t_barbers VALUES (:id, :name, :level)', {'barber_id': barber_id, 'name': name, 'level': level}
            )


def remove_barber(db_url, barber_id):
    with open_db(db_url) as db:
        db.cursor().execute(
            'DELETE FROM t_barbers WHERE id = :barber_id', {'id': barber_id}
        )


def search(db_url, search):
    search.strip()
    search += '%'
    with open_db(db_url) as db:
        result = db.cursor().execute(
            'SELECT t_barbers.id, t_barbers.name, t_barbers.level, t_service.price, count(t_clients.id) as clients FROM t_barbers, t_service, t_clients WHERE t_barbers.level = t_service.level AND (t_barbers.name LIKE :search OR t_barbers.level LIKE :search) and t_clients.barber_id = t_barbers.id', {'search': search}
        ).fetchall()
        return result


def search_by_id(db_url, barber_id):
    with open_db(db_url) as db:
        result = db.cursor().execute(
            'SELECT t_barbers.id, t_barbers.name, t_barbers.level, t_barbers.img_path, t_service.price, count(t_clients.id) as clients FROM t_barbers, t_service, t_clients WHERE t_barbers.id = :barber_id and t_service.level = t_barbers.level and t_clients.barber_id = t_barbers.id', {'barber_id': barber_id}
        ).fetchone()
        return result


def get_time(db_url, barber_id):
    with open_db(db_url) as db:
        result = db.cursor().execute(
            'SELECT time FROM t_timetable WHERE barber_id = :barber_id', {'barber_id': barber_id}
        ).fetchall()
        return result

