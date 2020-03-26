from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://localhost:5432/currency', echo=True)

Base = declarative_base()

Session = sessionmaker(bind=engine)
session = Session()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    surname = Column(String(50), nullable=False)
    login = Column(String(50), nullable=False)
    password = Column(String(50), nullable=False)

    def __init__(self, name, surname, login, password):
        self.name = name
        self.surname = surname
        self.login = login
        self.password = password


class Currency(Base):
    __tablename__ = 'currency'
    id = Column(Integer, primary_key=True)
    name_currency = Column(String(50), unique=True, nullable=False)
    abbreviation = Column(String(3), unique=True, nullable=False)
    copyright_currency_abb = Column(Integer, ForeignKey('users.id'), nullable=True)

    def __init__(self, name_currency, abbreviation, copyright_currency_abb = None):
        self.name_currency = name_currency
        self.abbreviation = abbreviation
        self.copyright_currency_abb = copyright_currency_abb


class History(Base):
    __tablename__ = 'histor_of_users'
    operation_id = Column(Integer, primary_key=True)
    what_abb = Column(String(3), nullable=False)
    how_much = Column(Integer, nullable=False)
    to_abb = Column(String(3), nullable=False)
    total = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

    def __init__(self, what_abb, how_much, to_abb, total, user_id):
        self.what_abb = what_abb
        self.how_much = how_much
        self.to_abb = to_abb
        self.total = total
        self.user_id = user_id

