from sqlalchemy import create_engine
from sqlalchemy import text

engine = create_engine('sqlite+pysqlite:///:memory:',echo=True)

with engine.connect() as conn:
    result = conn.execute(text("select 'hello world'"))
    print(result.all())

with engine.connect() as conn:
    conn.execute(text("CREATE TABLE some_table (x int, y int)"))
    conn.execute(text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
                 [{"x": 1, "y": 1}, {"x": 2, "y": 4}],
                 )
    conn.commit()
    result = conn.execute(text("SELECT * FROM some_table"))
    print(result.all())

with engine.begin() as conn:
    conn.execute(text("INSERT INTO some_table (x, y) VALUES (:x, :y)"),
                 [{"x": 6, "y": 8}, {"x": 9, "y": 10}],
                 )

with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM some_table"))
    for row in result:
        print(f'x: {row.x} y: {row.y}')
    print('Another way')
    # Why restult desapear after the first usage?
    result = conn.execute(text("SELECT * FROM some_table"))
    for x, y in result:
        print(f'x: {x} y: {y}')
    print('Using indexes')
    result = conn.execute(text("SELECT * FROM some_table"))
    for row in result:
        print(f'x: {row[0]} y: {row[1]}')
    print('Using mapping access')
    result = conn.execute(text("SELECT * FROM some_table"))
    for dict_row in result.mappings():
        print(f'x: {dict_row["x"]} y: {dict_row["y"]}')
    print('Using WHERE clause')
    result = conn.execute(text("SELECT * FROM some_table WHERE y > :y"), {"y": 4})
    for x, y in result:
        print(f'x: {x} y: {y}')

from sqlalchemy.orm import Session
# import ipdb;ipdb.set_trace(context=10)

print('Using session object')
stmt = text("SELECT x, y FROM some_table WHERE y > :y ORDER BY x, y")
with Session(engine) as session:
    result = session.execute(stmt, {"y": 6})
    for x, y in result:
        print(f'x: {x} y: {y}')

with Session(engine) as session:
    result = session.execute(
        text("UPDATE some_table SET y=:y WHERE x=:x"),
        [{"x": 6, "y": 11}, {"x": 9, "y": 15}],
    )
    session.commit()
    result = session.execute(text("SELECT * FROM some_table"))
    print('Seeing the insertion with session object')
    for row in result:
        print(f'x: {row.x} y: {row.y}')
