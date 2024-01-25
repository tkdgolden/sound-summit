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

        WordList.query.delete()
        WordSound.query.delete()
        Sound.query.delete()
        Word.query.delete()
        List.query.delete()

        self.client = app.test_client()

    def tearDown(self):
        """ tears down session from bad failed commits """

        db.session.rollback()
        db.session.remove()

    def test_sound_model(self):
        """ does basic model work? """

        a = Sound(ipa_symbol="a", keyword="TEST")

        db.session.add(a)
        db.session.commit()

        self.assertEqual(a.ipa_symbol, "a")
        self.assertEqual(a.keyword, "TEST")

    def test_sound_repr_method(self):
        """ does sound display as expected? """

        a = Sound(ipa_symbol="a", keyword="TEST")

        db.session.add(a)
        db.session.commit()

        display = a.__repr__()

        self.assertEqual(display, "<Sound a: TEST>")


class WordModelTestCase(TestCase):
    """ Test word """

    def setUp(self):
        """ create test client, add sample data """

        WordList.query.delete()
        WordSound.query.delete()
        Sound.query.delete()
        Word.query.delete()
        List.query.delete()

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
    
    def test_word_repr_method(self):
        """ does the repr look like expected? """

        a = Sound(ipa_symbol="a", keyword="TEST")
        apple = Word(word="apple")

        db.session.add(apple)
        db.session.add(a)
        db.session.commit()

        sound = WordSound(word_id = apple.word_id, sound_symbol=a.ipa_symbol, index=0)

        db.session.add(sound)

        display = apple.__repr__()
        self.assertEqual(display, f"<Word #{apple.word_id}: apple, [<WordSound {sound.id}: word({apple.word_id}), sound({a.ipa_symbol}), index({sound.index})>]>")

    def test_word_process_sounds_method(self):
        """ does method correctly call API for pronunciation and return array of ipa symbols? """

        apple = Word(word="apple")

        db.session.add(apple)

        apple_sounds = apple.process_sounds('.ˈæ.pəl')
        self.assertEqual(apple_sounds, ["æ", "p", "ə", "l"])
        
    def test_word_get_sounds_method(self):
        """ does method correctly call API for pronunciation and return array of ipa symbols? """

        apple = Word(word="apple")

        db.session.add(apple)
        apple_pronunciation = apple.get_sounds()
        print(apple_pronunciation)
        self.assertEqual(apple_pronunciation, ["æ", "p", "ə", "l"])


class ListModelTestCase(TestCase):
    """ Test list """

    def setUp(self):
        """ create test client, add sample data """

        WordList.query.delete()
        WordSound.query.delete()
        Sound.query.delete()
        Word.query.delete()
        List.query.delete()

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

    def test_list_repr_method(self):
        """ does list display as expected? """

        apple = Word(word="apple")
        fruit = List(list_name="fruit", difficulty=1)
        a = Sound(ipa_symbol="a", keyword="TEST")
        db.session.add(a)
        db.session.add(fruit)
        db.session.add(apple)
        db.session.commit()
        sound = WordSound(word_id=apple.word_id, sound_symbol=a.ipa_symbol, index=1)
        db.session.add(sound)
        db.session.commit()

        word = WordList(word_id = apple.word_id, list_id = fruit.list_id)

        db.session.add(word)
        display = fruit.__repr__()

        self.assertEqual(display, f"<List #{fruit.list_id}: fruit, 1, [<Word #{apple.word_id}: apple, [<WordSound {sound.id}: word({apple.word_id}), sound({a.ipa_symbol}), index({sound.index})>]>]>")


class WordSoundModelTestCase(TestCase):
    """ Test wordsound """

    def setUp(self):
        """ create test client, add sample data """

        WordList.query.delete()
        WordSound.query.delete()
        Sound.query.delete()
        Word.query.delete()
        List.query.delete()

        self.client = app.test_client()

    def tearDown(self):
        """ tears down session from bad failed commits """

        db.session.rollback()
        db.session.remove()

    def test_wordsound_model(self):
        """ does basic model work? """

        a = Sound(ipa_symbol="a", keyword="TEST")
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

        a = Sound(ipa_symbol="a", keyword="TEST")
        apple = Word(word="apple")

        db.session.add(apple)
        db.session.add(a)
        db.session.commit()

        sound = WordSound(word_id = apple.word_id, sound_symbol=a.ipa_symbol, index=0)

        db.session.add(sound)

        self.assertIn(a.ipa_symbol, apple.wordsounds[0].sound_symbol)


class WordListModelTestCase(TestCase):
    """ Test wordlist """

    def setUp(self):
        """ create test client, add sample data """

        WordList.query.delete()
        WordSound.query.delete()
        Sound.query.delete()
        Word.query.delete()
        List.query.delete()

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