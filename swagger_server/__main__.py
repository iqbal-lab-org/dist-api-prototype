#!/usr/bin/env python3
import os
from random import randrange

import connexion
from flask import g
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from swagger_server import encoder
from swagger_server.orm.DistanceORM import DistanceORM


def connect_db():
    engine = create_engine('mysql://{user}:{passwd}@localhost/{db}'.format(
        user=os.environ.get('MYSQL_USER'),
        passwd=os.environ.get('MYSQL_PASSWORD'),
        db=os.environ.get('MYSQL_DATABASE')
    ), convert_unicode=True)
    return scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine)), engine


def init_db():
    db_session, engine = connect_db()
    DistanceORM.query = db_session.query_property()
    DistanceORM.metadata.create_all(bind=engine)

    with open('swagger_server/test/data/sample.list') as f:
        test_data = f.read().splitlines()
        distances = []
        for line in test_data:
            s1 = line.rstrip()
            for s2 in test_data:
                s2 = s2.rstrip()
                if s2 != s1:
                    d = randrange(9)
                    distances.append(DistanceORM(s1=s1, s2=s2, d=d))
        db_session.bulk_save_objects(distances)
        db_session.commit()


def get_db():
    if 'db' not in g:
        g.db, _ = connect_db()

    return g.db


def main():
    init_db()

    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'Distance API'}, pythonic_params=True)
    app.run(port=8080, debug=os.environ.get('DEBUG'))


if __name__ == '__main__':
    main()
