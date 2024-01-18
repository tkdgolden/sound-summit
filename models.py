from flask import json
from flask_sqlalchemy import SQLAlchemy
import requests

db = SQLAlchemy()

VOWELS = ("u", "aʊ", "ɑ", "ə", "oʊ", "i", "eɪ", "aɪ", "ɔ", "ɪ", "ɜ", "ɛ", "æ", "ɔɪ", "ʊ", "ɨ", "ʌ", "o", "ɯ", "a", "o", "e")
SPECIAL_CHARS = ("ˈ", "ˌ", ".")

class Sound(db.Model):
    """ all 39 phonetic sounds in English plus 5 that ibm uses that arent ipa """

    __tablename__ = 'sounds'

    ipa_symbol = db.Column(
        db.Text,
        primary_key = True
    )

    keyword = db.Column(
        db.Text
    )

    def __repr__(self):
        """ displays sound """

        return f"<Sound {self.ipa_symbol}: {self.keyword}>"


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

    wordsounds = db.relationship(
        'WordSound'
    )

    def get_sounds(self):
        """ get an array of all the sounds that make up a word """

        url = "https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/623179bf-4231-4589-8043-efdce997209b/v1/pronunciation"

        payload = {
            "text": self.word,
            "format": "ipa"
        }
        headers = {
            "Content-Type": "application/json",
            "User-Agent": "insomnia/8.5.1",
            "Authorization": "Basic YXBpa2V5OlhoQmVqeTJCQTEwakI1a0dTVUR2SnBfM04zUUk3ZXpTMUJ0bjRfbzlQM0RD"
        }

        response = requests.request("POST", url, json=payload, headers=headers)
        pronunciation = json.loads(response.text)["pronunciation"]
        print(pronunciation)
        sounds = []
        prev = ""
        for char in pronunciation:
            if char in SPECIAL_CHARS:
                if prev in VOWELS:
                    sounds.append(prev)
                    prev = ""
                else:
                    prev = ""
            elif char in VOWELS:
                if prev in VOWELS:
                    combined = prev + char
                    sounds.append(combined)
                    prev = ""
                else:
                    prev = char
            else:
                if prev in VOWELS:
                    sounds.append(prev)
                    sounds.append(char)
                    prev = ""
                else:
                    sounds.append(char)
                    prev = ""
        if prev in VOWELS:
            sounds.append(prev)

        print(sounds)
        return sounds
    
    def __repr__(self):
        return f"<Word #{self.word_id}: {self.word}, {self.wordsounds}>"


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

    def __repr__(self):
        return f"<List #{self.list_id}: {self.list_name}, {self.difficulty}, {self.words}>"


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

    def __repr__(self):
        """ display wordsound """

        return f"<WordSound {self.id}: word({self.word_id}, sound({self.sound_symbol}), index({self.index})>"


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