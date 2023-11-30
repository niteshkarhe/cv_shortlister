from openapi_server.app_context import db
from openapi_server.models.users_model import UsersModel

from sqlalchemy import text
from datetime import datetime

class Db_Users(db.Model, UsersModel):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(50), unique=False, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(50), nullable=False)
    question = db.Column(db.String(50), nullable=False)
    answer = db.Column(db.String(50), nullable=True)
    percentage = db.Column(db.Integer, nullable=True)
    result = db.Column(db.String(50), nullable=True)
    recordingpath = db.Column(db.String(100), nullable=True)
    date = db.Column(db.DateTime(100), nullable=False)

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

    def update_userdata_for_given_id(self, id, actual_answer, videorecordingpath, percentage, result):
        db.session.execute(text(
            "update users set answer='" + actual_answer + "', recordingpath='" + videorecordingpath + "', percentage='" + percentage + "', result='" + result + "' where id=" + id
        ))
        db.session.commit()

    @staticmethod
    def get_all():
        users = Db_Users.query.all()
        if len(users) > 0:
            return users
        else:
            return None

    @staticmethod
    def get_userdata_for_given_id(id):
        users = Db_Users.query.filter_by(id=id).all()
        if len(users) > 0:
            return users[0]
        else:
            return None

    @staticmethod
    def get_id_from_addedtime(date):
        users = Db_Users.query.filter(Db_Users.date==date).all()
        if len(users) > 0:
            return users[0]
        else:
            return None
