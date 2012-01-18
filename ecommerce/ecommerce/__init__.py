from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from ecommerce.models import Base, Books, Meta

engine = create_engine('mysql://root:<pwd>@localhost/ecommerce')
Base.metadata.create_all(engine)
Session = sessionmaker(engine)
#session = Session()
