make lint:
	poetry run flake8 packages

package-reinstall:
	pip install --user --force-reinstall dist/*.whl