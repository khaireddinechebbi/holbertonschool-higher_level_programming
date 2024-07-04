#!/usr/bin/python3
"""
Script to delete all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa using SQLAlchemy.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{database_name}',
        pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_a = session.query(State).filter(State.name.like('%a%')).all()
    for state in state_a:
        session.delete(state)
    session.commit()
    session.close()
