from .db import db
from sqlalchemy.sql import func

class Player(db.Model):
    __tablename__ = 'players'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    wins = db.Column(db.Integer)
    losses = db.Column(db.Integer)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False, server_default=func.now())
    updated_at = db.Column(db.DateTime(timezone=True), onupdate=func.now(), default=func.now())

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'wins': self.wins,
            'losses': self.losses,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
