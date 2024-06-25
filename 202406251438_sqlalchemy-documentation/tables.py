from sqlalchemy import (
    MetaData,
    Table,
    Column,
    Integer,
    String,
    ForeignKey,
    create_engine,
    text,
)

engine = create_engine('sqlite+pysqlite:///:memory:',echo=True)

metadata_obj = MetaData()

user_table = Table(
    'user_account',
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('name', String(30)),
    Column('fullname', String),
)

address_table = Table(
    'address',
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('user_id', ForeignKey('user_account.id'), nullable=False),
    Column('email_address', String, nullable=False),
)

metadata_obj.create_all(engine)
with engine.connect() as conn:
    print('SELECT user_account table')
    result = conn.execute(text("SELECT * FROM user_account"))
    print(result.all())

    print('SELECT address table')
    result = conn.execute(text("SELECT * FROM address"))
    print(result.all())
