import pytest
from app import count_word_frequency

def test_count_word_frequency():
    text = "This is a test. This test is only a test."
    # Expected result with stop words filtered out
    expected_result = {"test": 3, "only": 1}
    result = count_word_frequency(text)
    assert result == expected_result

def test_count_word_frequency_no_stopwords():
    text = "This is a test. This test is only a test."
    # Expected result without filtering stop words
    expected_result = {"this": 2, "is": 2, "a": 2, "test": 3, "only": 1}
    result = count_word_frequency(text, filter_stop_words=False)
    assert result == expected_result
