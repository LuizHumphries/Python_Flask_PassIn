from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class __DbConnectionHandler:
    def __init__(self) -> None:
        self.__conection_string = "{}:///{}".format(
            "sqlite",
            "storage.db"
        )
        self.__engine = None
        self.session = None
    
    def __enter__(self):
        session_maker = sessionmaker()
        self.session = session_maker(bind=self.__engine)
        return self

    def __exit__(self, exec_type, exc_val, exc_tb):
        self.session.close() 
    
    def connect_to_db(self) -> None:
        self.__engine = create_engine(self.__conection_string)
    
    def get_engine(self):
        return self.__engine
    
db_connection_handler = __DbConnectionHandler()
    
