""" models tests """

# run with:
# python -m unittest

import os
from unittest import TestCase
from models import db, Word, Sound, List, WordList, WordSound

os.environ['DATABASE_URL'] = "postgresql:///sound_summit_test"

from app import app

db.create_all()


class SoundModelTestCase(TestCase):
    """ Test sounds """

    def setUp(self):
        """ create test client, add sample data """

        Sound.query.delete()
        Word.query.delete()
        List.query.delete()
        WordList.query.delete()
        WordSound.query.delete()

        self.client = app.test_client()

    def tearDown(self):
        """ tears down session from bad failed commits """

        db.session.rollback()
        db.session.remove()

    def test_sound_model(self):
        """ does basic model work? """

        a = Sound(ipa_symbol="a")

        db.session.add(a)
        db.session.commit()

        self.assertEqual(a.ipa_symbol, "a")


class WordModelTestCase(TestCase):
    """ Test word """

    def setUp(self):
        """ create test client, add sample data """

        Sound.query.delete()
        Word.query.delete()
        List.query.delete()
        WordList.query.delete()
        WordSound.query.delete()

        self.client = app.test_client()

    def tearDown(self):
        """ tears down session from bad failed commits """

        db.session.rollback()
        db.session.remove()

    def test_word_model(self):
        """ does basic model work? """

        apple = Word(word="apple")

        db.session.add(apple)
        db.session.commit()

        self.assertEqual(apple.word, "apple")


class ListModelTestCase(TestCase):
    """ Test list """

    def setUp(self):
        """ create test client, add sample data """

        Sound.query.delete()
        Word.query.delete()
        List.query.delete()
        WordList.query.delete()
        WordSound.query.delete()

        self.client = app.test_client()

    def tearDown(self):
        """ tears down session from bad failed commits """

        db.session.rollback()
        db.session.remove()

    def test_list_model(self):
        """ does basic model work? """

        fruit = List(list_name="fruit", difficulty=1)

        db.session.add(fruit)
        db.session.commit()

        self.assertEqual(fruit.list_name, "fruit")
        self.assertEqual(fruit.difficulty, 1)


class WordSoundModelTestCase(TestCase):
    """ Test wordsound """

    def setUp(self):
        """ create test client, add sample data """

        Sound.query.delete()
        Word.query.delete()
        List.query.delete()
        WordList.query.delete()
        WordSound.query.delete()

        self.client = app.test_client()

    def tearDown(self):
        """ tears down session from bad failed commits """

        db.session.rollback()
        db.session.remove()

    def test_wordsound_model(self):
        """ does basic model work? """

        a = Sound(ipa_symbol="a")
        apple = Word(word="apple")

        db.session.add(apple)
        db.session.add(a)
        db.session.commit()

        sound = WordSound(word_id = apple.word_id, sound_symbol=a.ipa_symbol, index=0)

        db.session.add(sound)

        self.assertEqual(sound.word_id, apple.word_id)
        self.assertEqual(sound.sound_symbol, a.ipa_symbol)
        self.assertEqual(sound.index, 0)

    def test_wordsound_relationships(self):
        """ do word and sound connect? """

        a = Sound(ipa_symbol="a")
        apple = Word(word="apple")

        db.session.add(apple)
        db.session.add(a)
        db.session.commit()

        sound = WordSound(word_id = apple.word_id, sound_symbol=a.ipa_symbol, index=0)

        db.session.add(sound)

        self.assertIn(a, apple.sounds)


class WordListModelTestCase(TestCase):
    """ Test wordlist """

    def setUp(self):
        """ create test client, add sample data """

        Sound.query.delete()
        Word.query.delete()
        List.query.delete()
        WordList.query.delete()
        WordSound.query.delete()

        self.client = app.test_client()

    def tearDown(self):
        """ tears down session from bad failed commits """

        db.session.rollback()
        db.session.remove()

    def test_wordlist_model(self):
        """ does basic model work? """

        apple = Word(word="apple")
        fruit = List(list_name="fruit", difficulty=1)

        db.session.add(fruit)
        db.session.add(apple)
        db.session.commit()

        word = WordList(word_id = apple.word_id, list_id = fruit.list_id)

        db.session.add(word)

        self.assertEqual(word.word_id, apple.word_id)
        self.assertEqual(word.list_id, fruit.list_id)

    def test_wordlist_relationship(self):
        """ does word and list connect? """

        apple = Word(word="apple")
        fruit = List(list_name="fruit", difficulty=1)

        db.session.add(fruit)
        db.session.add(apple)
        db.session.commit()

        word = WordList(word_id = apple.word_id, list_id = fruit.list_id)

        db.session.add(word)

        self.assertIn(apple, fruit.words)