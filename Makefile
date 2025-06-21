build:
	uv build
	
install:
	uv sync

package-install:
	uv tool install dist/*.whl

force_package:
	uv tool install --force dist/*.whl
