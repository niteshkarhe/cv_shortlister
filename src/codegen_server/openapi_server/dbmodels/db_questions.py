from openapi_server.app_context import db

class Db_Questions(db.Model):
    __tablename__ = "questions"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role = db.Column(db.String(50), nullable=False)
    hr_email = db.Column(db.String(50), nullable=False)
    question = db.Column(db.String(50), nullable=False)
    expected_answer = db.Column(db.String(50), nullable=False)

    def add(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return "questions"

    @staticmethod
    def get_all():
        questions = Db_Questions.query.all()
        return questions

    @staticmethod
    def get_role_questions(role):
        questions = Db_Questions.query.filter_by(role=role).all()
        if len(questions) > 0:
            return questions
        else:
            return None