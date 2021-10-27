import uuid

from flask_sqlalcehmy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.String(), priary_key=True, default=lambda: str(uuid.uuid4()))
    username = db.Column(db.String())
    email = db.Column(db.String(), unique=True)
