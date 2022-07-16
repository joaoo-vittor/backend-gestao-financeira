from __future__ import annotations
from typing import Type
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm.session import Session
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler:
    """Sqlalchemy database connection"""

    def __init__(self, connection_string: str) -> None:
        self.__connection_string = connection_string
        self.session: Type[Session] = None
        self.engine: Type[Engine] = None

    def get_engine(self) -> Type[Engine]:
        """Get Engine"""
        if self.engine is None:
            self.engine = create_engine(self.__connection_string, pool_size=10)

        return self.engine

    def get_session(self) -> Type[Session]:
        """Get Session"""
        if self.engine is None:
            self.get_engine()

        session_maker = sessionmaker()
        self.session = session_maker(bind=self.engine)

        return self.session
