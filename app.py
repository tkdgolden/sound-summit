from flask import Flask, redirect, render_template, request
from models import WordSound, db, connect_db, Word, Sound, List
from forms import WordListForm, EditListForm
import os

app = Flask(__name__)
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = (os.environ.get('DATABASE_URL', 'postgresql:///sound_summit'))

app.config['SECRET_KEY'] = "I'LL NEVER TELL!!"

connect_db(app)
db.create_all()

@app.route("/")
def index():
    """ Homepage """

    lists = List.query.all()

    return render_template("index.html", lists=lists)

@app.route("/new_wordlist", methods=["GET", "POST"])
def new_wordlist():
    """ Form for new list """

    form = WordListForm()

    if form.validate_on_submit():
        name = form.name.data
        difficulty = form.difficulty.data
        words = [form.word1.data, form.word2.data, form.word3.data, form.word4.data, form.word5.data, form.word6.data, form.word7.data, form.word8.data, form.word9.data, form.word10.data, form.word11.data, form.word12.data]

        list = List(list_name=name, difficulty=difficulty)
        for word in words:
            if word:
                w = Word(word=word)
                db.session.add(w)
                wpronunciation = w.get_sounds()
                wsounds = w.process_sounds(wpronunciation)
                counter = 0
                for sound in wsounds:
                    Sound.query.get_or_404(sound)
                    wsound = WordSound(word_id=w.word_id, sound_symbol=sound, index=counter)
                    db.session.add(wsound)
                    counter += 1
                db.session.commit()
                list.words.append(w)
        db.session.add(list)
        db.session.commit()
        
        return redirect(f"/edit/{list.list_id}")
    
    return render_template("new_wordlist.html", form=form)

@app.route("/<int:list_id>")
def gameplay(list_id):
    """ Play a game with the selected list """

    list = List.query.get_or_404(list_id)
    words = list.words
    word_sounds = {}
    for word in words:
        sounds = word.wordsounds
        sound_index = []
        for sound in sounds:
            s = Sound.query.filter(Sound.ipa_symbol == sound.sound_symbol).one()
            sound_index.append((s.keyword, s.ipa_symbol))
        word_sounds[word] = sound_index
    
    return render_template("gameplay.html", list=list, word_sounds=word_sounds)

@app.route("/educators")
def educators():
    lists = List.query.all()
    
    return render_template("educators.html", lists=lists)

@app.route("/edit/<int:list_id>", methods=["GET", "POST"])
def edit(list_id):
    form = EditListForm()
    list = List.query.get_or_404(list_id)
    words = list.words

    if form.validate_on_submit():
        difficulty = form.difficulty.data
        phonetics = [form.phon1.data, form.phon2.data, form.phon3.data, form.phon4.data, form.phon5.data, form.phon6.data, form.phon7.data, form.phon8.data, form.phon9.data, form.phon10.data, form.phon11.data, form.phon12.data]
        print(phonetics)
        list.difficulty = difficulty
        db.session.commit()
        for i in range(0, 11):
            print(i)
            print(words[i].word)
            WordSound.query.filter(WordSound.word_id == words[i].word_id).delete()
            wsounds = words[i].process_sounds(phonetics[i])

            counter = 0
            for sound in wsounds:
                print(sound)
                Sound.query.get_or_404(sound)
                wsound = WordSound(word_id=words[i].word_id, sound_symbol=sound, index=counter)
                db.session.add(wsound)
                counter += 1
            db.session.commit()

        return redirect("/educators")

    word_sounds = {}
    for word in words:
        sounds = word.wordsounds
        sound_index = []
        for sound in sounds:
            s = Sound.query.filter(Sound.ipa_symbol == sound.sound_symbol).one()
            sound_index.append((s.keyword, s.ipa_symbol))
        word_sounds[word] = sound_index
    all_sounds = Sound.query.all()
    
    return render_template("edit.html", list=list, word_sounds=word_sounds, all_sounds=all_sounds, form=form)