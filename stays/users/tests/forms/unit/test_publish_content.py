import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from faker import Faker

from users.forms import PublishContentForm

fake = Faker()


@pytest.fixture
def form_data():
    return {
        "content_type": "text",
        "title": fake.sentence(),
        "author_slug": fake.slug(),
        "author_username": fake.user_name(),
        "country_code_of_stay": "US",
        "published_from_country_code": "IT",
        "summary": fake.text(),
        "picture": SimpleUploadedFile(
            "profile_pic.jpg", b"file_content", content_type="image/jpeg"
        ),
        "year_of_stay": fake.year(),
        "season_of_stay": "Spring",
        "text_story": fake.text(),
        "voice_story": SimpleUploadedFile(
            "voice_story.mp3", b"file_content", content_type="audio/mpeg"
        ),
    }


def test_form_invalid_with_both_text_and_voice(form_data):
    form = PublishContentForm(data=form_data)
    assert not form.is_valid()


def test_form_invalid_without_content_type(form_data):
    form_data.pop("content_type")
    form = PublishContentForm(data=form_data)
    assert not form.is_valid()


def test_form_invalid_without_title(form_data):
    form_data.pop("title")
    form = PublishContentForm(data=form_data)
    assert not form.is_valid()


def test_form_invalid_without_author_slug(form_data):
    form_data.pop("author_slug")
    form = PublishContentForm(data=form_data)
    assert not form.is_valid()


def test_form_invalid_without_author_username(form_data):
    form_data.pop("author_username")
    form = PublishContentForm(data=form_data)
    assert not form.is_valid()


def test_form_invalid_without_country_code_of_stay(form_data):
    form_data.pop("country_code_of_stay")
    form = PublishContentForm(data=form_data)
    assert not form.is_valid()


def test_form_invalid_without_published_from_country_code(form_data):
    form_data.pop("published_from_country_code")
    form = PublishContentForm(data=form_data)
    assert not form.is_valid()


def test_form_invalid_without_summary(form_data):
    form_data.pop("summary")
    form = PublishContentForm(data=form_data)
    assert not form.is_valid()


def test_form_invalid_without_picture(form_data):
    form_data.pop("picture")
    form = PublishContentForm(data=form_data)
    assert not form.is_valid()


def test_form_invalid_without_year_of_stay(form_data):
    form_data.pop("year_of_stay")
    form = PublishContentForm(data=form_data)
    assert not form.is_valid()


def test_form_invalid_without_story(form_data):
    form_data["text_story"] = None
    form_data["voice_story"] = None
    form = PublishContentForm(data=form_data)
    assert not form.is_valid()


def test_form_valid_with_text_story(form_data):
    form_data["voice_story"] = None
    form = PublishContentForm(data=form_data)
    assert not form.is_valid()


def test_form_valid_with_voice_story(form_data):
    form_data["text_story"] = None
    form = PublishContentForm(data=form_data)
    assert not form.is_valid()
