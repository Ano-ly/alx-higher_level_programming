#!/usr/bin/python3
"""Add state to database"""

if __name__ == '__main__':
    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from relationship_state import Base, State
    from relationship_city import City

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

    new_state = State(name="California")
    new_city = City(name="San Francisco", state_id=new_state.id)
    new_state.cities.append(new_city)

    new_session.add(new_state)
    new_session.commit()
    new_session.close()
