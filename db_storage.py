from models.base_model import BaseModel
from models.state import State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

class DBStorage:
    """Database storage engine"""

    def __init__(self):
        """Initialize the storage engine"""
        self._engine = create_engine('sqlite:///:memory:')  # Example; use your DB config
        self._Session = sessionmaker(bind=self._engine)
        self.session = None

    def get(self, cls, id):
        """Retrieve an object by class and id"""
        if cls is None or id is None:
            return None
        return self.session.query(cls).get(id)

    def count(self, cls=None):
        """Count the number of objects in storage"""
        if cls:
            return self.session.query(cls).count()
        return self.session.query(BaseModel).count()  # Count all objects

