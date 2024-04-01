from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DbConnectionHandler:
    def __init__(self) -> None:
        self.__conection_string = "{}:///{}".format(
            "sqlite",
            "storage.db"
        )
        self.__engine = None
        self.__session = None
    
    def __enter__(self):
        session_maker = sessionmaker()
        self.__session = session_maker(bind=self.__engine)
        return self

    def __exit__(self, exec_type, exc_val, exc_tb):
        self.__session.close() 
    
    def connect_to_db(self) -> None:
        self.__engine = create_engine(self.__conection_string)
    
    def get_engine(self):
        return self.__engine
    
