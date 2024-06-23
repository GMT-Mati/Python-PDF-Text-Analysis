import pytest
from app import count_word_frequency

def test_count_word_frequency():
    text = "Hello world! Hello everyone."
    expected_result = {"hello": 2, "world": 1, "everyone": 1}
    result = count_word_frequency(text, filter_stop_words=False)
    assert result == expected_result
