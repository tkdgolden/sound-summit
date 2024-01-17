from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Sound(db.Model):
    """ all 39 phonetic sounds in English """

    __tablename__ = 'sounds'

    ipa_symbol = db.Column(
        db.Text,
        primary_key = True
    )


class Word(db.Model):
    """ words and their ids """  

    __tablename__ = 'words'

    word_id = db.Column(
        db.Integer,
        primary_key = True
    )

    word = db.Column(
        db.Text
    )

    sounds = db.relationship(
        'Sound',
        secondary = "wordsounds",
    )


class List(db.Model):
    """ a list name and difficulty level """

    __tablename__ = "lists"

    list_id = db.Column(
        db.Integer,
        primary_key = True
    )

    list_name = db.Column(
        db.Text,
    )

    difficulty = db.Column(
        db.Integer
    )

    words = db.relationship(
        'Word',
        secondary = "wordlists"
    )



class WordSound(db.Model):
    """ The sounds and their order within a word """
   
    __tablename__ = "wordsounds"

    id = db.Column(
        db.Integer,
        primary_key = True
    )

    word_id = db.Column(
        db.Integer,
        db.ForeignKey('words.word_id')
    )

    sound_symbol = db.Column(
        db.Text,
        db.ForeignKey('sounds.ipa_symbol')
    )

    index = db.Column(
        db.Integer
    )


class WordList(db.Model):
    """ relationship of words in lists """

    __tablename__ = "wordlists"

    id = db.Column(
        db.Integer,
        primary_key = True
    )

    list_id = db.Column(
        db.Integer,
        db.ForeignKey('lists.list_id')
    )

    word_id = db.Column(
        db.Integer,
        db.ForeignKey('words.word_id')
    )


def connect_db(app):
    """ connect to database """

    db.app = app
    db.init_app(app)