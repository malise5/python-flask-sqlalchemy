from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    PrimaryKeyConstraint,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

# import owner

Base = declarative_base()


class Pet(Base):
    __tablename__ = "pets"
    __table_args__ = (PrimaryKeyConstraint("id"),)  # Wrap in a tuple

    id = Column(Integer, primary_key=True)
    name = Column(String)
    species = Column(String)
    breed = Column(String)
    temperament = Column(String)
    owner_id = Column(Integer, ForeignKey("owners.id"))

    def __repr__(self):
        return f"<Pet(name={self.name}, species={self.species}, breed={self.breed}, temperament={self.temperament}, owner_id={self.owner_id})>"

    #alembic init migration 
    #alembic revision --autogenerate -m "create pets table"
    #alembic upgrade head
    #alembic downgrade -1
    #alembic revision --autogenerate -m "add created_at and updated_at columns"
    #alembic revision --autogenerate -m "add owner_id column"

    #your directory structure shoul look like the following:
    # /home/malise/Workspace/python/firstapp/
    # ├── alembic/
    # │   ├── env.py
    # │   ├── README
    # │   ├── script.py.mako``
    # │   └── versions/
    # ├── model.py
    # └── alembic.ini
    # alembic.ini -> the sqlalchemy.url to point to your database 'sqlalchemy.url = sqlite:///pets.db'
    # env.py -> find 'target_metadata' and add 'from model import Base' and above it.
    # Next, set target_metadata to 'target_metadata = Base.metadata'

    #Generate a migration by running 'alembic revision --autogenerate -m "Added Pet Model"'

        # pet_app.db should havebeen added to the directory structure

        # Take the time to review the migration and verify the datbase with SQLite Browser

        # Head to debug.py to test out CRUD actions

class Owner(Base):
    __tablename__ = "owners"
    __table_args__ = (PrimaryKeyConstraint("id"),)  # Wrap in a tuple

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    phone = Column(String)
    address = Column(String)
    pets = relationship("Pet", backref=backref("pet", lazy="dynamic"))

    def __repr__(self):
        return f"<Owner(name={self.name}, email={self.email})>"