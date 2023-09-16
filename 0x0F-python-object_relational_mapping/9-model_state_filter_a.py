#!/usr/bin/python3
"""
this is module
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    the main
    """
    url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])
    # Create the database engine using the url
    engine = create_engine(url)
    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()
    filter_ = session.query(State).filter(State.name.contains('a'))
    states = filter_.order_by(State.id)

    for state_ in states:
        print('{0}: {1}'.format(state_.id, state_.name))
