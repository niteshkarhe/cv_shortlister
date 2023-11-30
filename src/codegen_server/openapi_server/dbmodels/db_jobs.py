from openapi_server.app_context import db

from sqlalchemy import text

class Db_Jobs(db.Model):
    __tablename__ = "jobs"

    id = db.Column(db.Integer, primary_key=True, nullable=False)
    role = db.Column(db.String(50), nullable=False)
    hr_email = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return "jobs"

    def add(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.execute(text(
            'delete from jobs'
        ))
        db.session.commit()

    @staticmethod
    def get_jobs():
        jobs = Db_Jobs.query.all()
        if len(jobs) > 0:
            return jobs
        else:
            return None

    @staticmethod
    def get_jobid_deails(job_id):
        job = Db_Jobs.query.filter_by(id=job_id)
        if job.count() > 0:
            return job[0]
        else:
            return None