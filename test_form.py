from flask_wtf.csrf import generate_csrf
from app import app
from form import WordListForm

app.config['WTF_CSRF_ENABLED'] = False


class TestWordListForm:
    def test_wordlist_form_has_correct_fields(self):
        with app.test_request_context():
            form = WordListForm()

            assert 'name' in form.data
            assert 'difficulty' in form.data

    def test_wordlist_form_doesnt_include_unexpected_fields(self):
        with app.test_request_context():
            form = WordListForm()

            keys = list(form.data.keys())

            # Remove 'title', 'artist', and '_csrf' token keys from the keys list
            keys.remove('name')
            keys.remove('difficulty')
            keys.remove('word1')
            keys.remove('word2')
            keys.remove('word3')
            keys.remove('word4')
            keys.remove('word5')
            keys.remove('word6')
            keys.remove('word7')
            keys.remove('word8')
            keys.remove('word9')
            keys.remove('word10')
            keys.remove('word11')
            keys.remove('word12')
            keys.remove('word13')
            keys.remove('word14')
            keys.remove('word15')
            keys.remove('word16')
            keys.remove('word17')
            keys.remove('word18')
            keys.remove('word19')
            keys.remove('word20')

            # Check if there are any keys remaining in the list
            assert keys == [
            ], f"Unexpected fields found in the SongForm: {', '.join(keys)}"

    def test_wordlist_form_validation_is_working(self):
        with app.test_request_context(method="POST"):
            form = WordListForm()
            form.name.data = ''
            form.difficulty.data = 1
            assert form.validate_on_submit() is False

            form.name.data = 'test'
            form.difficulty.data = ''
            assert form.validate_on_submit() is False

            form.name.data = ''
            form.difficulty.data = ''
            assert form.validate_on_submit() is False

            form.name.data = 'title'
            form.difficulty.data = 1
            assert form.is_submitted() is True