from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)

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

@app.route('/user/<name>')
def user(name):
	    return render_template('user.html', name=name)

@app.route('/galaxy_stuff')
def galaxy_stuff():
	# return render_tamplate('')
	return render_template('/galaxy_stuff/galaxy_index.html')


if __name__ == "__main__":
    app.run(debug=True, port=5000)