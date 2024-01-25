""" Route Tests """

import os
from unittest import TestCase
from models import db, Word, Sound, List, WordList, WordSound

os.environ['DATABASE_URL'] = "postgresql:///sound_summit_test"

from app import app

db.create_all()

app.config['WTF_CSRF_ENABLED'] = False


class IndexTestCase(TestCase):
    """ Test views on index page. """

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

    def test_index_view(self):
        """ Display homepage """

        with self.client as c:
            resp = c.get("/")
            html = resp.get_data(as_text=True)
        
        self.assertIn('<h1 id="title">Sound Summit Explorers</h1>', html)


class NewWordListTestCase(TestCase):
    """ Tests new wordlist view """

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

    def test_new_wordlist_view(self):
        """ Display new wordlist form """

        with self.client as c:
            resp = c.get("/new_wordlist")
            html = resp.get_data(as_text=True)
        
        self.assertIn("<h1>Create a new list</h1>", html)

    def test_submit_new_wordlist(self):
        """ Submit new wordlist form """
        
        self.assertEqual([], List.query.all())
        # æ.pəl
        a = Sound(ipa_symbol="æ")
        db.session.add(a)
        b = Sound(ipa_symbol="p")
        db.session.add(b)
        c = Sound(ipa_symbol="ə")
        db.session.add(c)
        d = Sound(ipa_symbol="l")
        db.session.add(d)

        with self.client as c:
            resp = c.post("/new_wordlist", data={"name": "test", "difficulty": 1, "word1": "apple", "word2": "apple", "word3": "apple", "word4": "apple", "word5": "apple", "word6": "apple", "word7": "apple", "word8": "apple", "word9": "apple", "word10": "apple", "word11": "apple", "word12": "apple"})

        list = List.query.filter(List.list_name == "test").one()

        self.assertIn(list.words[0].word, "apple")
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(resp.location, f"/edit/{list.list_id}")

    def test_fail_submit_new_wordlist_not_12(self):
        """ Submit new wordlist form """
        
        self.assertEqual([], List.query.all())
        # æ.pəl
        a = Sound(ipa_symbol="æ")
        db.session.add(a)
        b = Sound(ipa_symbol="p")
        db.session.add(b)
        c = Sound(ipa_symbol="ə")
        db.session.add(c)
        d = Sound(ipa_symbol="l")
        db.session.add(d)

        with self.client as c:
            resp = c.post("/new_wordlist", data={"name": "test", "difficulty": 1, "word1": "apple"})

        self.assertEqual(resp.location, None)

    def test_submit_new_wordlist_follow_redirect(self):
        """ Submit new wordlist form """
        
        self.assertEqual([], List.query.all())
        # æpəl
        a = Sound(ipa_symbol="æ")
        db.session.add(a)
        b = Sound(ipa_symbol="p")
        db.session.add(b)
        c = Sound(ipa_symbol="ə")
        db.session.add(c)
        d = Sound(ipa_symbol="l")
        db.session.add(d)

        with self.client as c:
            resp = c.post("/new_wordlist", data={"name": "test", "difficulty": 1, "word1": "apple", "word2": "apple", "word3": "apple", "word4": "apple", "word5": "apple", "word6": "apple", "word7": "apple", "word8": "apple", "word9": "apple", "word10": "apple", "word11": "apple", "word12": "apple"}, follow_redirects=True)
            html = resp.get_data(as_text=True)

        list = List.query.filter(List.list_name == "test").one()

        self.assertEqual(resp.status_code, 200)
        self.assertIn(f'<h1 id="title" data-list="{ list.list_id }" class="d-inline">Edit test</h1>', html)


class GameplayTestCase(TestCase):
    """ Tests new gameplay view """

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

    def test_gameplay_view(self):
        """ Display new wordlist info necessary to run game """

        a = Sound(ipa_symbol="æ")
        db.session.add(a)
        b = Sound(ipa_symbol="p")
        db.session.add(b)
        c = Sound(ipa_symbol="ə")
        db.session.add(c)
        d = Sound(ipa_symbol="l")
        db.session.add(d)

        with self.client as c:
            resp = c.post("/new_wordlist", data={"name": "test", "difficulty": 1, "word1": "apple", "word2": "apple", "word3": "apple", "word4": "apple", "word5": "apple", "word6": "apple", "word7": "apple", "word8": "apple", "word9": "apple", "word10": "apple", "word11": "apple", "word12": "apple"}, follow_redirects=True)
            html = resp.get_data(as_text=True)

        list = List.query.filter(List.list_name == "test").one()

        with self.client as c:
            resp = c.get(f"/{list.list_id}")
            html = resp.get_data(as_text=True)
        
        self.assertIn(f'<h1 id="title" data-difficulty="1" data-list="{ list.list_id }" class="d-inline">test</h1>', html)

class EducatorsTestCase(TestCase):
    """ Test views on educator page. """

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

    def test_educators_view(self):
        """ display educator page """

        with self.client as c:
            resp = c.get("/educators")
            html = resp.get_data(as_text=True)
        
        self.assertIn('<h1 id="title" class="d-inline">Educators Options</h1>', html)

class EditTestCase(TestCase):
    """ Test views on educator page. """

    def setUp(self):
        """ create test client, add sample data """

        WordList.query.delete()
        WordSound.query.delete()
        Sound.query.delete()
        Word.query.delete()
        List.query.delete()

        self.client = app.test_client()

        self.assertEqual([], List.query.all())
        # æ.pəl
        a = Sound(ipa_symbol="æ")
        db.session.add(a)
        b = Sound(ipa_symbol="p")
        db.session.add(b)
        c = Sound(ipa_symbol="ə")
        db.session.add(c)
        d = Sound(ipa_symbol="l")
        db.session.add(d)

        with self.client as c:
            resp = c.post("/new_wordlist", data={"name": "test", "difficulty": 1, "word1": "apple", "word2": "apple", "word3": "apple", "word4": "apple", "word5": "apple", "word6": "apple", "word7": "apple", "word8": "apple", "word9": "apple", "word10": "apple", "word11": "apple", "word12": "apple"})

        list = List.query.filter(List.list_name == "test").one()

        self.assertEqual(resp.status_code, 302)
        self.assertEqual(resp.location, f"/edit/{list.list_id}")

    def tearDown(self):
        """ tears down session from bad failed commits """

        db.session.rollback()
        db.session.remove()

    def test_edit_view(self):
        """ display educator page """

        list = List.query.filter(List.list_name == "test").one()

        with self.client as c:
            resp = c.get(f"/edit/{list.list_id}")
            html = resp.get_data(as_text=True)

        self.assertEqual(resp.status_code, 200)
        self.assertIn(f'<h1 id="title" data-list="{ list.list_id }" class="d-inline">Edit test</h1>', html)

    def test_edit_submission(self):
        """ submit edit form """

        list = List.query.filter(List.list_name == "test").one()

        with self.client as c:
            resp = c.post(f"/edit/{list.list_id}", data={"difficulty": 2, "phon1": "pæ", "phon2": "æpəl", "phon3": "æpəl", "phon4": "æpəl", "phon5": "æpəl", "phon6": "æpəl", "phon7": "æpəl", "phon8": "æpəl", "phon9": "æpəl", "phon10": "æpəl", "phon11": "æpəl", "phon12": "æpəl"})

        self.assertEqual(list.difficulty, 2)
        self.assertEqual(list.words[0].wordsounds[0].sound_symbol, "p")
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(resp.location, "/educators")

    def test_edit_submission_redirect(self):
        """ redirect after edit form submission """

        list = List.query.filter(List.list_name == "test").one()

        with self.client as c:
            resp = c.post(f"/edit/{list.list_id}", data={"difficulty": 2, "phon1": "pæ", "phon2": "æpəl", "phon3": "æpəl", "phon4": "æpəl", "phon5": "æpəl", "phon6": "æpəl", "phon7": "æpəl", "phon8": "æpəl", "phon9": "æpəl", "phon10": "æpəl", "phon11": "æpəl", "phon12": "æpəl"}, follow_redirects=True)
            html = resp.get_data(as_text=True)

        self.assertEqual(resp.status_code, 200)
        self.assertIn(f'<button class="btn btn-warning">{ list.list_name }</button>', html)