"""Models for capstone1 app"""
import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

class Medication(db.Model):
    """medication."""

    __tablename__ = "medications"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text, nullable=False)
    time_given = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.datetime.now) 
    refused = db.Column(db.Boolean, unique=False, default=True)
    



# class Song(db.Model):
#     """Song."""
#     __tablename__ = "songs"

#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     title = db.Column(db.Text, nullable=False)
#     artist = db.Column(db.Text, nullable=False)
#     playlist_song = db.relationship('PlaylistSong', backref='song')    


# class PlaylistSong(db.Model):
#     """Mapping of a playlist to a song."""

#     # ADD THE NECESSARY CODE HERE
#     __tablename__ = "playlists_songs"
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     playlist_id = db.Column(db.Integer, db.ForeignKey('playlists.id'),primary_key=True)
#     songlist_id = db.Column(db.Integer, db.ForeignKey('songs.id'),primary_key=True)
