from flask_wtf.csrf import generate_csrf
from app import app
from forms import WordListForm, EditListForm

app.config['WTF_CSRF_ENABLED'] = False


class TestWordListForm:
    def test_wordlist_form_has_correct_fields(self):
        with app.test_request_context():
            form = WordListForm()

            assert 'name' in form.data
            assert 'difficulty' in form.data
            assert 'word1' in form.data
            assert 'word2' in form.data
            assert 'word3' in form.data
            assert 'word4' in form.data
            assert 'word5' in form.data
            assert 'word6' in form.data
            assert 'word7' in form.data
            assert 'word8' in form.data
            assert 'word9' in form.data
            assert 'word10' in form.data
            assert 'word11' in form.data
            assert 'word12' in form.data


    def test_wordlist_form_doesnt_include_unexpected_fields(self):
        with app.test_request_context():
            form = WordListForm()

            keys = list(form.data.keys())

            # Remove correct keys from the keys list
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

            # Check if there are any keys remaining in the list
            assert keys == [
            ], f"Unexpected fields found in the SongForm: {', '.join(keys)}"

    def test_wordlist_form_validation_is_working(self):
        with app.test_request_context(method="POST"):
            form = WordListForm()
            form.name.data = 'title'
            form.difficulty.data = 1
            form.word1.data = 'word'
            assert form.validate_on_submit() is False

            form = WordListForm()
            form.name.data = 'title'
            form.difficulty.data = ''
            form.word1.data = 'word'
            form.word2.data = 'word'
            form.word3.data = 'word'
            form.word4.data = 'word'
            form.word5.data = 'word'
            form.word6.data = 'word'
            form.word7.data = 'word'
            form.word8.data = 'word'
            form.word9.data = 'word'
            form.word10.data = 'word'
            form.word11.data = 'word'
            form.word12.data = 'word'
            assert form.validate_on_submit() is False

            form = WordListForm()
            form.name.data = ''
            form.difficulty.data = 1
            form.word1.data = 'word'
            form.word2.data = 'word'
            form.word3.data = 'word'
            form.word4.data = 'word'
            form.word5.data = 'word'
            form.word6.data = 'word'
            form.word7.data = 'word'
            form.word8.data = 'word'
            form.word9.data = 'word'
            form.word10.data = 'word'
            form.word11.data = 'word'
            form.word12.data = 'word'
            assert form.validate_on_submit() is False

            form = WordListForm()
            form.name.data = 'title'
            form.difficulty.data = 1
            form.word1.data = 'word'
            form.word2.data = 'word'
            form.word3.data = 'word'
            form.word4.data = 'word'
            form.word5.data = 'word'
            form.word6.data = 'word'
            form.word7.data = 'word'
            form.word8.data = 'word'
            form.word9.data = 'word'
            form.word10.data = 'word'
            form.word11.data = 'word'
            form.word12.data = 'word'
            assert form.is_submitted() is True

class TestEditListForm:
    def test_edit_list_form_has_correct_fields(self):
        with app.test_request_context():
            form = EditListForm()

            assert 'difficulty' in form.data
            assert 'phon1' in form.data
            assert 'phon2' in form.data
            assert 'phon3' in form.data
            assert 'phon4' in form.data
            assert 'phon5' in form.data
            assert 'phon6' in form.data
            assert 'phon7' in form.data
            assert 'phon8' in form.data
            assert 'phon9' in form.data
            assert 'phon10' in form.data
            assert 'phon11' in form.data
            assert 'phon12' in form.data


    def test_edit_list_form_doesnt_include_unexpected_fields(self):
        with app.test_request_context():
            form = EditListForm()

            keys = list(form.data.keys())

            # Remove correct keys from the keys list
            keys.remove('difficulty')
            keys.remove('phon1')
            keys.remove('phon2')
            keys.remove('phon3')
            keys.remove('phon4')
            keys.remove('phon5')
            keys.remove('phon6')
            keys.remove('phon7')
            keys.remove('phon8')
            keys.remove('phon9')
            keys.remove('phon10')
            keys.remove('phon11')
            keys.remove('phon12')

            # Check if there are any keys remaining in the list
            assert keys == [
            ], f"Unexpected fields found in the SongForm: {', '.join(keys)}"

    def test_edit_list_form_validation_is_working(self):
        with app.test_request_context(method="POST"):
            form = EditListForm()
            form.difficulty.data = 1
            form.phon1.data = 'word'
            assert form.validate_on_submit() is False

            form = EditListForm()
            form.difficulty.data = 1
            form.phon1.data = ''
            form.phon2.data = 'word'
            form.phon3.data = 'word'
            form.phon4.data = 'word'
            form.phon5.data = 'word'
            form.phon6.data = 'word'
            form.phon7.data = 'word'
            form.phon8.data = 'word'
            form.phon9.data = 'word'
            form.phon10.data = 'word'
            form.phon11.data = 'word'
            form.phon12.data = 'word'
            assert form.validate_on_submit() is False

            form = EditListForm()
            form.difficulty.data = 1
            form.phon1.data = 'word'
            form.phon2.data = 'word'
            form.phon3.data = 'word'
            form.phon4.data = 'word'
            form.phon5.data = 'word'
            form.phon6.data = 'word'
            form.phon7.data = 'word'
            form.phon8.data = 'word'
            form.phon9.data = 'word'
            form.phon10.data = 'word'
            form.phon11.data = 'word'
            form.phon12.data = 'word'
            assert form.is_submitted() is True