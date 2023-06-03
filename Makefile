make lint:
	poetry run flake8 gendiff

package-reinstall:
	pip install --user --force-reinstall dist/*.whl