build:
	uv build
	
install:
	uv sync

reinstall:
	uv sync
	uv build
	uv tool install --force dist/*.whl

package-install:
	uv tool install dist/*.whl

force_package:
	uv tool install --force dist/*.whl
lint:
	uv run ruff check

check:
	lint
		
test-coverage:
	uv run pytest --cov=gendiff --cov-report xml
