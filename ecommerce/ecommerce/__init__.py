from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from ecommerce.models import Base, Books, Meta

engine = create_engine('<mysql connection>')
Base.metadata.create_all(engine)
session = Session(engine)
#session = Session()
