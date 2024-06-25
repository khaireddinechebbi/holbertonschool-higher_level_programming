#!/usr/bin/python3
"""
Script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

    # Create an engine connected to the database
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost/{database_name}',
        pool_pre_ping=True)

    # Create all tables in the database
    Base.metadata.create_all(engine)

    # Create a sessionmaker bound to the engine
    Session = sessionmaker(bind=engine)

    # Create a session object
    session = Session()

    # Query all State objects containing the letter 'a', ordered by id
    states_with_a = session.query(State).filter(
        State.name.like('%a%')).order_by(
        State.id).all()
    for state in states_with_a:
        print(f"{state.id}: {state.name}")
    session.close()
