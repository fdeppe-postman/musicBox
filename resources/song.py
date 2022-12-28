from flask.views import MethodView
from flask_smorest  import Blueprint, abort
from flask_jwt_extended import jwt_required,  get_jwt
from sqlalchemy.exc import SQLAlchemyError

from db import db
from models import SongModel
from schemas import SongSchema


 
blp = Blueprint("Songs", "songs", description="Operations on songs")

@blp.route("/song/<int:song_id>")
class Song(MethodView):
    @blp.response(200,SongSchema)
# ------ get song --------     
    #@jwt_required()
    def get(self, song_id):
        song = SongModel.query.get_or_404(song_id)
        return song        

# ------ delete song -------- 
    #@jwt_required()
    def delete(self, song_id):
        jwt = get_jwt()
        if not jwt.get("is_admin"):
            abort(401, "Must be admin")
        song = SongModel.query.get_or_404(song_id)
        db.session.delete(song)
        db.session.commit()
        return {"message": "song has been deleted"}


@blp.route("/song")
class SongList(MethodView):
# ------ get song(s) --------         
    @blp.response(200,SongSchema(many=True ))
    def get(self):
        return SongModel.query.all()

# ------ create song --------    
    #@jwt_required(fresh=True)
    @blp.arguments(SongSchema)
    @blp.response(201, SongSchema)
    def post(self, song_data):
        song = SongModel(**song_data)

        try:
            db.session.add(song)
            db.session.commit()
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the song.")

        return song
     
