from openapi_server.app_context import db

class Db_Jobs(db.Model):
    __tablename__ = "jobs"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    role = db.Column(db.String(50))
    hr_email = db.Column(db.String(50))

    def __repr__(self):
        return "jobs"

    def add(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def get_jobid_deails(job_id):
        job = Db_Jobs.query.filter_by(id=job_id)
        if job.count() > 0:
            return job[0]
        else:
            return None