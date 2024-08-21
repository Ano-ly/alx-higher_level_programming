#!/usr/bin/python3
"""Get rid of an object"""

if __name__ == '__main__':
    from model_state import Base, State
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

    objs = new_session.query(State).filter(State.name.like('%a%')).all()
    for my_row in objs:
        new_session.delete(my_row)
    new_session.commit()
    new_session.close()
