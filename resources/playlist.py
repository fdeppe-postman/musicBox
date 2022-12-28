from flask.views import MethodView
from flask_smorest  import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models import PlaylistModel
from schemas import PlaylistSchema, PlaylistUpdateSchema



blp = Blueprint("Playlists", "playlists", description="Operations on playlists")

@blp.route("/playlist/<int:playlist_id>")
class Playlist(MethodView):
    @blp.response(200, PlaylistSchema)


##------- get playlist   
    def get(self, playlist_id):
        playlist = PlaylistModel.query.get_or_404(playlist_id)
        return playlist
        
##------- del playlist   
    def delete(self, playlist_id):
        playlist = PlaylistModel.query.get_or_404(playlist_id)
        db.session.delete(playlist)
        db.session.commit()
        return {"message": "playlist has been deleted"} 


@blp.route("/playlist")
class PlaylistList(MethodView):

# ------ get all playlists 
    @blp.response(200, PlaylistSchema(many=True))
    def get(self):
        return PlaylistModel.query.all()


#------- post playlist 
    @blp.arguments(PlaylistSchema)
    @blp.response(201, PlaylistSchema) 
    def post(self, playlist_data): 
        playlist = PlaylistModel(**playlist_data)
        try:
            db.session.add(playlist)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A playlist with that name already exists"
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred creating the playlist")
        
        return playlist


# ------ update playlist --------   

    @blp.arguments(PlaylistUpdateSchema)
    @blp.response(200, PlaylistSchema)
    def put(self, playlist_data, playlist_id):
        playlist = PlaylistModel.query.get(playlist_id)
        
        if playlist:            
            playlist.name = playlist_data["name"]
        else:
            playlist = PlaylistModel(id=playlist_id, **playlist_data)

        db.session.add(playlist)
        db.session.commit()

        return playlist


