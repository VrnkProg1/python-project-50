from gendiff.difference_checker import generate_diff
from fixtures.right import RIGHT_RESULT


def test_gendiff_json():
	assert RIGHT_RESULT == generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json')

def test_gendiff_yml():
	assert RIGHT_RESULT == generate_diff('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml')
	assert RIGHT_RESULT == generate_diff('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yaml')
	assert RIGHT_RESULT == generate_diff('tests/fixtures/file1.yaml', 'tests/fixtures/file2.yml')
	assert RIGHT_RESULT == generate_diff('tests/fixtures/file1.yml', 'tests/fixtures/file2.yaml')

def test_gendiff_yml_json():
	assert RIGHT_RESULT == generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.yml')
	assert RIGHT_RESULT == generate_diff('tests/fixtures/file1.yml', 'tests/fixtures/file2.json')
	assert RIGHT_RESULT == generate_diff('tests/fixtures/file1.yaml', 'tests/fixtures/file2.json')
	assert RIGHT_RESULT == generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.yaml')