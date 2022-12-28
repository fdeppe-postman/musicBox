from db import db

class PlaylistModel(db.Model):
    __tablename__ = "playlist"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False) 

    songs = db.relationship("SongModel", back_populates="playlist", lazy="dynamic", cascade="all, delete")
#   items = db.relationship("ItemModel", back_populates="store", lazy="dynamic", cascade="all, delete")

    


    