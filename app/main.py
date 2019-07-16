import os
import uuid
import waitress
from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect
from app import db


def start():
    app = Flask(__name__)
    app.config['IMAGE_DIR'] = os.path.join('app/static')
    DATABASE_URL = 'app/db.sqlite'

    @app.route('/')
    def index():
        search = request.args.get('search')
        if search:
            result = db.search(DATABASE_URL, search)
            return render_template("index.html", barbers=result, search=search)
        return render_template("index.html", barbers=db.get_barbers(DATABASE_URL))

    @app.route('/client/<barber_id>/registration')
    def registration(barber_id):
        barber = db.search_by_id(DATABASE_URL, barber_id)
        times = []
        temp = db.get_time(DATABASE_URL, barber_id)
        for row in temp:
            times.append(row[0])
        return render_template("registration.html", barber=barber, times=times)

    @app.route('/client/<barber_id>/register', methods=['POST'])
    def register(barber_id):
        client_id = uuid.uuid4()
        time = db.get_time_id(DATABASE_URL, barber_id, int(request.form['time']))
        time_id = time[0]
        name = str(request.form['name'])
        phone = str(request.form['phone'])
        db.create_client(DATABASE_URL, client_id, barber_id, time_id, name, phone)
        client = db.get_client_by_id(DATABASE_URL, client_id)
        return render_template("registred_success.html", client=client)


    @app.route('/manager')
    def manage():
        search = request.args.get('search')
        if search:
            result = db.search(DATABASE_URL, search)
            return render_template("manager.html", barbers=result, search=search)
        return render_template("manager.html", barbers=db.get_barbers_for_manager(DATABASE_URL))

    @app.route('/manager/<barber_id>/edit')
    def barber_edit(barber_id):
        if barber_id == 'new':
            return render_template("barber_new.html")
        else:
            barber = db.search_by_id(DATABASE_URL, barber_id)
            return render_template("barber_edit.html", barber=barber)

    @app.route('/manager/<barber_id>/save', methods=['POST'])
    def barber_save(barber_id):
        name = str(request.form['name'])
        level = str(request.form['level'])
        is_working = 1
        img = request.files['img']
        image = img.filename
        path = os.path.join(app.config['IMAGE_DIR'], image)
        img.save(path)

        if barber_id == 'new':
            barber_id = uuid.uuid4()
            db.save_barber_new(DATABASE_URL, barber_id, name, level, path, is_working)
            db.create_timetable(DATABASE_URL, barber_id)
        else:
            db.save_barber(DATABASE_URL, barber_id, name, level, path, is_working)
        return redirect(url_for('manage', barbers=db.get_barbers(DATABASE_URL)))

    @app.route('/manager/<barber_id>/dismiss', methods=['POST'])
    def barber_dismiss(barber_id):
        db.dismiss_barber(DATABASE_URL, barber_id)
        return redirect(url_for('manage', barbers=db.get_barbers(DATABASE_URL)))

    if os.getenv('APP_ENV') == 'PROD' and os.getenv('PORT'):
        waitress.serve(app, port=os.getenv('PORT'))
    else:
        app.run(port=9877, debug=True)


if __name__ == '__main__':
    start()
