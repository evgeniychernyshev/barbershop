import os
import waitress
from flask import Flask, render_template, request, url_for, make_response
from werkzeug.utils import redirect
from app import db


def start():
    app = Flask(__name__)
    app.config['IMAGE_DIR'] = os.path.join('static')
    DATABASE_URL = 'db.sqlite'

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
        pass

    @app.route('/manager')
    def manage():
        search = request.args.get('search')
        if search:
            result = db.search(DATABASE_URL, search)
            return render_template("manager.html", barbers=result, search=search)
        return render_template("manager.html", barbers=db.get_barbers(DATABASE_URL))

    @app.route('/manager/<barber_id>/edit')
    def barber_edit(barber_id):
        pass

    @app.route('/manager/<barber_id>/save', methods=['POST'])
    def barber_save(barber_id):
        pass

    @app.route('/manager/<barber_id>/remove', methods=['POST'])
    def barber_remove(barber_id):
        pass

    if os.getenv('APP_ENV') == 'PROD' and os.getenv('PORT'):
        waitress.serve(app, port=os.getenv('PORT'))
    else:
        app.run(port=9877, debug=True)


if __name__ == '__main__':
    start()
