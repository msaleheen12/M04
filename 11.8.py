#16.8
from sqlalchemy import create_engine, MetaData, Table, Column, String, Integer, select

db_url = 'sqlite:///books.db'

engine = create_engine(db_url)

metadata = MetaData(bind=engine)
metadata.reflect()

books_table = Table('books', metadata, autoload=True, autoload_with=engine)


select_query = select([books_table.columns.title]).order_by(books_table.columns.title.asc())

with engine.connect() as conn:
    result = conn.execute(select_query)
    rows = result.fetchall()


print("Titles in alphabetical order:")
for row in rows:
    print(row[0])  



