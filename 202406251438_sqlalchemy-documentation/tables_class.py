from base_class import Base
from typing import (
    List,
    Optional,
)
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)
from sqlalchemy import (
    MetaData,
    String,
    create_engine,
    ForeignKey,
    Table,
)

engine = create_engine('sqlite+pysqlite:///:memory:',echo=True)
metadata_obj = MetaData()

class User(Base):
    __tablename__ = 'user_account'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]

    addresses: Mapped[List["Address"]] = relationship(back_populates="user")

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"

class Address(Base):
    __tablename__ = 'address'

    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str]
    user_id = mapped_column(ForeignKey("user_account.id"))

    user: Mapped[User] = relationship(back_populates='addresses')

    def __repre__(self) -> str:
        return f'Address(id={self.id!r}, email_address={self.email_addressr})'

Base.metadata.create_all(engine)
sandy = User(name="sandy", fullname="Sandy Cheeks")
print(sandy)
user = Table("user_account", metadata_obj, autoload_with=engine)
import ipdb; ipdb.set_trace(context=10)
