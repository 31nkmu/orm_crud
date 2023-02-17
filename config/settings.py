import sqlalchemy as db
import sqlalchemy.orm as orm
from decouple import config

engine = db.create_engine(config('DB_URL'), echo=False)


class Base(orm.DeclarativeBase):
    pass
