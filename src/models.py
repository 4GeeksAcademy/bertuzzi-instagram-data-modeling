import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer,primary_key=True)
    username = Column(String(50),nullable=False,unique=True)
    password = Column(String(50),nullable=False)

class Follower(Base):
    __tablename__ = 'followers'
    id = Column(Integer,primary_key=True)
    following_id = Column(Integer,ForeignKey('users.user_id'))
    follower_id = Column(Integer,ForeignKey('users.user_id'))
    users = relationship(User)

class Post(Base):
    __tablename__ = 'posts'
    post_id = Column(Integer,primary_key=True)
    user_id = Column(Integer,ForeignKey('users.user_id'))
    posting_date = Column(DateTime,nullable=False)
    likes = Column(Integer,nullable=False)
    comments = Column(Integer,nullable=False)
    users = relationship(User)

class Like(Base):
    __tablename__ = 'likes'
    like_id = Column(Integer,primary_key=True)
    user_id = Column(Integer,ForeignKey('users.user_id'))
    post_id = Column(Integer,ForeignKey('posts.post_id'))
    users = relationship(User,foreign_keys=[user_id])
    posts = relationship(Follower,foreign_keys=[post_id])

class Comment(Base):
    __tablename__ = 'comments'
    comment_id = Column(Integer,primary_key=True)
    user_id = Column(Integer,ForeignKey('users.user_id'))
    post_id = Column(Integer,ForeignKey('posts.post_id'))
    users = relationship(User,foreign_keys=[user_id])
    posts = relationship(Follower,foreign_keys=[post_id])

class Message(Base):
    __tablename__ = 'messages'
    message_id = Column(Integer,primary_key=True)
    user_id = Column(Integer,ForeignKey('users.user_id'))
    follower_id = Column(Integer,ForeignKey('followers.id'))
    users = relationship(User,foreign_keys=[user_id])
    followers = relationship(Follower,foreign_keys=[follower_id])



## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
