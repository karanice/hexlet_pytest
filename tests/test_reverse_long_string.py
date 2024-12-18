from hexlet_pytest.example import reverse
from pathlib import Path

def get_test_data_path(filename):
    return Path(__file__).parent / 'test_data' / filename

def read_file(filename):
    return get_test_data_path(filename).read_text()

def test_reverse_long_string():
    before = read_file('reverse_before.txt')
    expected = read_file('reverse_after.txt')
    actual = reverse(before)

    assert actual == expected