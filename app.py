from flask import Flask, render_template, jsonify, request, redirect, url_for
from flask_bootstrap import Bootstrap
from datetime import datetime, timedelta
from flask_moment import Moment
import os


app = Flask(__name__)
moment = Moment(app)
bootstrap = Bootstrap(app)

# This configuration will make the app less hackable.
app.config["ADMIN_PASSWORD"] = os.environ.get("ADMIN_PASSWORD")

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

# This code for the /gallery route was Dre's work.
# Need to make two routes:  (1) One for the pictures and (2) One secret or locked route for uploads.
# The /gallery route can remains as it was and a new route /admin/password can be create for the uploading.
"""
app.config["IMAGE_UPLOADS"] = "/static/img"

@app.route('/gallery', methods = ['GET','POST'])
def gallery():
     if request.method == "POST":

        if request.files:
            image = request.files["image"]
            image.save(os.path.join(app.config["IMAGE_UPLOADS"], image.filename))
            print(image)
            print("img is save")
            return redirect(request.url)
     return render_template('photo_gallery.html')

"""
@app.route('/gallery')
def gallery():
	return render_template('photo_gallery.html')

@app.route('/galaxy_stuff')
def galaxy_stuff():
	return render_template('/galaxy_stuff/galaxy_index.html')

"""
@app.route('/admin/<name>')
def user(name):
	    return render_template('user.html', name=name)
"""

@app.route('/discord')
def discordInfoPage():
	return render_template('DiscordInfoPage.html')

@app.route('/admin/upload')
def upload():
    return render_template('upload.html')

# This allows files to be upload to the server.
# Need to secure this 
@app.route('/admin/upload', methods=['POST'])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(uploaded_file.filename)
    return redirect(url_for('upload'))

if __name__ == "__main__":
    app.run(debug=True, port=5000)
