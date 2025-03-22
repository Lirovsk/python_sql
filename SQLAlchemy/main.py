import time 
import os
from add_membro import *
from models import Membro, area_hist, charge_hist, base, engine
from sqlalchemy.orm import Session

base.metadata.create_all(engine)

#create a session
session = Session(engine)

#crate a new member
obj_member = add_membro.adding_process()
instance_member = obj_member.create_isntance()
session.add(instance_member)
session.commit()
