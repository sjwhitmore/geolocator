import os
import sqlite3
from contextlib import closing
from flask import Flask, g, session, redirect, url_for, escape, request, jsonify, render_template

#create app
app = Flask(__name__, static_url_path="/")
app.config.from_object(__name__)

# Load default config and override config from an environment variable
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, 'locations.db'),
    #disable DEBUG before production!!
    DEBUG=True,
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))
# define DASHBOARD_SETTINGS if we want to config file, silent means don't complain
app.config.from_envvar('GEOLOCATOR_SETTINGS', silent=True)

# Connect to database.
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()


@app.route('/get_location')
def get_location():
	sid = request.args.get('sid', 0, type=str)
	date = request.args.get('date', 0, type=str)
	visitor_lat = request.args.get('visitor_lat', 0, type=int)
	visitor_long = request.args.get('visitor_long', 0, type=int)
	visitor_city = request.args.get('visitor_city', 0, type=str)
	visitor_region = request.args.get('visitor_region', 0, type=str)
	visitor_country = request.args.get('visitor_country', 0, type=str)
	visitor_countrycode = request.args.get('visitor_countrycode', 0, type=str)
	# ADD TO DB
	g.db.execute('insert into locations (sid, date, visitor_lat, visitor_long, visitor_city, visitor_region, visitor_country, visitor_countrycode) values (?, ?, ?, ?, ?, ?, ?, ?)',
                 [sid, date, visitor_lat, visitor_long, visitor_city, visitor_region, visitor_country, visitor_countrycode])
	g.db.commit()
	#on success:
	return jsonify(result="Successfully stored!")

@app.route('/')
def index():
	return render_template('index.html')


if __name__ == '__main__':
	app.run()
