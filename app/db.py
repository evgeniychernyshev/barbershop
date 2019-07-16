import sqlite3
import uuid


def open_db(db_url):
    db = sqlite3.connect(db_url)
    db.row_factory = sqlite3.Row
    return db


def get_barbers(db_url):
    with open_db(db_url) as db:
        barbers = db.cursor().execute(
            'SELECT b.id, b.name, b.level, s.price, b.img_path FROM t_barbers b, t_service s WHERE b.level = s.level and b.is_working = 1'
        ).fetchall()
        return barbers


def get_barbers_for_manager(db_url):
    with open_db(db_url) as db:
        barbers = db.cursor().execute(
            'SELECT b.id, b.name, b.level, b.is_working, b.img_path, (SELECT COUNT(*) FROM t_clients c WHERE c.barber_id = b.id) clients FROM t_barbers b'
        ).fetchall()
        return barbers


def save_barber_new(db_url, barber_id, name, level, img_path, is_working):
    with open_db(db_url) as db:
            db.cursor().execute(
                'INSERT INTO t_barbers (id, name, level, img_path, is_working) VALUES (:barber_id, :name, :level, :img_path, :is_working)', {'barber_id': str(barber_id), 'name': str(name), 'level': str(level), 'img_path': str(img_path), 'is_working': int(is_working)}
            )
            db.commit()


def save_barber(db_url, barber_id, name, level, img_path, is_working):
    with open_db(db_url) as db:
        db.cursor().execute(
            'UPDATE t_barbers SET name = :name, level = :level, img_path = :img_path, is_working = :is_working WHERE id = :barber_id', {'barber_id': str(barber_id), 'name': str(name), 'level': str(level), 'img_path': str(img_path), 'is_working': int(is_working)}
        )
        db.commit()


def dismiss_barber(db_url, barber_id):
    with open_db(db_url) as db:
        db.cursor().execute(
            'UPDATE t_barbers SET is_working = 0 WHERE id = :barber_id', {'barber_id': str(barber_id)}
        )
        db.commit()


def search(db_url, search):
    search.strip()
    search += '%'
    with open_db(db_url) as db:
        result = db.cursor().execute(
            'SELECT b.id, b.name, b.level, s.price, b.img_path FROM t_barbers b, t_service s WHERE b.level = s.level AND (b.name LIKE :search OR b.level LIKE :search)', {'search': search}
        ).fetchall()
        return result


def search_by_id(db_url, barber_id):
    with open_db(db_url) as db:
        result = db.cursor().execute(
            'SELECT b.id, b.name, b.level, b.img_path, s.price, b.img_path FROM t_barbers b, t_service s WHERE b.id = :barber_id and s.level = b.level', {'barber_id': barber_id}
        ).fetchone()
        return result


def get_time(db_url, barber_id):
    with open_db(db_url) as db:
        result = db.cursor().execute(
            'SELECT t.time FROM t_timetable t LEFT JOIN t_clients tc on t.id = tc.time_id WHERE t.barber_id = :barber_id and tc.id is null', {'barber_id': barber_id}
        ).fetchall()
        return result


def create_client(db_url, client_id, barber_id, time_id, name, phone):
    with open_db(db_url) as db:
        db.cursor().execute(
            'INSERT INTO t_clients (id, name, phone, time_id, barber_id) VALUES (:id, :name, :phone, :time_id, :barber_id)', {'id': str(client_id), 'name': str(name), 'phone': str(phone), 'time_id': str(time_id), 'barber_id': str(barber_id)}
        )
        db.commit()


def create_timetable(db_url, barber_id):
    with open_db(db_url) as db:
        start = 10
        end = 18
        while start <= end:
            id = uuid.uuid4()
            db.cursor().execute(
                'INSERT INTO t_timetable VALUES (:id, :start, :barber_id)', {'id': str(id), 'start': int(start), 'barber_id': str(barber_id)}
            )
            start += 1
        db.commit()


def get_client_by_id(db_url, client_id):
    with open_db(db_url) as db:
        result = db.cursor().execute(
            'SELECT c.name, (SELECT tt.time FROM t_timetable tt WHERE tt.id = c.time_id) time, (SELECT b.name FROM t_barbers b WHERE b.id = c.barber_id) barber_name FROM t_clients c WHERE c.id = :client_id', {'client_id': str(client_id)}
        ).fetchone()
        return result


def get_time_id(db_url, barber_id, time):
    with open_db(db_url) as db:
        result = db.cursor().execute(
            'SELECT t.id FROM t_timetable t WHERE t.time = :time and t.barber_id = :barber_id', {'time': time, 'barber_id': barber_id}
        ).fetchone()
        return result

