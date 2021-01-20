from flask import Flask, render_template, jsonify
from flask_bootstrap import Bootstrap
from datetime import datetime, timedelta
from flask_moment import Moment

app = Flask(__name__)
moment = Moment(app)
bootstrap = Bootstrap(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calendar')
def calendar():
	return render_template('calendar.html')


@app.route('/gallery')
def gallery():
	return render_template('photo_gallery.html')

@app.route('/galaxy_stuff')
def galaxy_stuff():
	return render_template('/galaxy_stuff/galaxy_index.html')

@app.route('/admin/<name>')
def user(name):
	    return render_template('user.html', name=name)

@app.route('/discord')
def discordInfoPage():
	return render_template('DiscordInfoPage.html')

if __name__ == "__main__":
    app.run(debug=True, port=5000)
