from db import db

class StoreModel(db.Model):
    __tablename__ = "playlist"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False) 
    song = db.relationship("SongModel", back_populates="playlist", lazy="dynamic", cascade="all, delete")
    

    