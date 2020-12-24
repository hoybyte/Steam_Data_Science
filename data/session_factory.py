import sqlalchemy
import sqlalchemy.orm
import database.db_folder as db_folder

__factory = None


def global_init():
    global __factory

    full_file = db_folder.get_db_path('steam_data.sqlite')
    connection_string = 'sqlite:///' + full_file

    engine = sqlalchemy.create_engine(connection_string, echo=False)
    # TODO Create metadata for tables in Database

    __factory = sqlalchemy.orm.sessionmaker(bind=engine)


def create_sesion():
    global __factory

    if __factory is None:
        global_init()
    return __factory()
