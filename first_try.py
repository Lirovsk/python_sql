from sqlalchemy.orm import declarative_base
from sqlalchemy import *

base = declarative_base()

class Membro(base):
    __tablename__ = 'Membros'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    start_date = Column(Date, nullable=False)
    course = Column(String)
    actual_area = Column(String, nullable=False)
    more_than1_area = Column(Boolean)
    actual_charge = Column(String)
    more_than1_charge = Column(Boolean)
    menager = Column(Boolean)

class area_hist(base):
    __tablename__ = 'area_hist'
    id = Column(Integer, primary_key=True)
    id_membro = Column(Integer, ForeignKey('Membros.id'), nullable=False)
    area = Column(String, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    
class charge_hist(base):
    __tablename__ = 'charge_hist'
    id = Column(Integer, primary_key=True)
    id_membro = Column(Integer, ForeignKey('Membros.id'), nullable=False)
    charge = Column(String, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)