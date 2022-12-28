from marshmallow import Schema, fields

class PlainSongSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)    
    
class PlainPlaylistSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str()

class SongSchema(PlainSongSchema):
    playlist_id = fields.Int(required=True, load_only=True)
    playlist = fields.Nested(PlainPlaylistSchema(), dump_only=True)
    
class PlaylistUpdateSchema(Schema):
    name = fields.Str()    

class PlaylistSchema(PlainPlaylistSchema):
    songs = fields.List(fields.Nested(PlainSongSchema()), dump_only=True)    

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True)

class UserRegisterSchema(UserSchema):
    email = fields.Str(required=True)