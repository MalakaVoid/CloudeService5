from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate
from flask_caching import Cache
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)
app.config.from_object(Config)
metrics = PrometheusMetrics(app)

cache = Cache(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models, constants
