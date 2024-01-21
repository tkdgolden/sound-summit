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
        
        self.assertIn("<h1>Sound Summit Explorers</h1>", html)


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
            resp = c.post("/new_wordlist", data={"name": "test", "difficulty": 1, "word1": "apple"})

        self.assertEqual(resp.status_code, 302)
        self.assertEqual(resp.location, "/")

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
            resp = c.post("/new_wordlist", data={"name": "test", "difficulty": 1, "word1": "apple"}, follow_redirects=True)
            html = resp.get_data(as_text=True)

        self.assertEqual(resp.status_code, 200)
        self.assertIn("<button>test</button>", html)


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
            resp = c.post("/new_wordlist", data={"name": "test", "difficulty": 1, "word1": "apple"}, follow_redirects=True)
            html = resp.get_data(as_text=True)

        list = List.query.filter(List.list_name == "test").one()

        with self.client as c:
            resp = c.get(f"/{list.list_id}")
            html = resp.get_data(as_text=True)
        
        self.assertIn(f'<h1 id="title" data-difficulty="{list.difficulty}" data-list="{list.list_id}">test</h1>', html)