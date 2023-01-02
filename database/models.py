from sqlalchemy import (Boolean, Column, DateTime, ForeignKey, Integer, String, Text)
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.sql import func, expression

Base = declarative_base()


class PrimaryKey:
    id = Column(Integer, primary_key=True, index=True, unique=True)


class Name(PrimaryKey):
    name = Column(String(30))


class User(Base, Name):
    __tablename__ = 'user'

    email         = Column(String(255), nullable=False, unique=True)
    nickname      = Column(String(100), nullable=False, unique=True)
    password      = Column(String(255), nullable=False)
    created_at    = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    is_deleted    = Column(Boolean(), server_default=expression.false())
    categories    = relationship('Category', back_populates='user')
    user_articles = relationship('UserArticle', back_populates='user')


class Category(Base, Name):
    __tablename__ = 'category'

    description = Column(String(100))
    user_id     = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'))
    user        = relationship('User', back_populates='categories')
    is_public   = Column(Boolean, server_default=expression.false())
    articles    = relationship('Article', back_populates='category')


class UserArticle(Base, PrimaryKey):
    __tablename__ = 'user_article'

    user_id    = Column(Integer, ForeignKey('user.id', ondelete='CASCADE'))
    user       = relationship('User', back_populates='user_articles')
    article_id = Column(Integer, ForeignKey('article.id', ondelete='CASCADE'))
    article    = relationship('Article', back_populates='user_articles')


class Article(Base, PrimaryKey):
    __tablename__ = 'article'

    title       = Column(String(255))
    url         = Column(String(255), nullable=False)
    category_id = Column(Integer, ForeignKey('category.id', ondelete='CASCADE'))
    category    = relationship('Category', back_populates='articles')
    is_read     = Column(bool, server_default=expression.false())
