from sqlalchemy.orm import declarative_base
from sqlalchemy import *

base = declarative_base()

class Membro(base):
    __tablename__ = 'Membros'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    start_date = Column(Date)
    course = Column(String)
    actual_area = Column(String)
    more_than1_area = Column(Boolean)
    actual_charge = Column(String)
    more_than1_charge = Column(Boolean)
    menager = Column(Boolean)

class area_hist(base):
    __tablename__ = 'area_hist'
    id = Column(Integer, primary_key=True)
    id_membro = Column(Integer, ForeignKey('Membros.id'))
    area = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    
class charge_hist(base):
    __tablename__ = 'charge_hist'
    id = Column(Integer, primary_key=True)
    id_membro = Column(Integer, ForeignKey('Membros.id'))
    charge = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)