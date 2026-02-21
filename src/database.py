import sqlite3
import threading
import typing as tp
from enum import Enum
from datetime import datetime


class Database:
    access = threading.Lock()

    @classmethod
    def query(cls, sql: str) -> list[tp.Any]:
        _ = cls.access.acquire()
        try:
            with sqlite3.connect("performance.db") as db:
                cur = db.execute(sql)
                db.commit()
                return cur.fetchall()
        except Exception as _:
            raise
        finally:
            cls.access.release()


class ProgrammerState(Enum):
    AWAIT = "A"
    WORK = "W"

class WorkingCounter:
    state = ProgrammerState.AWAIT
    started_at = datetime.now()

    @classmethod
    def _reset(cls):
        cls.started_at = datetime.now()
        cls.state = ProgrammerState.AWAIT

    @classmethod
    def start(cls):
        cls.state = ProgrammerState.WORK
        cls.started_at = datetime.now()

    @classmethod
    def end(cls) -> int:
        minutes = int((datetime.now() - cls.started_at).total_seconds() // 60)
        cls._reset()
        return minutes
