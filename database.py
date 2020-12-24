from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import models

class GBDataBase:
    def __init__(self, db_url: str):
        engine = create_engine(db_url)
        models.Base.metadata.create_all(bind=engine)
        self.session_m = sessionmaker(bind=engine)

    def create_post(self, data):
        print(1)


