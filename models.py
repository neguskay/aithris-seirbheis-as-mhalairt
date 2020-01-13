from sqlalchemy import create_engine, Table, MetaData, Column, Integer, String
from sqlalchemy.orm import scoped_session, sessionmaker, mapper
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.ext.declarative import declarative_base
import json
# from sqlalchemy import Column, Integer, String
# from app import db
#
# engine = create_engine('sqlite:///database.db', echo=True)
# db_session = scoped_session(sessionmaker(autocommit=False,
#                                          autoflush=False,
#                                          bind=engine))
# Base = declarative_base()
# Base.query = db_session.query_property()
#
# # Set your classes here.
#
# '''
# class User(Base):
#     __tablename__ = 'Users'
#
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(120), unique=True)
#     email = db.Column(db.String(120), unique=True)
#     password = db.Column(db.String(30))
#
#     def __init__(self, name=None, password=None):
#         self.name = name
#         self.password = password
# '''
#
# # Create tables.
# Base.metadata.create_all(bind=engine)


db_url_string = "postgres+psycopg2://interview:uo4uu3AeF3@candidate.suade.org/suade"
engine = create_engine(db_url_string, echo=True)
# meta_data = MetaData(engine)

Base = declarative_base(engine)
meta_data = Base.metadata
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

session = Session()


class Local_Reports(Base):
    __tablename__ = 'reports'

    id = Column(Integer, primary_key=True)
    type = Column(String)

    def __init__(self, id, data):
        self.id = id
        self.type = json.loads(type.replace("'", '"'))
        self.cleaned = self.get_cleaned_data()

    def __repr__(self):
        """"""
        return "<Report - '%s'>" % self.id

    def get_cleaned_data(self):
        if "invalid_json" not in self.type:
            data_to_return = json.loads(self.type)
        else:
            data_to_return = None
        return data_to_return

    @property
    def clean_data(self):
        clean_data = self.get_cleaned_data()
        if clean_data is not None:
            return clean_data

    @property
    def inventory(self):
        clean_data = self.get_cleaned_data()
        if clean_data is not None:
            return self.get_cleaned_data()["inventory"]

    @property
    def organization(self):
        clean_data = self.get_cleaned_data()
        if clean_data is not None:
            return clean_data["organization"]

    @property
    def created_date(self):
        clean_data = self.get_cleaned_data()
        if clean_data is not None:
            return self.get_cleaned_data()["created_at"]

    @property
    def report_date(self):
        clean_data = self.get_cleaned_data()
        if clean_data is not None:
            return clean_data["reported_at"]




# db_session = None

#
# test_table = Table('reports', meta_data, autoload=True)
#
#
#
#
#
# mapper(Local_Reports, test_table)
#
# # db_session = scoped_session(sessionmaker(autocommit=False,
# #                                      autoflush=False,
# #                                      bind=engine))
#
# Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#
# session = Session()


    # __table__ = Table('reports', meta_data,
    #                   autoload=True, autoload_with=engine)


# Base = declarative_base()
# Base.query = db_session.query_property()




# Set your classes here.
# class Reports(Base):
#     __table__ = Table('mytable', meta_data=meta_data,
#                     autoload=True)

'''
class User(Base):
    __tablename__ = 'Users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(30))

    def __init__(self, name=None, password=None):
        self.name = name
        self.password = password
'''

# Create tables.
# Base.metadata.create_all(bind=engine)
