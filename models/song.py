from db import db


class SongModel(db.Model):
    __tablename__ = "songs"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    description = db.Column(db.String)

    playlist_id = db.Column(db.Integer, db.ForeignKey("playlist.id"), unique=False, nullable=False)
    playlist = db.relationship("PlaylistModel", back_populates="songs")

    # store_id = db.Column(db.Integer, db.ForeignKey("stores.id"), unique=False, nullable=False)
    # store = db.relationship("StoreModel", back_populates="items")

