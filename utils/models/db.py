import sqlite3
from utils.misc.log import logging


class Sqlite:

    def __init__(self) -> None:
        self.__conn = sqlite3.connect('data/db.sqlite')
        self.__cursor = self.__conn.cursor()

    async def execute(self, commands: str):
        try:
            self.__cursor.execute(commands)
            self.__conn.commit()
        except Exception as ex:
            logging.warning(ex)

    async def get(self, commands: str) -> list:
        try:
            self.__cursor.execute(commands)
            return self.__cursor.fetchall()
        except Exception as ex:
            logging.warning(ex)
