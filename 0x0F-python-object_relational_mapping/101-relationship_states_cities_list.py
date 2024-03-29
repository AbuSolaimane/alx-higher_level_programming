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

    outer_join = session.query(State).outerjoin(City)
    results = outer_join.order_by(State.id, City.id).all()

    for state_ in results:
        print("{}: {}".format(state_.id, state_.name))
        for city_ in state_.cities:
            print("    {}: {}".format(city_.id, city_.name))
