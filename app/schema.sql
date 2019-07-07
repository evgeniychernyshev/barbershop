CREATE TABLE t_barbers (
  id TEXT PRIMARY KEY,
  name TEXT NOT NULL,
  level TEXT NOT NULL,
  img_path TEXT
);

CREATE TABLE t_timetable (
    id TEXT PRIMARY KEY,
    time INTEGER NOT NULL,
    barber_id TEXT NOT NULL,
    FOREIGN KEY (barber_id) REFERENCES t_barbers(id)
);

CREATE TABLE t_service (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    price INTEGER NOT NULL,
    level TEXT NOT NULL
);

CREATE TABLE t_clients (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    phone TEXT NOT NULL,
    barber_id TEXT NOT NULL,
    FOREIGN KEY (barber_id) REFERENCES t_barbers(id)
);