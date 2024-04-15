#!/usr/bin/python3
"""Get all cities. Print according to id and state"""

if __name__ == '__main__':
    from model_state import Base, State
    from model_city import City
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

    objs = new_session.query(City).order_by(City.id)
    obj = new_session.query(State).order_by(State.id)
    for my_row in obj.all():
        for my_rows in objs.all():
            if my_rows.state_id == my_row.id:
                print("{}: ({}) {}".format(my_row.name,
                                           my_rows.id, my_rows.name))

    new_session.close()
