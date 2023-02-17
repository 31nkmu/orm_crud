from typing import List, Optional

import sqlalchemy as db
import sqlalchemy.orm as orm

from config.settings import Base


class Category(Base):
    __tablename__ = 'category'

    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    title: orm.Mapped[str] = orm.mapped_column(db.String(30))

    products: orm.Mapped[List['Product']] = orm.relationship(back_populates='category', cascade='all, delete-orphan')

    def __repr__(self):
        return self.title


class Product(Base):
    __tablename__ = 'product'

    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    title: orm.Mapped[str] = orm.mapped_column(db.String(60))
    price: orm.Mapped[float] = orm.mapped_column(db.Numeric(asdecimal=True))

    category_id: orm.Mapped[int] = orm.mapped_column(db.ForeignKey('category.id'))
    category: orm.Mapped['Category'] = orm.relationship(back_populates='products')

    user_id: orm.Mapped[int] = orm.mapped_column(db.ForeignKey('user_account.id'))
    user: orm.Mapped['User'] = orm.relationship(back_populates='products')

    def __repr__(self):
        return self.title


class User(Base):
    __tablename__ = 'user_account'

    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    email: orm.Mapped[str] = orm.mapped_column(db.String(60))
    username: orm.Mapped[Optional[str]]
    password: orm.Mapped[str] = orm.mapped_column(db.String(50))

    products: orm.Mapped[Optional['Product']] = orm.relationship(back_populates='user',
                                                                 cascade='all, delete-orphan')

    def __repr__(self):
        return self.email
