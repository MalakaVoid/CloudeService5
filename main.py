from config import Config
from app import app, db
from prometheus_flask_exporter import PrometheusMetrics


with app.app_context():
    db.create_all()


if __name__ == '__main__':
    metrics = PrometheusMetrics(app)
    app.run(host=Config.FLASK_APP_HOST,
            debug=Config.FLASK_DEBUG)
