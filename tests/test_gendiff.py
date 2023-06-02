from gendiff.generate import generate_diff
from .fixtures.right_result import RIGHT_RESULT

def test_generate_diff():
    assert RIGHT_RESULT == generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')
