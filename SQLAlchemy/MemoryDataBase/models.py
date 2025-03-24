from sqlalchemy import String
from sqlalchemy import Integer
from sqlalchemy import create_engine
from sqlalchemy import ForeignKey
from sqlalchemy import insert
# In case of need:
from sqlalchemy import text
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Session
from typing import List
from typing import Optional

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
    
    address: Mapped[List["Address"]] = relationship(back_populates="User")
    
    
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
stmt = insert(User).values(name="Lira", fullname="João Vítor Lira")
stmt2 = insert(User).values(name="Isa", fullname="Isadora")
compiled = stmt.compile()
compiled2 = stmt2.compile()
compiled.params
compiled2.params
input("Enter para prosseguir")
with engine.connect() as conn:
    conn.execute(stmt)
    conn.execute(stmt2)
    conn.commit()
    
