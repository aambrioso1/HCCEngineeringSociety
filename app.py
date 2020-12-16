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
    now = datetime.utcnow()
    midnight = datetime(now.year, now.month, now.day, 0, 0, 0)
    epoch = datetime(1970, 1, 1, 0, 0, 0)
    next_saturday = now + timedelta(5 - now.weekday())
    return render_template('calendar.html', now=now, midnight=midnight,
                           epoch=epoch, next_saturday=next_saturday)
	# Only this line appears in original code for the /calendar route
	# return render_template('calendar.html')

@app.route('/ajax')
def ajax():
    return jsonify({'timestamp': moment.create(datetime.utcnow()).format(
        'LLLL')})


@app.route('/gallery')
def gallery():
	return render_template('photo_gallery.html')

@app.route('/galaxy_stuff')
def galaxy_stuff():
	return render_template('/galaxy_stuff/galaxy_index.html')

@app.route('/user/<name>')
def user(name):
	    return render_template('user.html', name=name)

@app.route('/discord')
def discordInfoPage():
	return render_template('DiscordInfoPage.html')

if __name__ == "__main__":
    app.run(debug=True, port=5000)
