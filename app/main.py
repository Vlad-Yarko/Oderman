from flask import Flask, session, render_template
from asgiref.wsgi import WsgiToAsgi
from datetime import timedelta
from app.src.accounts.account import account
from app.src.restaurant.restaurant import restaurant
import uvicorn

from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())


app = Flask(__name__)
app.permanent_session_lifetime = timedelta(days=7)
app.secret_key = os.getenv('SECRET_TOKEN')
app.register_blueprint(account, url_prefix='/account')
app.register_blueprint(restaurant, url_prefix='/restaurant')
# login_manager = LoginManager(app)
# login_manager.login_view = 'accounts.login_site'


# @login_manager.user_loader
# async def load_user(user_id):
#     return await UserLogin().get_user(int(user_id))
#
#
# # @app.before_request
# # async def before():
# #     ur = await current_user


@app.route('/')
async def home():
    username = session.get('usr', "")
    return render_template('index.html', user=username)

a = WsgiToAsgi(app)


if __name__ == '__main__':
    uvicorn.run('main:a', port=8080)
