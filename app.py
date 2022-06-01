from datetime import datetime
from flask import Flask, render_template, request, session,\
    redirect, g
from flask_babel import Babel, gettext


app = Flask(__name__, 
    template_folder="asset", 
    static_folder="asset/static")
app.config['BABEL_DEFAULT_LOCALE'] = 'es'
# app.config.from_pyfile('babel.cfg')

babel = Babel(app)
babel.init_app(app=app)


LANGUAGE_SUPPORT = ['en', 'es']

@babel.localeselector
def get_locale():
    lang = request.args.get('lang', '', type=str)
    if lang in LANGUAGE_SUPPORT:
        return lang
    else:
        return 'es'
        
@babel.timezoneselector
def get_timezone():
    user = getattr(g, 'user', None)
    if user is not None:
        return user.timezone

@app.route('/', methods=['GET'])
def home():
    data = {
        "server_time": datetime.utcnow()
    }
    return render_template('index.html', result=data)


# @app.route('/lang', methods=['GET', 'POST'])
# def lang():
#     if request.method == 'POST':
#         return render_template('lang.html')
    
#     else:
#         lang = request.form['lang']
#         language = get_user_lang(lang)
#         return redirect('/')







