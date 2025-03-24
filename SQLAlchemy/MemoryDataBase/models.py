from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy import insert
from sqlalchemy import select
# In case of need:
from sqlalchemy import text
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from typing import List
from typing import Optional

from time import sleep

# Definindo a engine do banco de dados / Defining the engine of the database
engine = create_engine("sqlite:///:memory:", echo=True)


# Definindo a base para as tabelas / Defining the Base for the tables
class Base(DeclarativeBase):
    pass

# Definindo as tabelas do banco de dados / Defining the tables from the database
class User(Base):
    __tablename__ = "user_account"
    
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]
    
    addresses: Mapped[List["Address"]] = relationship(back_populates="user")
    
    
    def __repr__(self) -> str:
        return f"User<id:{self.id!r}, Name:{self.name!r}, FullName:{self.fullname!r}>"
    
class Address(Base):
    __tablename__ = "address"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str]
    user_id = mapped_column(ForeignKey("user_account.id"))

    user: Mapped[User] = relationship(back_populates="addresses")
    
    
    def __repr__(self):
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"

# Criando as tabelas / Creating the tables
Base.metadata.create_all(engine)
lira = User(name="Lira", fullname="João Vítor Lira")
Isa = User(name="Isa", fullname="Isadora")
Paula = User(name="Paula", fullname="Paula arantes")
print(lira, Isa, Paula)
input("Enter para prosseguir")
with Session(engine) as conn:
    conn.add(lira)
    conn.add(Isa)
    conn.add(Paula)
    # The above objects are not in the database yet
    conn.flush()
    # The flushing process allow it to decide the bes method to commit hte changes into the database
    conn.commit()
    print(f"The objects' id is: {lira.id}, {Isa.id}, {Paula.id}") # The objects need to be inside a session.
    conn.close()
    
"""input("Pressione enter para pesquisar informações no banco de dados")
print(select(User))
stmt = select(User).where(User.name =="Isa")
with Session(engine) as conn:
    result = conn.execute(stmt)"""
with Session(engine) as conn:
    result = conn.execute(select(User)).all()
for row in result:
    print(row)        

with Session(engine) as conn:
    result = conn.execute(select(User.name)).all()
for row in result:
    print(row)
