import logging
import os
import config

from flask import Flask
from flask_migrate import Migrate

from api import api
from models import db


logging.basicConfig(
    level=logging.DEBUG,
    format="[%(asctime)s]: {} %(levelname)s %(message)s".format(os.getpid()),
    datefmt="%Y-%m-%d %H:%M:%S",
    handlers=[logging.StreamHandler()],
)

logger = logging.getLogger()


def create_app():
    logger.info(f"Starting app in {config.APP_ENV} environment")
    app = Flask(__name__)
    app.config.from_object("config")
    api.init_app(app)
    # initialize sql alchemy
    db.init_app(app)
    migrate = Migrate(app, db)

    @app.route("/")
    def hello_world():
        return "Hello, test"

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", debug=True)


# old content
# from flask import Flask
# from flask_migrate import Migrate

# app = Flask(__name__)
# migrate = Migrate(app, db)


# @app.route("/", methods=["GET"])
# def hello_world():
#     return {"hello": "world"}
