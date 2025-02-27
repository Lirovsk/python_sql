from sqlalchemy.orm import declarative_base, relationship, Session
from sqlalchemy import *


base = declarative_base()

class Membro(base):
    __tablename__ = 'Membros'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    start_date = Column(Date, nullable=False)
    course = Column(String)
    actual_area = Column(String, nullable=False)
    more_than1_area = Column(Boolean)
    actual_charge = Column(String)
    more_than1_charge = Column(Boolean)
    menager = Column(Boolean)
    area_hist = relationship('area_hist', back_populates='Membros', cascade='all, delete-orphan')
    charge_hist = relationship('charge_hist', back_populates='Membros', cascade='all, delete-orphan')
    
    def __repr__(self):
        return f'<Membro(Id={self.id}, name={self.name}, start_date={self.start_date}, course={self.course}, actual_area={self.actual_area}, more_than1_area={self.more_than1_area}, actual_charge={self.actual_charge}, more_than1_charge={self.more_than1_charge}, menager={self.menager})>'

class area_hist(base):
    __tablename__ = 'area_hist'
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_membro = Column(Integer, ForeignKey('Membros.id'), nullable=False)
    area = Column(String, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    Membros = relationship('Membro', back_populates='area_hist')
    
    def __repr__(self):
        return f'<area_hist(Membro(Id={self.id}, area={self.area}, start_date={self.start_date}, end_date={self.end_date})>'
    
class charge_hist(base):
    __tablename__ = 'charge_hist'
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_membro = Column(Integer, ForeignKey('Membros.id'), nullable=False)
    charge = Column(String, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)
    Membros = relationship('Membro', back_populates='charge_hist')
    
    def __repr__(self):
        return f'<charge_hist(Membro(Id={self.id}, charge={self.charge}, start_date={self.start_date}, end_date={self.end_date})>'
    
    
    #Conections
engine = create_engine('sqlite:///membros.db')
    
    #Create tables
base.metadata.create_all(engine)
    
inspector = inspect(engine)

print(inspector.get_table_names())
print(inspector.get_schema_names())

   
