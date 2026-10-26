from sqlalchemy import Column, Integer, String, UniqueConstraint
from database import Base

class Book(Base):

    __tablename__ = "books"
    __table_args__ = (
        UniqueConstraint("title", "author", "year", name="unique_book_details"),
    )

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    year = Column(Integer,  nullable=False)

# Pydantic BookCreate outlines the lexcial and numeric constraints for values in the 
# books database, such as year being Greater Than or Equal to 1900
  
# SQL alchemy Book model in models defines the database table including column/attirbute names, datatyprs, 
#  with further constrains for the overall table to preserve book object uniqueness