""" form for new wordlist """

from wtforms import StringField, IntegerField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired

class WordListForm(FlaskForm):
    """ form for adding list """

    name = StringField("Name:", validators=[InputRequired()])
    difficulty = IntegerField("Difficulty Level:", validators=[InputRequired()])
    word1 = StringField("Add a Word:")
    word2 = StringField("Add a Word:")
    word3 = StringField("Add a Word:")
    word4 = StringField("Add a Word:")
    word5 = StringField("Add a Word:")
    word6 = StringField("Add a Word:")
    word7 = StringField("Add a Word:")
    word8 = StringField("Add a Word:")
    word9 = StringField("Add a Word:")
    word10 = StringField("Add a Word:")
    word11 = StringField("Add a Word:")
    word12 = StringField("Add a Word:")
    word13 = StringField("Add a Word:")
    word14 = StringField("Add a Word:")
    word15 = StringField("Add a Word:")
    word16 = StringField("Add a Word:")
    word17 = StringField("Add a Word:")
    word18 = StringField("Add a Word:")
    word19 = StringField("Add a Word:")
    word20 = StringField("Add a Word:")