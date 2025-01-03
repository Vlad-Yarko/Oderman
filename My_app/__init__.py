from flask import Flask
from datetime import timedelta
from dotenv import load_dotenv, find_dotenv
import os

load_dotenv(find_dotenv())

app = Flask(__name__)
app.permanent_session_lifetime = timedelta(days=7)
app.secret_key = os.getenv('SECRET_TOKEN')

from My_app.routers import registration
from My_app.routers import base
