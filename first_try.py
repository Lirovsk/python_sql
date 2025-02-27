from sqlalchemy.orm import declarative_base, relationship, Session
from sqlalchemy import *
from datetime import datetime

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

with Session(engine) as session:
    
    start_date = datetime.strptime('2021-01-01', '%Y-%m-%d').date()
    end_date = datetime.strptime('2021-01-02', '%Y-%m-%d').date()
    
    session.add(Membro(name='João', start_date=start_date, course='Engenharia', actual_area='TI', more_than1_area=False, actual_charge='Analista', more_than1_charge=False, menager=False))
    session.commit()

    session.add(area_hist(id_membro=1, area='TI', start_date=start_date, end_date=end_date))
    session.commit()
    
    session.add(charge_hist(id_membro=1, charge='Analista', start_date=start_date, end_date=end_date))
    session.commit()
    
    print(session.query(Membro).all())
    print(session.query(area_hist).all())
    print(session.query(charge_hist).all())
   
stmt = select(Membro).where(Membro.id == 1)

with Session(engine) as session:
    print(session.execute(stmt).scalars().all())