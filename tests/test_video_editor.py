import pytest

from text_to_video.video_editor import VideoEditor

@pytest.fixture
def video_editor():
    return VideoEditor()

def test_add_text(video_editor):
    # TODO: Implement test for adding text to video
    assert True

def test_remove_text(video_editor):
    # TODO: Implement test for removing text from video
    assert True

def test_edit_text(video_editor):
    # TODO: Implement test for editing text in video
    assert True

def test_export_video(video_editor):
    # TODO: Implement test for exporting video
    assert True
