POETRY = $(shell command -v poetry 2>/dev/null || python3 -c "import sys; import os; bin_path = os.path.join(os.path.expanduser('~'), 'Library', 'Python', f'{sys.version_info.major}.{sys.version_info.minor}', 'bin', 'poetry'); print(bin_path if os.path.exists(bin_path) else 'poetry')")

install:
	$(POETRY) install

project:
	$(POETRY) run project

build:
	$(POETRY) build

publish:
	$(POETRY) publish --dry-run

package-install:
	python3 -m pip install dist/*.whl

lint:
	$(POETRY) run ruff check .

