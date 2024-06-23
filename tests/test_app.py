import pytest
from app import count_word_frequency

def test_count_word_frequency():
    text = "This is a test. This test is only a test."
    # Expected result with stop words filtered out
    expected_result = {"test": 3, "only": 1}
    result = count_word_frequency(text)
    assert result == expected_result
