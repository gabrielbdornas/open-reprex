# kit de ferramentas p trabalhar com db sql
# automações
# alembic lib de migrações
# orm: object relational mapper

# Core: Núcleo
# Engine (connection,dialect, pool): Fábrica de conexões
from sqlalchemy import create_engine

engine = create_engine( # factory
    'sqlite://',
    echo=True, # Mostra logs
)

print(engine)
print(engine.dialect)
# google sheets!!!
conn = engine.connect() # sem gerenciador de context (with)
print(conn.connection.dbapi_connection)
conn.close() # sem gerenciador de context (with)

# poll - reservatório de conexões
# commit - transação que deu certo
# rollback - transação deu errado (select sempre terá ROLLBACK)
# ACID - atomicidade (tudo ou nada da transação)

from sqlalchemy import create_engine, text

engine = create_engine('sqlite://', echo=True)

with engine.connect() as conn:
    sql = text("select 'hello world'")
    result = conn.execute(sql)
    print(result.all())

# python -i main.py (lembrar do -i)
# pq o result some após o primeiro uso

with engine.connect() as conn:
    with conn.begin(): # já commita e mesma conexão para a mesma conexões
        sql = text("select 'olá mundo'")
        result = conn.execute(sql)
        print(result.all())

# Result
# .fetchone()
# .fetchmany(3)
# .fetchall()
# .first()
# olhar documentação
