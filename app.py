from flask import Flask
from models import db, connect_db, Word, Sound, List, WordList, WordSound

app = Flask(__name__)
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///sound_summit'

connect_db(app)
db.create_all()