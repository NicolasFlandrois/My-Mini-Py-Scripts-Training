#!/usr/bin/python3.7
# UTF8
# Date: Tue 23 Jul 2019 15:45:15 CEST
# Author: Nicolas Flandrois

from sqlalchemy import MetaData
from sqlalchemy import Column, Integer, String, Boolean, Table #, ForeignKey
# from sqlalchemy import Float, DateTime
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from connect import engine


def createtables(name):
    """Create tables in OC Pizza DB"""
    Base = declarative_base()
    engin = engine(name)
    metadata = MetaData(bind=engin)

    todo = Table(
                 'todo', metadata,
    Column('id', Integer, primary_key=True),
    Column('text', String(200)),
    Column('complete', Boolean)
    )

    # Creat all tables
    metadata.create_all(engin)
