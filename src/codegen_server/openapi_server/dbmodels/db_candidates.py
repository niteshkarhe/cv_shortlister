from openapi_server.app_context import db
from openapi_server.dbmodels.db_jobs import Db_Jobs

class Db_Candidates(db.Model):
    __tablename__ = "candidates"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    jobid = db.Column(db.Integer, nullable=False)
    resume_matched_percentage = db.Column(db.String(50), nullable=False)
    is_shorlisted = db.Column(db.String(50), nullable=True)

    def __repr__(self):
        return "candidates"

    def add(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_candidates():
        candidates = Db_Candidates.query.all()
        if len(candidates) > 0:
            return candidates
        else:
            return None

    @staticmethod
    def get_candidate_by_logincode(login_code):
        candidates = Db_Candidates.query.filter_by(id=login_code)
        if candidates.count() > 0:
            return candidates[0]
        else:
            return None