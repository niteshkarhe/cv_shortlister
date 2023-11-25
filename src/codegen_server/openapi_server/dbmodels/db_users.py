from openapi_server.app_context import db
from openapi_server.models.users_model import UsersModel

from sqlalchemy import text

class Db_Users(db.Model, UsersModel):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(50))
    role = db.Column(db.String(50))
    question = db.Column(db.String(50))
    answer = db.Column(db.String(50))
    percentage = db.Column(db.Integer)
    result = db.Column(db.String(50))
    recordingpath = db.Column(db.String(100))
    date = db.Column(db.DateTime(100))

    def __repr__(self):
        return "users"

    def add(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.execute(text(
            'delete from users'
        ))
        db.session.commit()

    @staticmethod
    def get_all():
        users = Db_Users.query.all()
        return users
