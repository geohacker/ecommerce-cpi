from sqlalchemy import Column, Integer, String, Float, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import TIMESTAMP

Base = declarative_base()

class Meta(Base):
  __tablename__ = "meta"

  round = Column(Integer,primary_key=True)
  time = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP'))

  def __init__(self, round):
    self.round = round


class Books(Base):
  __tablename__ = "books"

  id = Column(Integer,primary_key=True)
  round = Column(Integer)
  time = Column(TIMESTAMP,server_default=text('CURRENT_TIMESTAMP'))
  title = Column(String(50))
  author= Column(String(25))
  flipkart = Column(Float(6))
  infibeam = Column(Float(6))
  ebay = Column(Float(6))
  
  def __init__(self, round, title, author,flipkart=0, infibeam=0, ebay=0):
    self.round = round
    self.title = title
    self.author = author
    self.flipkart = flipkart
    self.infibeam = infibeam
    self.ebay = ebay


class Computers(Base):
  __tablename__ = "computers"

  id = Column(Integer,primary_key=True)
  round = Column(Integer)
  time = Column(TIMESTAMP,server_default=text('CURRENT_TIMESTAMP'))
  name = Column(String(25))
  manufacturer = Column(String(25))
  flipkart = Column(Float(6))
  infibeam = Column(Float(6))
  ebay = Column(Float(6))
  letsbuy = Column(Float(6))


  def __init__(self, round, name, manufacturer,flipkart=0, infibeam=0, ebay=0, letsbuy=0):
    self.round = round
    self.name = title
    self.manufacturer = manufacturer
    self.flipkart = flipkart
    self.infibeam = infibeam
    self.ebay = ebay
    self.letsbuy = letsbuy

    
class Mobiles(Base):
  __tablename__ = "mobiles"

  id = Column(Integer,primary_key=True)
  round = Column(Integer)
  time = Column(TIMESTAMP,server_default=text('CURRENT_TIMESTAMP'))
  name = Column(String(25))
  manufacturer = Column(String(25))
  flipkart = Column(Float(6))
  infibeam = Column(Float(6))
  ebay = Column(Float(6))
  letsbuy = Column(Float(6))


  def __init__(self, round, name, manufacturer,flipkart=0, infibeam=0, ebay=0, letsbuy=0):
    self.round = round
    self.name = title
    self.manufacturer = manufacturer
    self.flipkart = flipkart
    self.infibeam = infibeam
    self.ebay = ebay
