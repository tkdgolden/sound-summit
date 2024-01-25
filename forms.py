""" form for new wordlist """

from wtforms import StringField, IntegerField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired

class WordListForm(FlaskForm):
    """ form for adding list """

    name = StringField("Name:", validators=[InputRequired()])
    difficulty = IntegerField("Difficulty Level:", validators=[InputRequired()])
    word1 = StringField("Add a Word:", validators=[InputRequired()])
    word2 = StringField("Add a Word:", validators=[InputRequired()])
    word3 = StringField("Add a Word:", validators=[InputRequired()])
    word4 = StringField("Add a Word:", validators=[InputRequired()])
    word5 = StringField("Add a Word:", validators=[InputRequired()])
    word6 = StringField("Add a Word:", validators=[InputRequired()])
    word7 = StringField("Add a Word:", validators=[InputRequired()])
    word8 = StringField("Add a Word:", validators=[InputRequired()])
    word9 = StringField("Add a Word:", validators=[InputRequired()])
    word10 = StringField("Add a Word:", validators=[InputRequired()])
    word11 = StringField("Add a Word:", validators=[InputRequired()])
    word12 = StringField("Add a Word:", validators=[InputRequired()])

class EditListForm(FlaskForm):
    """ form for editing word sounds """

    phon1 = StringField(validators=[InputRequired()])
    phon2 = StringField(validators=[InputRequired()])
    phon3 = StringField(validators=[InputRequired()])
    phon4 = StringField(validators=[InputRequired()])
    phon5 = StringField(validators=[InputRequired()])
    phon6 = StringField(validators=[InputRequired()])
    phon7 = StringField(validators=[InputRequired()])
    phon8 = StringField(validators=[InputRequired()])
    phon9 = StringField(validators=[InputRequired()])
    phon10 = StringField(validators=[InputRequired()])
    phon11 = StringField(validators=[InputRequired()])
    phon12 = StringField(validators=[InputRequired()])
    difficulty = IntegerField(validators=[InputRequired()])