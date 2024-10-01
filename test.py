import pytest
from main import count_vowels
@pytest.fixture
def vowel_strings():
    return {
        "only_vowels_lower": "аеёиоуыэюя",
        "only_vowels_upper": "АЕЁИОУЫЭЮЯ",
        "no_vowels_lower": "бвгджзйклмнпрстфхцчшщ",
        "no_vowels_upper": "БВГДЖЗЙКЛМНПРСТФХЦЧШЩ",
        "mixed_vowels": "Привет, программист!",
        "complex_string": "Тестирование фУнкцИй",
        "empty_string": ""
    }

def test_only_vowels(vowel_strings):
    assert count_vowels(vowel_strings["only_vowels_lower"]) == 10
    assert count_vowels(vowel_strings["only_vowels_upper"]) == 10

def test_no_vowels(vowel_strings):
    assert count_vowels(vowel_strings["no_vowels_lower"]) == 0
    assert count_vowels(vowel_strings["no_vowels_upper"]) == 0

def test_mixed_case_vowels(vowel_strings):
    assert count_vowels(vowel_strings["mixed_vowels"]) == 5  # 'и', 'е', 'о', 'а', 'и'
    assert count_vowels(vowel_strings["complex_string"]) == 8  # 'е', 'и', 'о', 'а', 'и', 'е', 'у', 'и'

def test_empty_string(vowel_strings):
    assert count_vowels(vowel_strings["empty_string"]) == 0
