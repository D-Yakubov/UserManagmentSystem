from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String, unique=True, index=True)
    email = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))


class Admin(Base):
    __tablename__ = "admins"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, unique=True, index=True)
    role = Column(String)


class LoginLogout(Base):
    __tablename__ = "login_logout"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, ForeignKey('users.username'), nullable=False)
    login_time = Column(DateTime, nullable=False)
    logout_time = Column(DateTime)

    # Define relationship with User table
    # user = relationship("User", backref="login_logout_entries", foreign_keys=[user_id, username])
