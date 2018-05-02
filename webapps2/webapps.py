"""
- render_template is jinja2 powered flask template rendering.
- user can define customized error page by using @app.errorhandler placeholder
- url_for is used to print or get url in template dynamically. e.g {{ url_for('user',name='john',_external=True) }}

"""
from datetime import datetime
from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask import url_for

# First step define Flask App.
app = Flask(__name__)

# Bootstrap provided by twitter.
bootstrap = Bootstrap(app)

# Moment is used for manipulating date time.
moment = Moment(app)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', current_time = datetime.utcnow())


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    app.run(port=8001)