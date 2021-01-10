from sqlalchemy import Boolean, Column , ForeignKey
from sqlalchemy import DateTime, Integer, String, Text, Float
from sqlalchemy.orm import relationship
from flask_sqlalchemy import SQLAlchemy;
import config
from flask import Flask;

app = Flask(__name__);


db = SQLAlchemy(app)	



class Users(db.Model):
	"""Artículos de nuestra tienda"""
	__tablename__ = 'users'
	id = Column(Integer, primary_key=True)
	username = Column(String(100),nullable=False)
	password = Column(String(100),nullable=False)	


	def __repr__(self):
		return (u'<{self.__class__.__name__}: {self.id}>'.format(self=self))