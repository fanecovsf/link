import os
from sqlalchemy import create_engine

ACCEPTABLE_DBS = [
    'sqlite',
    'postgresql'
]

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'db.txt'), mode='r') as file:
    lines = file.readlines()

    if len(lines) == 5:
        for line in lines:
            try:
                key, value = line.split('=')
                match key:
                    case 'db_kind':
                        DB_KIND = value.rstrip()
                    case 'username':
                        DB_USERNAME = value.rstrip()
                    case 'password':
                        DB_PASSWORD = value.rstrip()
                    case 'host':
                        DB_HOST = value.rstrip()
                    case 'port':
                        DB_PORT = value.rstrip()
            except:
                raise ValueError("db config error: maybe there's an error on db config file.")
    else:
        raise ValueError("db config error: maybe there's an error on db config file.")
    
if DB_KIND:
    if DB_KIND in ACCEPTABLE_DBS:
        match DB_KIND:
            case 'sqlite':
                CONN_STRING = 'sqlite:///link_database.sqlite3'
            case 'postgresql':
                CONN_STRING = f'postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/link_database'
    else:
        raise ValueError("please select an available database: [sqlite, postgresql]")
else:
    raise ValueError("please select the db kind o db config file")

try:
    ENGINE = create_engine(CONN_STRING)
except:
    raise ValueError("invalid db configurations")

