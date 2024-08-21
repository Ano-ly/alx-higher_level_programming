#!/usr/bin/python3
"""Get all states and corresponding city objects"""

if __name__ == '__main__':
    from relationship_state import Base, State
    from relationship_city import City
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    args = sys.argv
    user = args[1]
    pswd = args[2]
    db = args[3]

    my_engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                              format(user,
                                     pswd,
                                     'localhost:3306',
                                     db))
    Base.metadata.create_all(bind=my_engine)
    Session = sessionmaker(my_engine)
    new_session = Session()

    objs = new_session.query(State).order_by(State.id)
    for my_row in objs.all():
        print("{}: {}".format(my_row.id, my_row.name))
        for city in my_row.cities:
            print("\t{}: {}".format(city.id, city.name))

    new_session.close()
