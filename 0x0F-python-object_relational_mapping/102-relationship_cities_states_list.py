#!/usr/bin/python3
"""
this is module
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
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
    Base.metadata.create_all(engine)
    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    states_cities = session.query(State).join(City).order_by(City.id).all()

    for state_ in states_cities:
        for city_ in state_.cities:
            print("{}: {} -> {}".format(city_.id, city_.name, state_.name))
