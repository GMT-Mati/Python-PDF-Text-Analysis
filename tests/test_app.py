import pytest
from app import count_word_frequency

def test_count_word_frequency():
    text = "This is a test. This test is only a test."
    expected_result = {"this": 2, "test": 3, "only": 1}
    result = count_word_frequency(text)
    assert result == expected_result
