from __future__ import annotations

from abc import ABC


class AbstractUnitOfWork(ABC):

    async def __aenter__(self) -> AbstractUnitOfWork:
        return self

    async def __aexit__(self, exc_type, exc_value, traceback):
        if exc_type:
            self.rollback()
        else:
            self.commit()

    def commit(self):
        self.session.commit()

    def flush(self):
        self.session.flush()

    def add(self,entity):
        self.session.add(entity)

    def rollback(self):
        self.session.rollback()
