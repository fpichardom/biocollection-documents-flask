from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db
# Adds required methods that are needed for flask_login to work so these don't need to be implemented manually
from flask_login import UserMixin
from app import login

@login.user_loader
def load_user(id):
    # The user id is transformed to integer because default is string. If the id is naturally a string then this line is not needed
    return db.session.get(User, int(id))
    #return db.session.get(User,id)



# Uses SQLAlchemy 2.0 style

class User(UserMixin, db.Model):
    # Override the table name to be used by SQLAlchemy. Default use the class name in snake case
    __tablename__ = 'user'
    
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(120))
    email: so.Mapped[Optional[str]] = so.mapped_column(sa.String(120))
    role: so.Mapped[str] = so.mapped_column(sa.String(64), default='user')    
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

    def __repr__(self):
        return '<User {}>'.format(self.username)