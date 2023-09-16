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
    
    join_res = session.query(City, State).join(State)

    for city_, state_ in join_res.all():
        print("{}: ({}) {}".format(state_.name, city_.id, city_.name))
